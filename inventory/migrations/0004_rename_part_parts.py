# Generated by Django 3.2.5 on 2021-07-02 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210702_2039'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Part',
            new_name='Parts',
        ),
    ]