from django.contrib import admin
from .models import Dokter, Obat, Pasien, Resep
# Register your models here.
@admin.register(Dokter)
class DokterAdmin(admin.ModelAdmin):
    list_display = ('id','nama','no_tel','bidang')
    ordering = ('id',)
    search_fields = ('name',)
@admin.register(Pasien)
class PasienAdmin(admin.ModelAdmin):
    list_display = ('id','nama','no_tel','alamat','keluhan')
    ordering = ('id',)
    search_fields = ('name',)    
@admin.register(Obat)
class ObatAdmin(admin.ModelAdmin):
    list_display = ('id','nama','khasiat')
    ordering = ('id',)
    search_fields = ('nama',)
@admin.register(Resep)
class ResepAdmin(admin.ModelAdmin):
    list_display = ('id','nama','total_harga','kumpulan_obat')
    ordering = ('id',)
    search_fields = ('nama',)
# admin.site.register(Dokter)
# admin.site.register(Obat)
# admin.site.register(Pasien)
# admin.site.register(Resep)