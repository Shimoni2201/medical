from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime
from prodoutward.models import prodoutward
from customer.models import customer
from django.urls import reverse

# Create your models here.

class outward_purchase(models.Model):
    date = models.DateField(default=datetime.utcnow)
    cus = models.ForeignKey(customer, on_delete=models.CASCADE, related_name="customers")
    products = models.ManyToManyField(prodoutward, related_name='outward_purchase_bill')
    total = models.IntegerField(validators=[MinValueValidator(0, 'Value should not be less than 0')])
    gst = models.DecimalField(default=0, max_digits=9, decimal_places=2,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    net_amount = models.DecimalField(max_digits=9, decimal_places=2,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    due_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    sgst = models.DecimalField(default=0, max_digits=9, decimal_places=2,validators=[MinValueValidator(0, 'Value should not be less than 0')])
    def __str__(self):
        return f"{self.id} "

    def get_absolute_url(self):
        return reverse('purchase-view')

