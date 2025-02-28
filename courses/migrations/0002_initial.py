# Generated by Django 5.1 on 2024-08-27 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='comments',
            field=models.ManyToManyField(to='courses.comment'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_section',
            field=models.ManyToManyField(to='courses.coursesection'),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='episode',
            field=models.ManyToManyField(to='courses.episode'),
        ),
        migrations.AddField(
            model_name='sector',
            name='related_course',
            field=models.ManyToManyField(to='courses.course'),
        ),
    ]
