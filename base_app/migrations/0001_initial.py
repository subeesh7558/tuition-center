# Generated by Django 4.0.1 on 2022-03-22 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('fathername', models.CharField(max_length=240, null=True)),
                ('mothername', models.CharField(max_length=240, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=240, null=True)),
                ('presentaddress1', models.CharField(max_length=240, null=True)),
                ('presentaddress2', models.CharField(max_length=240, null=True)),
                ('presentaddress3', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('district', models.CharField(max_length=240, null=True)),
                ('state', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('permanentaddress1', models.CharField(max_length=240, null=True)),
                ('permanentaddress2', models.CharField(max_length=240, null=True)),
                ('permanentaddress3', models.CharField(max_length=240, null=True)),
                ('permanentpincode', models.CharField(max_length=240, null=True)),
                ('permanentdistrict', models.CharField(max_length=240, null=True)),
                ('permanentstate', models.CharField(max_length=240, null=True)),
                ('permanentcountry', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('alternativeno', models.CharField(max_length=240, null=True)),
                ('employee_id', models.CharField(default='', max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
                ('idproof', models.FileField(blank=True, null=True, upload_to='images/')),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('attitude', models.IntegerField(default='0')),
                ('creativity', models.IntegerField(default='0')),
                ('workperformance', models.IntegerField(default='0')),
                ('joiningdate', models.DateField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='', max_length=240, null=True)),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base_app.designation')),
            ],
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField()),
                ('leave_status', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('leaveapprovedstatus', models.CharField(max_length=200)),
                ('leave_rejected_reason', models.CharField(max_length=300)),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base_app.designation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base_app.user_registration')),
            ],
        ),
    ]