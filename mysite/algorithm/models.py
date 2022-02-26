import os
from datetime import date

import pandas as pd
from django.db import models

from mysite.settings import MEDIA_ROOT, STATIC_ROOT

from .utils import dfq_to_dict, dftree_to_dict


def upload_questions(instance, filename):
    upload_url = os.path.join("algorithm", str(instance.name), "questions.xlsx")
    if os.path.isfile(os.path.join(MEDIA_ROOT, "users", upload_url)):
        os.remove(os.path.join(MEDIA_ROOT, "users", upload_url))
    return upload_url


def upload_layout(instance, filename):
    upload_url = os.path.join("algorithm", str(instance.name), "layout.xlsx")
    if os.path.isfile(os.path.join(MEDIA_ROOT, "users", upload_url)):
        os.remove(os.path.join(MEDIA_ROOT, "users", upload_url))
    return upload_url


class Algorithm(models.Model):
    name = models.CharField("Nom de l'algorithme", max_length=20, primary_key=True)
    layout = models.FileField(
        upload_to=upload_layout,
        default=os.path.join(MEDIA_ROOT, "default", "algorithm", "layout.xlsx"),
    )
    questions = models.FileField(
        upload_to=upload_questions,
        default=os.path.join(MEDIA_ROOT, "default", "algorithm", "questions.xlsx"),
    )
    last_updated = models.DateTimeField(auto_now=True)

    def build(self):
        if "_algo" not in self.__dict__:
            df = pd.read_excel(self.layout, header=None)
            self._algo = dftree_to_dict(df)
            df = pd.read_excel(self.questions, index_col=0)
            self._questions = dfq_to_dict(df)
        return {"algo": self._algo, "questions": self._questions}
