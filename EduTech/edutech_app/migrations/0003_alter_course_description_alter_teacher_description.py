# Generated by Django 4.0 on 2022-04-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edutech_app', '0002_classnumber_subject_teacher_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Description',
            field=models.TextField(max_length=800),
        ),
    ]