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
        if self.book.book_type == 'regular':
            if days <= 2:
                return 2.0
            return (self.book.daily_charge * (days-2.0)) + 2.0 # every extra day add to base days
        if self.book.book_type == 'novels':
            if days <= 3:
                return 4.5
            return (self.book.daily_charge * (days-3.0)) + 4.5 # every extra day add to base days
        return days * self.book.daily_charge
    def ___str___(self):
        return self.id