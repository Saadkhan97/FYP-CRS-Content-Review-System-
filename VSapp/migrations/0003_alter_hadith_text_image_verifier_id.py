# Generated by Django 3.2 on 2023-01-25 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VSapp', '0002_hadith_text_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hadith_text_image',
            name='verifier_id',
            field=models.ForeignKey(limit_choices_to={'Verifier': True}, on_delete=django.db.models.deletion.CASCADE, to='VSapp.userinformation'),
        ),
    ]