# Generated by Django 2.2.1 on 2019-06-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20190610_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='summary',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
