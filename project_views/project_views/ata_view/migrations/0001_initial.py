# Generated by Django 2.2.3 on 2019-07-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('jabatan', models.CharField(max_length=255)),
                ('durasi', models.IntegerField()),
                ('quote', models.TextField()),
            ],
        ),
    ]