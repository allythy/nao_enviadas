# Generated by Django 3.1.7 on 2021-05-17 01:45

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_letter_letter_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='color',
            field=colorfield.fields.ColorField(default='#FFF', max_length=18),
        ),
    ]