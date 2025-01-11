from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    frontend_url = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'meta_title', 'content', 'thumbnail', 
            'slug', 'summary', 'status', 'meta_data', 
            'created_at', 'updated_at', 'published_at', 'frontend_url'
        ]

    def get_frontend_url(self, obj):
        return obj.get_frontend_url()
