from django.db import models


# Create your models here.
class Foto(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    gambar = models.ImageField(upload_to='static/galeri/')
    tanggal_unggah = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = "Foto"
