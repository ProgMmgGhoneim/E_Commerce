# Generated by Django 2.0.7 on 2018-07-07 07:51

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180707_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
