from django.db import models
#from django.contrib.auth.models import AbstractUser



# class UserRegistration(AbstractUser):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.username



class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField() # null=True, default=True
    
    def __str__(self):
        return self.title
    

