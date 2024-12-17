from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Flower(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
