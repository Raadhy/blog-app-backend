from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'created_at', 'updated_at', 'is_active']

admin.site.register(models.User, UserAdmin)