# Generated by Django 3.2 on 2023-05-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VSapp', '0010_auto_20230126_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hadith_text_image',
            name='analyst_id',
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Verifier', 'Verifier')], default='USER', max_length=20),
        ),
    ]
