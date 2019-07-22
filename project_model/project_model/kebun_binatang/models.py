from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama=models.CharField(max_length=255)
    species=models.CharField(max_length=255)
    berat=models.IntegerField()
    umur=models.IntegerField()
class Kandang(models.Model):
    nama=models.CharField(max_length=255)
    isi_kandang=models.TextField()
    luas_kandang=models.IntegerField()
class Penjaga(models.Model):
    nama=models.CharField(max_length=255)
    no_tel=models.CharField(max_length=17)
    jadwal_jaga = models.DateField()
class Pengunjung(models.Model):
    nama=models.CharField(max_length=255)
    no_tel=models.CharField(max_length=17)
    jadwal_berkunjung = models.DateTimeField()
