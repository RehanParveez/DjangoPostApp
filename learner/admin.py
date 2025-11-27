from django.contrib import admin
from learner.models import Post

# Register your models here.
admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'status']

