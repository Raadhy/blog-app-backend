from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'published_at')

admin.site.register(models.Post, PostAdmin)