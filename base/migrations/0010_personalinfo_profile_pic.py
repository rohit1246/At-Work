# Generated by Django 4.1.2 on 2022-11-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_personalinfo_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='profile_pic',
            field=models.ImageField(default='man.png', null=True, upload_to=''),
        ),
    ]
