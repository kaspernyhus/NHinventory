# Generated by Django 3.2.5 on 2021-07-04 13:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0011_part_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.part')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BOMmanager.project')),
            ],
        ),
    ]