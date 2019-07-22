from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    no_tel = models.CharField(max_length=16)
    bidang = models.CharField(max_length=255)
    jadwal_praktek = models.DateField()
    def __str__(self):
        return self.nama
    
class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    no_tel = models.CharField(max_length=16)
    alamat = models.TextField()
    keluhan  = models.TextField()
    def __str__(self):
        return self.nama
class Obat(models.Model):
    nama = models.CharField(max_length=255)
    khasiat = models.TextField()
    def __str__(self):
        return self.nama
class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.IntegerField() 
    kumpulan_obat = models.TextField()
    def __str__(self):
        return self.nama
