from django.contrib import admin
from .models import Hewan, Kandang,Pengunjung,Penjaga
# Register your models here.

admin.site.register(Hewan)
admin.site.register(Kandang)
admin.site.register(Pengunjung)
admin.site.register(Penjaga)
