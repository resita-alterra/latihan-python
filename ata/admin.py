from django.contrib import admin
from .models import Mentor, Mentee, Blog

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'exp', 'quote','nama_file_image']
    ordering = ['id']

class MenteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'quote', 'nama_file_image']
    ordering = ['id']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tanggal_dipost', 'komen', 'nama_file_image']

admin.site.register(Mentor, MentorAdmin)
admin.site.register(Mentee, MenteeAdmin)
admin.site.register(Blog, BlogAdmin)

# Register your models here.
