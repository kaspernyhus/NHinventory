# Generated by Django 3.2.8 on 2021-10-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOMmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectbom',
            name='pcb_ref',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]