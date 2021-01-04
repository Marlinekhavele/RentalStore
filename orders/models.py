import uuid
from django.utils import timezone
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Customer
from books.models import Book

# Create your models here.
class Order(models.Model):
    """ order Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price_per_book = models.DecimalField(
        _("Order Cost"), decimal_places=2, max_digits=15, default=1.0
    )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def current_charge(self):

        days = (timezone.now() - self.created_at).days
        if days < 1:
            days = 1
        if days < 2:
            days = 2
        if days < 3:
            days = 3
        return days * self.book.daily_charge
        
    def altered_prices(self):
        if self.book_type=='fiction':
            return 2.00
        if self.book_type=='regular':
            return 1.00
        if self.book_type=='novels':
            return 4.50


    def ___str___(self):
        return self.id