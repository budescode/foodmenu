# Generated by Django 3.0.6 on 2020-12-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_ordermodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='table',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
