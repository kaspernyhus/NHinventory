# Generated by Django 3.2.5 on 2021-07-02 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20210702_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='subtypes',
            new_name='subtype',
        ),
    ]
