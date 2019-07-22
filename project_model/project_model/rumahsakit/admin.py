from django.contrib import admin
from .models import Dokter, Obat, Pasien, Resep
# Register your models here.

admin.site.register(Dokter)
admin.site.register(Obat)
admin.site.register(Pasien)
admin.site.register(Resep)