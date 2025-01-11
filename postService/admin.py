from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'published_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_approved')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'is_approved')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)