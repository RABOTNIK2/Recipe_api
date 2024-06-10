from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['login', 'image']
    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_of_comment', 'comment_to', 'author_rating']
# Register your models here.
