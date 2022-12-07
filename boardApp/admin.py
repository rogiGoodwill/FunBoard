from django.contrib import admin
from .models import User, Profile, Ad, Comments
# Register your models here.

admin.site.register(
    (Profile,
     Ad,
     Comments)
)