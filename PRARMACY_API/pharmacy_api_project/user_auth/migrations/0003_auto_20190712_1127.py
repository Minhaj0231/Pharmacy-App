# Generated by Django 2.1 on 2019-07-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_auto_20190712_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_mobile_no', models.CharField(max_length=30)),
                ('customer_email', models.CharField(max_length=30)),
                ('customer_address', models.CharField(max_length=30)),
                ('customer_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='customeuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customeuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomeUser',
        ),
    ]
