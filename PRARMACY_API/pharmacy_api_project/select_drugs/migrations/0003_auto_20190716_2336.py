# Generated by Django 2.1 on 2019-07-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_drugs', '0002_auto_20190716_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='drug_name',
            field=models.CharField(default='no_name', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='drugs',
            name='drug_type',
            field=models.CharField(default='no_type2', max_length=20),
        ),
    ]
