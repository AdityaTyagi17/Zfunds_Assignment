from django.contrib import admin
from .models import User,Product, ProductCategory  # Import the User model from your app's models

# Register the User model
admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductCategory)
