# Generated by Django 4.0.1 on 2022-03-31 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_subject_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.batch'),
        ),
    ]
