# Generated by Django 4.2.3 on 2023-07-13 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0003_snippet_rename_passaport_kimlik_pasaport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
