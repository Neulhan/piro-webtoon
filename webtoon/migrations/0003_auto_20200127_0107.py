# Generated by Django 3.0.2 on 2020-01-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0002_auto_20200127_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtoon',
            name='list_url',
            field=models.URLField(),
        ),
    ]