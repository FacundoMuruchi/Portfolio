# Generated by Django 4.2.6 on 2024-05-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='com',
            name='link',
        ),
        migrations.AddField(
            model_name='com',
            name='preview',
            field=models.FileField(blank=True, null=True, upload_to='previews/'),
        ),
    ]
