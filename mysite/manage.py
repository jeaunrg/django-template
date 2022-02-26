#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import glob
import os
import shutil
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def clear():
    dirname = os.path.dirname(__file__)
    manage_pyfile = os.path.join(dirname, "manage.py")

    print("delete migrations...")
    for migration_file in glob.glob(os.path.join(dirname, "*", "migrations", "*.py")):
        if not migration_file.endswith("__init__.py"):
            os.remove(migration_file)
            print("delete", migration_file)

    print("delete database...")
    db_path = os.path.join(dirname, "db.sqlite3")
    if os.path.isfile(db_path):
        os.remove(db_path)

    print("delete media but not default")
    media_path = os.path.join(dirname, "media_cdn", "users")
    shutil.rmtree(media_path)
    os.mkdir(media_path)


def init():
    dirname = os.path.dirname(__file__)
    manage_pyfile = os.path.join(dirname, "manage.py")

    print("Making migrations...")
    os.system(f"python {manage_pyfile} makemigrations")

    print("Migrating...")
    os.system(f"python {manage_pyfile} migrate")

    print("Creating superuser...")
    os.environ["DJANGO_SUPERUSER_PASSWORD"] = "admin"
    os.system(
        f"python {manage_pyfile} createsuperuser --noinput --username admin --email admin@gmail.com"
    )


if __name__ == "__main__":
    if "--reset" in sys.argv:
        clear()
        init()
        sys.argv.remove("--reset")
    main()
