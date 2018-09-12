from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'published_date']


# register the Post model.
admin.site.register(Post, PostAdmin)
