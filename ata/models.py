from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    quote = models.TextField()
    nama_file_image = models.CharField(max_length=255, default='profpic')

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    quote = models.TextField()
    nama_file_image = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    tanggal_dipost = models.DateField()
    komen = models.IntegerField()
    isi = models.TextField()
    nama_file_image = models.CharField(max_length=255)

