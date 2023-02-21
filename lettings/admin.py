from django.contrib import admin

from .models import Letting
from .models import Address

admin.site.register(Letting)
admin.site.register(Address)
