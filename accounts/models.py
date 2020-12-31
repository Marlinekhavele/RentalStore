from django.contrib.auth.models import User

class Customer(User):

    class Meta:
        proxy = True