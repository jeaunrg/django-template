# django-template
A dynamic django website template that you can pull and start from (frontend & backend)

## Contents

- Account management (create, modify, delete, authorization, groups)
- Post management and public posts feed (create, modify posts)
- PDF creation with html template
- Data download
- Widgets (lookup tables, forms, embedding, collapsable menu for mobile, profile dropdown, sidebar, image cropping, light/dark mode button)
- Animation (light/dark button, sidebar, profile photo)
- Design

<p align="center">
  <img src="https://github.com/jeaunrg/django-template/blob/main/django-template.gif?raw=true">
</p>

## How to use

Clone this repository

```bash
git clone git@github.com:jeaunrg/django-template.git
```

Install python requirements

```bash
pip install -r ./requirements.txt
```

Launch the server

```bash
python ./mysite/manage.py runserver
```
if you want to reset presets before launching the server, use this command:
```bash
python ./mysite/manage.py runserver --reset
```

Access the application on chrome browser
http://localhost:8000/


Default administration login
- username: admin
- password: admin


## Requirements

- Python 3.9.9
- Django 4.0.1
