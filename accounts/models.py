from django.db import models

# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name