from django.contrib import admin
from .models import Hewan, Kandang,Pengunjung,Penjaga
# Register your models here.
@admin.register(Hewan)
class HewanAdmin(admin.ModelAdmin):
    list_display=('id','nama','species')
    ordering=('id',)
    search_fields=('nama',)
@admin.register(Kandang)
class KandangAdmin(admin.ModelAdmin):
    list_display=('id','nama')
    ordering=('id',)
    search_fields=('nama',)
@admin.register(Penjaga)
class PenjagaAdmin(admin.ModelAdmin):
    list_display=('id','nama','no_tel')
    ordering=('id',)
    search_fields=('nama',)
@admin.register(Pengunjung)
class PengunjungAdmin(admin.ModelAdmin):
    list_display=('id','nama','no_tel')  
    ordering=('id',)
    search_fields=('nama',)

# admin.site.register(Hewan)
# admin.site.register(Kandang)
# admin.site.register(Pengunjung)
# admin.site.register(Penjaga)
