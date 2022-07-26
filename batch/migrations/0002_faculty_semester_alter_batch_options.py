# Generated by Django 4.0.5 on 2022-07-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name': 'Batch_name', 'verbose_name_plural': 'Batch_names'},
        ),
    ]
