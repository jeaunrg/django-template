help = """
Ce fichier contient toutes les informations sur les traitements,
ainsi que les données utiles pour l'algorithme et pour l'inclusion de patients.


REFS:   Liste des références utilisées dans l'algorithme.
        Les références permettent d'associer chaque conclusion de l'algorithme à un ou plusieurs traitements.
        Exemple:
            'ref_aspirin1' est le mot clé utilisé dans l'algorithme précédé de '%' pour lier une question à cette référence.
            Le label 'Aspirine en prévention primaire' est la phrase affichée devant la conclusion à la fin de l'algo.
            Les autres éléments 'pathologie' et 'traitement' sont les clés permettant de retrouver les traitements déjà inclus et liés à cette référence.

ALGO_CHOICES:       Liste des guidelines possibes.
BLEEDRISK_CHOICES:  Liste des risques d'hémorragie pendant l'opération.
CHIR_CHOICES:       Liste des interventions.
PATH_CHOICES:       Liste des justificatifs de traitement (pathologies).
TRAIT_CHOICES:      Liste des traitements envisageables.
                    A chaque médicament est associé une catégorie.

"""


REFS = {
    "ref_aspirin1": {
        "label": "Aspirine en prévention primaire",
        "pathologie": "Prévention primaire",
        "traitement": "Aspirine, Asaflow, Cardioaspirine",
    },
    "ref_aspirin_mono": {
        "label": "Aspirine en prévention secondaire et monothérapie",
        "pathologie": "Prévention secondaire",
        "traitement": "Aspirine, Asaflow, Cardioaspirine",
    },
    "ref_clopi_mono": {
        "label": "Clopidrogen en prévention secondaire et monothérapie",
        "pathologie": "Prévention secondaire",
        "traitement": "Clopidogrel, PLAVIX",
    },
    "ref_stent_bitherapy": {
        "label": "Bithérapie pour les stents coronaires",
        "pathologie": "Stents Cardiaques",
    },
    "ref_vka": {"label": "VKA", "flags": "AVK"},
    "ref_doac_before": {"label": "DOAC avant l'intervention", "flags": "ACOD"},
    "ref_doac_after": {"label": "DOAC après l'intervention", "flags": "ACOD"},
    "ref_xaban_before": {
        "label": "Rivaroxaban, apixaban et edoxaban, avant l'intervention",
        "flags": "xaban",
    },
    "ref_dabigatran_before": {
        "label": "Dabigatran, avant l'intervention",
        "traitement": "Dabigatran, PRADAXA",
    },
}

ALGO_CHOICES = ["Belge", "Français", "Européen"]
BLEEDRISK_CHOICES = ["faible", "intermédiaire", "élevé"]

CHIR_CHOICES = [
    "Chirurgie Cardiaque",
    "Chirurgie Digestive",
    "Chirurgie Gynecologique",
    "Chirurgie Hepatique",
    "Chirurgie Orthopedique",
    "Chirurgie Ophtalmologique",
    "Chirurgie Plastique",
    "Chirurgie Thoracique",
    "Chirurgie Urologique",
    "Endoscopie",
    "Neurochirurgie",
    "Chirurgie ORL",
    "Radiologie Interventionnelle",
    "Stomatologie",
]

PATH_CHOICES = [
    "Prévention primaire",
    "Prévention secondaire",
    "Fibrilation Atriale",
    "Valvulopathie",
    "Pontages Cardiaques",
    "Chirurgie Vasculaire Arterielle",
    "ATCD EP",
    "ATCD TVP",
    "ATCD AVC + AIT",
    "CMI",
    "Stents Cardiaques",
    "Greffe",
    "Thrombose Porte",
    "Thrombose Mesenterique",
]

TRAIT_CHOICES = {
    "Aspirine, Asaflow, Cardioaspirine": "Antiagregant plaquettaire",
    "Clopidogrel, PLAVIX": "Antiagregant plaquettaire",
    "Prasugrel, EFFIENT": "Antiagregant plaquettaire",
    "Ticlopidine, TICLID": "Antiagregant plaquettaire",
    "Dipyridamole": "Antiagregant plaquettaire",
    "Ticagrelor, BRILIQUE": "Antiagregant plaquettaire",
    "Acénocoumarol, SINTROM": "Anticoagulant-ACOD-AVK-thrombo",
    "Phenprocoumone, MARCOUMAR": "Anticoagulant-ACOD-AVK",
    "Warfarine, MAREVAN": "Anticoagulant-ACOD-AVK",
    "Apixaban, ELIQUIS": "Anticoagulant-ACOD-AOD-thrombo-xaban",
    "Dabigatran, PRADAXA": "Anticoagulant-ACOD-AOD-thrombo",
    "Edoxaban, LIXIANA": "Anticoagulant-ACOD-AOD-xaban",
    "Rivaroxaban, XARELTO": "Anticoagulant-ACOD-AOD-xaban",
    "Fondaparinux, ARIXTRA": "Anticoagulant-ACOD-AOD",
    "Enoxaparine, CLEXANE": "Anticoagulant-Injectable",
    "Nadroparine, FRAXIPARINE, FRAXODI": "Anticoagulant-Injectable",
    "Tinzaparine, INNOHEP": "Anticoagulant-Injectable",
    "HNF, Héparine Sodique": "Anticoagulant-Injectable",
}
