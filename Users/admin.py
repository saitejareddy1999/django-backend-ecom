from django.contrib import admin
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 

# Register your models here.
User = get_user_model()
class UserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = ()
admin.site.register(User, UserAdmin)
