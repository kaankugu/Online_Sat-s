# Generated by Django 4.2.3 on 2023-07-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kimlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('passaport', models.CharField(max_length=20)),
            ],
        ),
    ]
