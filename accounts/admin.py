from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Result

admin.site.register(User, UserAdmin)
admin.site.register(Result)