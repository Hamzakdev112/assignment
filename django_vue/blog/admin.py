from .models import Post
from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'published')
