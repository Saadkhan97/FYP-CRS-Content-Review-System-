# Generated by Django 3.2 on 2023-08-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VSapp', '0020_auto_20230803_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hadith_text_image',
            name='book_id',
            field=models.IntegerField(default=0),
        ),
    ]