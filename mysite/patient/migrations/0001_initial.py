# Generated by Django 4.0.1 on 2022-02-09 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('firstname', models.CharField(default='', max_length=200, verbose_name='prénom')),
                ('lastname', models.CharField(default='', max_length=200, verbose_name='nom')),
                ('height', models.IntegerField(verbose_name='taille')),
                ('weight', models.IntegerField(verbose_name='poids')),
                ('ddn', models.DateField(verbose_name='Date de naissance')),
                ('ddi', models.DateField(blank=True, null=True, verbose_name="Date de l'intervention")),
                ('intervention', models.CharField(blank=True, default='', max_length=200, verbose_name='intervention')),
                ('chirurgien', models.CharField(blank=True, default='', max_length=200, verbose_name='chirurgien')),
                ('chirurgie', models.CharField(blank=True, choices=[('', ''), ('Chirurgie Cardiaque', 'Chirurgie Cardiaque'), ('Chirurgie Digestive', 'Chirurgie Digestive'), ('Chirurgie Gynecologique', 'Chirurgie Gynecologique'), ('Chirurgie Hepatique', 'Chirurgie Hepatique'), ('Chirurgie Orthopedique', 'Chirurgie Orthopedique'), ('Chirurgie Ophtalmologique', 'Chirurgie Ophtalmologique'), ('Chirurgie Plastique', 'Chirurgie Plastique'), ('Chirurgie Thoracique', 'Chirurgie Thoracique'), ('Chirurgie Urologique', 'Chirurgie Urologique'), ('Endoscopie', 'Endoscopie'), ('Neurochirurgie', 'Neurochirurgie'), ('Chirurgie ORL', 'Chirurgie ORL'), ('Radiologie Interventionnelle', 'Radiologie Interventionnelle'), ('Stomatologie', 'Stomatologie')], max_length=40, verbose_name="Discipline de l'intervention")),
                ('bleeding_risk', models.CharField(blank=True, choices=[('', ''), ('faible', 'faible'), ('intermédiaire', 'intermédiaire'), ('élevé', 'élevé')], max_length=100, verbose_name='Risque hémorragique de la chirurgie')),
                ('ddconsult', models.DateField(auto_now_add=True, verbose_name='Date de la consultation')),
                ('traitements', models.JSONField(blank=True, default=dict)),
                ('algo', models.CharField(blank=True, choices=[('', ''), ('Belge', 'Belge'), ('Français', 'Français'), ('Européen', 'Européen')], max_length=40, verbose_name='Algorithme suivi')),
                ('algo_complete_results', models.JSONField(default=dict)),
                ('schema_therap', models.CharField(choices=[('', ''), ('Date exacte', 'Date exacte'), ("Terminologie 'dernière prise à J-xx'", "Terminologie 'dernière prise à J-xx'"), ("Pas d'arrêt du traitement", "Pas d'arrêt du traitement")], default='Date exacte', max_length=40, verbose_name='Schéma thérapeutique donné au patient')),
                ('aptt', models.IntegerField(blank=True, null=True, verbose_name='APTT')),
                ('pt', models.IntegerField(blank=True, null=True, verbose_name='PT')),
                ('inr', models.IntegerField(blank=True, null=True, verbose_name='INR')),
                ('hemoglobine', models.IntegerField(blank=True, null=True, verbose_name='Hémoglobine')),
                ('plaquette', models.IntegerField(blank=True, null=True, verbose_name='Plaquettes')),
                ('dfg', models.IntegerField(blank=True, null=True, verbose_name='DFG')),
                ('vol_sang', models.IntegerField(blank=True, null=True, verbose_name='Volume de saignement peropératoire')),
                ('coag', models.CharField(choices=[('', ''), ('-0', '-0'), ('-1', '-1'), ('-2', '-2'), ('-3', '-3'), ('-4', '-4'), ('-5', '-5'), ('+5', '+5'), ('+4', '+4'), ('+3', '+3'), ('+2', '+2'), ('+1', '+1'), ('+0', '+0')], default='-5', max_length=2, verbose_name='Qualité de la coagulation selon le chirurgien')),
                ('incl_num', models.AutoField(primary_key=True, serialize=False)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
