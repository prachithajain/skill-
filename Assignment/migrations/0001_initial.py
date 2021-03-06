# Generated by Django 2.1.5 on 2019-02-23 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=100)),
                ('assignmentName', models.CharField(max_length=100)),
                ('assignmentDescription', models.CharField(blank=True, max_length=2000)),
                ('assignmentFormat', models.CharField(blank=True, max_length=2000)),
                ('assignmentDate', models.CharField(max_length=2000)),
                ('assignedBy', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mysubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileUpload', models.FileField(upload_to='')),
                ('usn', models.CharField(max_length=100)),
                ('uploadTime', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('assignmentName', models.CharField(max_length=100)),
            ],
        ),
    ]
