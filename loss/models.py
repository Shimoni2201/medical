from django.core.validators import MinValueValidator
from django.db import models
from product.models import product
from datetime import datetime
from django.urls import reverse
# Create your models here.
class loss(models.Model):
    date = models.DateField(default=datetime.utcnow)
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="loss")
    price = models.IntegerField(validators=[MinValueValidator(0, 'Value should not be less than 0')])
    rate = models.IntegerField(validators=[MinValueValidator(0, 'Value should not be less than 0')])
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Value should not be less than 0')])
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.product}"

    def get_absolute_url(self):
        return reverse("loss-view")