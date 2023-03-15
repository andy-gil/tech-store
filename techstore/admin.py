from django.contrib import admin
from .models import Item
from .models import Laptops
from .models import Desktops
from .models import Cart

# Register your models here.
admin.site.register(Item)
admin.site.register(Laptops)
admin.site.register(Desktops)
admin.site.register(Cart)