# Generated by Django 4.0.1 on 2022-03-31 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0006_user_registration_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='sclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sclass', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user_registration',
            name='sclass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.sclass'),
        ),
    ]
