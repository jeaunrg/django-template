from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify
from editable.data import *


def to_choice(data, add_empty=True):
    if isinstance(data, dict):
        choices = [(i, i) for i in data.keys()]
    else:
        choices = [(i, i) for i in data]
    if add_empty:
        choices = [("", "")] + choices
    return choices


class Patient(models.Model):
    # -------------------- PREOP -----------------#
    # patient
    firstname = models.CharField("prénom", max_length=200, blank=True, default="")
    lastname = models.CharField("nom", max_length=200, blank=True, default="")
    height = models.IntegerField("taille", null=True, blank=True)
    weight = models.IntegerField("poids", null=True, blank=True)
    ddn = models.DateField("Date de naissance", null=True, blank=True)

    # intervention
    ddi = models.DateField("Date de l'intervention", null=True, blank=True)
    intervention = models.CharField(
        "intervention", max_length=200, default="", blank=True
    )
    chirurgien = models.CharField("chirurgien", max_length=200, default="", blank=True)
    chirurgie = models.CharField(
        "Discipline de l'intervention",
        max_length=40,
        choices=to_choice(CHIR_CHOICES),
        blank=True,
    )
    bleeding_risk = models.CharField(
        "Risque hémorragique de la chirurgie",
        max_length=100,
        choices=to_choice(BLEEDRISK_CHOICES),
        blank=True,
    )

    # consultation
    ddconsult = models.DateField(
        "Date de la consultation", auto_now_add=True, blank=True
    )

    # traitement
    traitements = models.JSONField(default=dict, blank=True)

    # -------------------- ALGO -----------------#
    algo = models.CharField(
        "Algorithme suivi", max_length=40, choices=to_choice(ALGO_CHOICES), blank=True
    )
    algo_complete_results = models.JSONField(default=dict, blank=True)

    # -------------------- POSTOP -----------------#
    schema_therap = models.CharField(
        "Schéma thérapeutique donné au patient",
        max_length=40,
        default="Date exacte",
        choices=to_choice(
            [
                "Date exacte",
                "Terminologie 'dernière prise à J-xx'",
                "Pas d'arrêt du traitement",
            ]
        ),
    )
    aptt = models.IntegerField("APTT", null=True, blank=True)
    pt = models.IntegerField("PT", null=True, blank=True)
    inr = models.IntegerField("INR", null=True, blank=True)
    hemoglobine = models.IntegerField("Hémoglobine", null=True, blank=True)
    plaquette = models.IntegerField("Plaquettes", null=True, blank=True)
    dfg = models.IntegerField("DFG", null=True, blank=True)
    vol_sang = models.IntegerField(
        "Volume de saignement peropératoire", null=True, blank=True
    )
    coag = models.CharField(
        "Qualité de la coagulation selon le chirurgien",
        max_length=2,
        default="-5",
        choices=to_choice(
            ["-" + str(i) for i in range(6)] + ["+" + str(i) for i in range(5, -1, -1)]
        ),
    )

    # -------------------- HIDDEN -----------------#
    # hidden fields
    incl_num = models.AutoField(primary_key=True)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return str(self.incl_num)

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify("patient") + "-" + str(self.incl_num)
            self.save()

    def get_infos(self):
        infos = {}
        for k, v in self.__dict__.items():
            if k != "_state":
                if v is None:
                    v = ""
                infos[k] = v
        return infos

    def get_age_at_intervention(self):
        return ((self.ddi - self.ddn) / 365).days

    def get_height(self):
        if not self.height:
            return "None"
        hm = int(self.height / 100)
        return "{0}m{1}".format(hm, int(self.height - hm * 100))

    def get_traitement_ids(self, **kwargs):
        ids = []
        for i, data in self.traitements.items():
            # categorie
            b1, b2, b3 = True, True, True
            if "flags" in kwargs:
                if kwargs["flags"] not in data["flags"]:
                    b1 = False
            # pathologie
            if "pathologie" in kwargs:
                if kwargs["pathologie"] != data["pathologie"]:
                    b2 = False
            # traitement
            if "traitement" in kwargs:
                if data["traitement"] not in kwargs["traitement"].split(" | "):
                    b3 = False
            if b1 and b2 and b3:
                ids.append(i)
        return ids

    def get_cure(self, **kwargs):
        for data in self.traitements.values():
            boolean = True
            for k, v in kwargs.items():
                if data.get(k) != v:
                    boolean = False
                    break
            if boolean:
                return True
        return False

    def reset_cure_conclusions(self):
        for k in self.traitements.keys():
            self.traitements[k]["conclusion"] = []
        self.save()
