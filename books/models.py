import uuid
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    BOOK_TYPE = (
       ('regular', _('Regular')),
       ('fiction', _('Fiction')),
       ('novels', _('Novels')),
       )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn = models.CharField(_("ISBN"), max_length=13, unique=True)
    title = models.CharField(_("Book's title"), max_length=128)
    publisher = models.CharField(_("Publisher"), max_length=64)
    author = models.CharField(_("Author"), max_length=64)
    book_type = models.CharField(_('Book Type'), max_length=20, choices=BOOK_TYPE,default='regular')
    flat_days_charge = models.DecimalField(_('Flat Days Charge'),decimal_places=2, max_digits=15, default=1.0)
    pages = models.IntegerField(_("Pages"), default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def daily_charge(self):
        if self.book_type=='fiction':
            return 3.00
        if self.book_type=='regular':
            return 1.50
        if self.book_type=='novels':
            return 1.50
            
    def __str__(self):
        return self.title
