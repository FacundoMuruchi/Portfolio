# Generated by Django 4.2.6 on 2024-07-16 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_com_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='com',
            name='version',
            field=models.IntegerField(blank=True, choices=[(1, 'Original'), (2, 'Remake'), (3, 'Alternative Version')], null=True),
        ),
    ]
