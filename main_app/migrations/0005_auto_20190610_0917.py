# Generated by Django 2.2.1 on 2019-06-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_covergamemodel_gamemodel_genregamemodel_genremodel_imagemodel_platformgamemodel_platformmodel_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='aggregated_rating',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='aggregated_rating_count',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='first_release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='rating',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='rating_count',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='summary',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='version_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]