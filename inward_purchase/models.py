from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime
from prodinward.models import prodinward
from supplier.models import suppliers
from django.urls import reverse

# Create your models here.

class inward_purchase(models.Model):
    date = models.DateField(default=datetime.utcnow)
    sup = models.ForeignKey(suppliers, on_delete=models.CASCADE, related_name="suppliers")
    products = models.ManyToManyField(prodinward, related_name='inward_purchase_bill')
    total = models.IntegerField(validators=[MinValueValidator(0, 'Value should not be less than 0')])
    gst = models.DecimalField(default=0, max_digits=9, decimal_places=2,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    net_amount = models.DecimalField( max_digits=15, decimal_places=2,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    due_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    sgst = models.DecimalField(default=0, max_digits=9, decimal_places=2,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    def __str__(self):
        return f"{self.id} "

    def get_absolute_url(self):
        return reverse('view-purchase')

