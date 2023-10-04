from django.contrib import admin
from .models import User,Product, ProductCategory 

# Register the User model
admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductCategory)
