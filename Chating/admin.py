from django.contrib import admin
from . models import Message,Order
# Register your models here.

admin.site.register([Message,Order])