from datetime import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=400)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=False, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class HojaDeVida(models.Model):
    titulo = models.CharField(max_length=255)
    archivo_pdf = models.FileField(upload_to='hojas_de_vida/', default='hoja_de_vida.pdf')
    fecha_subida = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    

