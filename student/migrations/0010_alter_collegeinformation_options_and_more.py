# Generated by Django 4.0.5 on 2022-07-26 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_familyinformation_educationinformation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collegeinformation',
            options={'ordering': ('symbol_number',), 'verbose_name': 'CollegeInformation', 'verbose_name_plural': 'CollegeInformations'},
        ),
        migrations.AlterModelOptions(
            name='familyinformation',
            options={'verbose_name': 'FamilyInformation', 'verbose_name_plural': 'FamilyInformations'},
        ),
        migrations.DeleteModel(
            name='EducationInformation',
        ),
    ]
