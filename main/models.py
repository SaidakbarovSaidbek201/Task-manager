from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 256)
    year = models.DateField(auto_now_add = True)
    pages = models.IntegerField()
    mualif = models.CharField(max_length=255, default='Unknown Author')
    janri = models.CharField(max_length= 256)
    image = models.ImageField(upload_to="photos/")
    info = models.TextField()
    
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.name

    

class Vazifa(models.Model):
    sarlavha = models.CharField(max_length=200)
    tavsif = models.TextField()
    oxirgi_muddat = models.DateField()


    def __str__(self):
        return self.sarlavha
    
    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"

