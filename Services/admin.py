from django.contrib import admin

# Register your models here.
from .models import BasicPackage,Description,Category,Gallery,Overview,PremiumPackage,Question,RatingService,StandardPackage

admin.site.register([BasicPackage,Description,Category,Gallery,PremiumPackage,Question,RatingService,StandardPackage])