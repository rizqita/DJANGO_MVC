from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama=models.CharField(max_length=255)
    no_telp=models.CharField(max_length=16)
    jabatan=models.CharField(max_length=100)
    def __str__(self):
        return self.nama
class Mentee(models.Model):
    nama=models.CharField(max_length=255)
    def __str__(self):
        return self.nama
class MataPelajaran(models.Model):
    nama_pelajaran=models.CharField(max_length=255)
    jadwal_dimulai=models.DateField()
    jadwal_berakhir=models.DateTimeField()
    def __str__(self):
        return self.nama_pelajaran  
class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    no_telp = models.CharField(max_length=16)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama

class Challenge(models.Model):
    nama_challenge=models.CharField(max_length=255)
    banyak_soal=models.PositiveIntegerField()
    bobot_nilai=models.PositiveIntegerField()
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_challenge
class LiveCode(models.Model):
    nama_live_code=models.CharField(max_length=200)
    banyak_soal=models.PositiveIntegerField()
    bobot_nilai=models.PositiveIntegerField()
    tanggal_pelaksanaan=models.DateTimeField()
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_live_code
    