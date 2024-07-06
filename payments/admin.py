from django.contrib import admin
from . models import Bank,PaymentMethod,PaymentWithdrawal,Refund_details,SellerAccountBalance,Transaction,Upi_id

admin.site.register([Bank,PaymentMethod,PaymentWithdrawal,Refund_details,SellerAccountBalance,Upi_id,])
# Register your models here.
