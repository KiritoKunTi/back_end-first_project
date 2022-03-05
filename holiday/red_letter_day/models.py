from django.db import models

# Create your models here.
class State(models.Model):
    title = models.CharField("Мейрам атауы", max_length=70)
    on_date = models.CharField("Күн-айы", max_length=50)
    anons = models.TextField("Мейрам жайлы")
    
    def __str__(self):
        return self.title
    
    
class National(models.Model):
    title = models.CharField("Мейрам атауы", max_length=70)
    on_date = models.CharField("Күн-айы", max_length=50)
    anons = models.TextField("Мейрам жайлы")
    
    def __str__(self):
        return self.title
    
    
    
class Professional(models.Model):
    title = models.CharField("Мейрам атауы", max_length=70)
    on_date = models.CharField("Күн-айы", max_length=50)
    anons = models.TextField("Мейрам жайлы")
    
    def __str__(self):
        return self.title