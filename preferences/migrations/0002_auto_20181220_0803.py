# Generated by Django 2.0 on 2018-12-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='sites',
            field=models.ManyToManyField(blank=True, to='sites.Site'),
        ),
    ]
