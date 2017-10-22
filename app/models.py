from django.db import models

class Entrée(models.Model):
    principal = models.CharField(max_length=100)
    accompagnement = models.CharField(max_length=100)
    def __str__(self):
        return self.principal

class Plat(models.Model):
    principal = models.CharField(max_length=100)
    accompagnement = models.CharField(max_length=100)
    def __str__(self):
        return self.principal

class Dessert(models.Model):
    principal = models.CharField(max_length=100)
    accompagnement = models.CharField(max_length=100)
    def __str__(self):
        return self.principal
