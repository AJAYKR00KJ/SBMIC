# Generated by Django 3.1.5 on 2021-01-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBMAPP', '0009_youtube_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('date', models.DateTimeField()),
                ('featured', models.BooleanField()),
                ('link_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('date', models.DateTimeField()),
                ('featured', models.BooleanField()),
                ('link_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('date', models.DateTimeField()),
                ('featured', models.BooleanField()),
                ('link_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('date', models.DateTimeField()),
                ('featured', models.BooleanField()),
                ('link_url', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='youtube',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]
