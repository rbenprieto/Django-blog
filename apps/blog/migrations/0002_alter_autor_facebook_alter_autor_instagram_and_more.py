# Generated by Django 4.1.4 on 2022-12-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='instagram'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='twitter'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='web',
            field=models.URLField(blank=True, null=True, verbose_name='web'),
        ),
    ]
