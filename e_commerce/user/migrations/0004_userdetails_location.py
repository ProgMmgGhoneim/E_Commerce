# Generated by Django 2.0.7 on 2018-07-07 07:46

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180707_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=464646, max_length=63),
            preserve_default=False,
        ),
    ]