from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator



 


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enterprise_name = models.CharField(max_length=100)
    name_fantasy = models.CharField(max_length=100)
    email = models.EmailField()
    cnpj = models.CharField(max_length=14, validators=(MinLengthValidator(14),))
    address = models.CharField(max_length=200)
    address_number = models.IntegerField()

    def __str__(self):
        return self.enterprise_name
    

                