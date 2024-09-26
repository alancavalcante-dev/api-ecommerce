from django.db import models
from django.contrib.auth.models import User
from products.models import Product

STARS = (
    ('1', '1 - STAR'),
    ('2', '2 - STARS'),
    ('3', '3 - STARS'),
    ('4', '4 - STARS'),
    ('5', '5 - STARS'),
)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='filhos')
    rate = models.CharField(max_length=10, default='5',choices=STARS)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name