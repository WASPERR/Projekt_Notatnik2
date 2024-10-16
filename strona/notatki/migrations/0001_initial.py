# Generated by Django 5.1.2 on 2024-10-13 16:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('roboczy', 'Roboczy'), ('opublikowany', 'Opublikowany')], default='roboczy', max_length=12)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notatki_notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='notatki_not_publish_8323fb_idx')],
            },
        ),
    ]
