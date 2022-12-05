from django.contrib import admin
from .models import User, Category, Profile, Ad, Comments
# Register your models here.

admin.site.register(
    (Category,
     Profile,
     Ad,
     Comments)
)