# Generated by Django 3.1.3 on 2020-11-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201126_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
