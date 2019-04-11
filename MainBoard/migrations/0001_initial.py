# Generated by Django 2.1.8 on 2019-04-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicName', models.CharField(max_length=500)),
                ('topicDescription', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapanyName', models.CharField(max_length=500)),
                ('companyExperience', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='popularCodingProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicHeading', models.CharField(max_length=500)),
                ('topicDescription', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=500)),
                ('topicHeading', models.CharField(max_length=500)),
                ('topicDescription', models.CharField(max_length=5000)),
            ],
        ),
    ]
