from django.contrib import admin

from Blog.crispy_blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

