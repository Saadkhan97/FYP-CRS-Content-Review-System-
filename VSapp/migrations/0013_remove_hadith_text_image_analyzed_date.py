# Generated by Django 3.2 on 2023-05-11 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VSapp', '0012_remove_hadith_text_image_analyzation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hadith_text_image',
            name='analyzed_date',
        ),
    ]
