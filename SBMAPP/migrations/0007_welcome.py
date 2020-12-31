# Generated by Django 3.0.2 on 2020-12-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBMAPP', '0006_auto_20210101_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('featured', models.BooleanField()),
            ],
        ),
    ]