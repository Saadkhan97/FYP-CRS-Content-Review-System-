# Generated by Django 3.2 on 2023-01-25 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VSapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hadith_Text_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hadith_text', models.CharField(max_length=500, null=True)),
                ('verifier_date', models.DateField()),
                ('analyzed_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Analyzed', 'Analyzed'), ('Verified', 'Verified')], default='Pending', max_length=20)),
                ('verifier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VSapp.userinformation')),
            ],
        ),
    ]