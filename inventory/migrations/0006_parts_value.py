# Generated by Django 3.2.5 on 2021-07-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20210702_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
