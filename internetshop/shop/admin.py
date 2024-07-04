from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Review, ReviewAdmin)
