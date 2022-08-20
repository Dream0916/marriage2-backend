# Generated by Django 3.2.15 on 2022-08-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_person_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
