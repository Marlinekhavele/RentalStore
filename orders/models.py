import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Customer
from books.models import Book

# Create your models here.
class Order(models.Model):
    """ order Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price_per_book = models.DecimalField(_('Order Cost'), decimal_places=2, max_digits=15)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer"
    )
   
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def current_price(self):
        return (datetime.now() - self.created_at).days * price_per_book

    def ___str___(self):
        return self.id