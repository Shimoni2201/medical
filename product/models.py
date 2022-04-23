from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    model_no = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    product_comp_name = models.CharField(max_length=200)
    pic1 = models.ImageField(upload_to='product', default='default.jpg')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product-view")