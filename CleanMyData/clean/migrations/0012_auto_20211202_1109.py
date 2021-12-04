# Generated by Django 3.2.9 on 2021-12-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0011_auto_20211130_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerpreference',
            name='null_choice_date',
            field=models.CharField(choices=[('nothing', 'Nothing'), ('remove-tuples', 'Remove tuples'), ('Replace', (('Now', 'Current date'), ('Cus', 'Custom date')))], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headerpreference',
            name='null_choice_num',
            field=models.CharField(choices=[('nothing', 'Nothing'), ('remove-tuples', 'Remove tuples'), ('Replace', (('Avg', 'Average'), ('Med', 'Median'), ('Min', 'Minimum'), ('Max', 'Maximum'), ('Cus', 'Custom value')))], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headerpreference',
            name='null_choice_string',
            field=models.CharField(choices=[('nothing', 'Nothing'), ('remove-tuples', 'Remove tuples'), ('Replace', (('Cus', 'Custom string'),))], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='headerpreference',
            name='current_type',
            field=models.CharField(choices=[('non', 'None'), ('Temperature', (('C', 'Celsius'), ('F', 'Fahrenheit'), ('K', 'Kelvin'))), ('Distance', (('KM', 'Kilometer'), ('MI', 'Mile'))), ('Weight', (('KG', 'Kilogram'), ('LB', 'Pound')))], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='headerpreference',
            name='desired_type',
            field=models.CharField(choices=[('non', 'None'), ('Temperature', (('C', 'Celsius'), ('F', 'Fahrenheit'), ('K', 'Kelvin'))), ('Distance', (('KM', 'Kilometer'), ('MI', 'Mile'))), ('Weight', (('KG', 'Kilogram'), ('LB', 'Pound')))], default='NON', max_length=3),
        ),
    ]