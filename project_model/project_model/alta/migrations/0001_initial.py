# Generated by Django 2.2.3 on 2019-07-22 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('no_telp', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('no_telp', models.CharField(max_length=16)),
                ('mentor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alta.Mentor')),
            ],
        ),
    ]
