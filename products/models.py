from django.db import models
from sellers.models import Seller
from genres.models import Genre



class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genre, on_delete=models.PROTECT)
    release_date = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    freight = models.DecimalField(max_digits=10, decimal_places=2, default=7.50)
    image = models.ImageField(upload_to='products/images/')
    resume = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name