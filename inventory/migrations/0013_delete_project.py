# Generated by Django 3.2.5 on 2021-07-04 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_remove_part_part_of_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]