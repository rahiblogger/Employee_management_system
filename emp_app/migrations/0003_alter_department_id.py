# Generated by Django 4.1.2 on 2023-01-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
