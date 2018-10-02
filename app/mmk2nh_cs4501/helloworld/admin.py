from django.contrib import admin
# Register your models here.
from helloworld.models import Shoe, User, Transactions, Inventory
admin.site.register(Shoe)
admin.site.register(User)
admin.site.register(Transactions)
admin.site.register(Inventory)
