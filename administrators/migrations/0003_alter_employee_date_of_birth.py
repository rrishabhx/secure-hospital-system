# Generated by Django 4.0.1 on 2022-02-26 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]