# Generated by Django 5.0.4 on 2025-01-10 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SundaySchoolLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('memory_verse', models.TextField()),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='lesson_banners/')),
            ],
        ),
        migrations.CreateModel(
            name='ReflectionQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='sermon.sundayschoollesson')),
            ],
        ),
        migrations.CreateModel(
            name='LessonSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='sermon.sundayschoollesson')),
            ],
        ),
        migrations.CreateModel(
            name='FurtherReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='further_readings', to='sermon.sundayschoollesson')),
            ],
        ),
    ]
