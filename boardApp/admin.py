from django.contrib import admin
from .models import User, Ad, Comments, Category
# Register your models here.

admin.site.register(
    (Ad,
     Comments,
     Category)
)