# Generated by Django 4.2.5 on 2023-10-09 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaprojects', '0005_remove_post_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
