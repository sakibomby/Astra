# Generated by Django 5.0.6 on 2024-06-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_package_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
        migrations.AlterField(
            model_name='package',
            name='destination',
            field=models.CharField(choices=[('Mo', 'Moon'), ('Ma', 'Mars'), ('Pl', 'Pluto'), ('Is', 'International Space Station'), ('Ne', 'Neptune')], default=0, max_length=2),
        ),
    ]
