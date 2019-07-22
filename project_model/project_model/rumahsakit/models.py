from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    no_tel = models.CharField(max_length=16)
    bidang = models.CharField(max_length=255)
    jadwal_praktek = models.DateField()
class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    no_tel = models.CharField(max_length=16)
    alamat = models.TextField()
    keluhan  = models.TextField()
class Obat(models.Model):
    nama = models.CharField(max_length=255)
    khasiat = models.TextField()
class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.IntegerField() 
    kumpulan_obat = models.TextField()
