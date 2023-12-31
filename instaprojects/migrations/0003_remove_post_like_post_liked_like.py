# Generated by Django 4.2.5 on 2023-10-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaprojects', '0002_post_video_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaprojects.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
