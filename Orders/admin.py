from django.contrib import admin
from .models import DeliveryDetails,Order,Order_Requirements,Overview, Transaction,UserProfile
# Register your models here.

admin.site.register([DeliveryDetails,Order_Requirements,Overview, Transaction,UserProfile])