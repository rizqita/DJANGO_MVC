# Generated by Django 2.2.3 on 2019-07-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('berat', models.IntegerField(max_length=4)),
                ('umur', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('isi_kandang', models.TextField()),
                ('luas_kandang', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('no_tel', models.CharField(max_length=17)),
                ('jadwal_berkunjung', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('no_tel', models.CharField(max_length=17)),
                ('jadwal_jaga', models.DateField()),
            ],
        ),
    ]
