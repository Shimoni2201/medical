from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from product.models import product
# Create your models here.
class prodinward(models.Model):
    prod = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Value should not be less than 0')])
    rate = models.FloatField(max_length=100,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    price = models.FloatField(max_length=100,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    discount = models.FloatField(default=0,max_length=100, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    gst = models.FloatField(default=0,max_length=100, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    sgst = models.FloatField(default=0, max_length=100, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    is_billed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.price}"


    def get_absolute_url(self):
        return reverse("closed")