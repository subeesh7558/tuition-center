# Generated by Django 4.0.1 on 2022-03-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_batch_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
