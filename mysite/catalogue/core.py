import zipfile
from mysite.settings import MEDIA_ROOT
import os
import pandas as pd
from datetime import datetime
import django_filters
from .models import Document
from django.db import models


def extract_catalogue(zip_folder):

    media_tmp = os.path.join(MEDIA_ROOT, 'unzipped', str(datetime.now().strftime("%Y%m%d_%H%M%S")))

    with zipfile.ZipFile(zip_folder, 'r') as zip_ref:
        zip_ref.extractall(media_tmp)

    folder_tmp = os.path.join(media_tmp, os.path.splitext(str(zip_folder))[0])
    data = pd.read_excel(os.path.join(folder_tmp, 'data.xlsx')).astype(str)
    data = data.set_index('image')
    data = data.to_dict(orient='index')
    for file in data.keys():
        file_path = os.path.join(folder_tmp, file)
        if os.path.isfile(file_path):
            result = data.get(file)
            result['image'] = os.path.join(folder_tmp, file)
            yield result
