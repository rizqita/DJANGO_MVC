from django.contrib import admin
from .models import Direksi,Mentee,Mentor,MataPelajaran,LiveCode,Challenge
# Register your models here.
@admin.register(Direksi)
class DireksiAdmin(admin.ModelAdmin):
    list_display=('id','nama','no_telp','jabatan')
    ordering = ('id',)
    search_fields = ('nama',)
@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display=('id','nama')
    ordering = ('id',)
    search_fields = ('nama',)
@admin.register(MataPelajaran)
class MataPelajaranAdmin(admin.ModelAdmin):
    list_display=('id','nama_pelajaran')
    ordering = ('id',)
    search_fields = ('nama_pelajaran',)
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display=('id','nama','alamat','no_telp')
    ordering = ('id',)
    search_fields = ('nama',)
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display=('id','nama_challenge')
    ordering = ('id',)
    search_fields = ('nanama_challenge',)
@admin.register(LiveCode)
class LiveCodeAdmin(admin.ModelAdmin):
    list_display=('id','nama_live_code')
    ordering = ('id',)
    search_fields = ('nama_live_code',)

# admin.site.register(Direksi)
# admin.site.register(Mentee)
# admin.site.register(Mentor)
# admin.site.register(MataPelajaran)
# admin.site.register(LiveCode)
# admin.site.register(Challenge)
