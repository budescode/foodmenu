# Generated by Django 2.0.3 on 2020-12-16 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20201216_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='email',
        ),
    ]
