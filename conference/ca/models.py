from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import datetime
import random




class Cathegorie(models.Model):
    montant=models.IntegerField(null=True)
    
    def __str__(self):
        return f"{ self.montant }"
    
    
class Mensualite(models.Model):
    mois=models.CharField(max_length=25)
    
    def __str__(self):
        return f"{ self.mois }"
    
    
class Donateur(models.Model):
    code = models.CharField(max_length=10,unique=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    profession=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    eglise=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def save(self, **kwargs):
        self.code = random.randrange(0,9999999, 1000)
        return super(Donateur, self).save(**kwargs)
    
    def __str__(self):
        return f"{ self.nom } {self.prenom}"
    
    def get_absolute_url(self):
        return reverse('donateur-detail', kwargs={'pk': self.pk})
    
    
class Promesse_dons(models.Model):
    donateur=models.ForeignKey(Donateur, on_delete=models.CASCADE, related_name="donateur",null=True)
    cathegorie=models.IntegerField(null=True, blank=True)
    autre_montant=models.IntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{ self.donateur } {self.cathegorie}"
    
    
class Dons(models.Model):
    donateur=models.ForeignKey(Donateur,on_delete=models.CASCADE, related_name="donateur_list")
    montant=models.IntegerField(null=True)
    periode=models.ForeignKey(Mensualite,on_delete=models.CASCADE, related_name="periode_list")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{ self.donateur } payé {self.montant}"
    
    