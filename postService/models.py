import uuid
from django.db import models
from django.utils.text import slugify
from authService import models as authModel

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(authModel.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='post/thumbnail', default='https://cdn.pixabay.com/photo/2015/11/03/08/58/post-1019869_1280.jpg')
    slug = models.SlugField(max_length=264, unique=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    meta_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-published_at',)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            base_slug = slugify(self.title)
            if self.published_at:
                date_str = self.published_at.strftime('%Y-%m-%d')
                self.slug = f"{base_slug}-{date_str}"
            else:
                self.slug = base_slug

            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"

        super().save(*args, **kwargs)

    def get_frontend_url(self):
        return f"http://127.0.0.1:8000/posts/{self.slug}"

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return "Commented By {} on {}".format(self.name, self.post.title)
