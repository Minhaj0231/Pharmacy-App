# Generated by Django 2.1 on 2019-07-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_drugs', '0003_auto_20190716_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='drug_type',
            field=models.CharField(default='no_type', max_length=20),
        ),
    ]
