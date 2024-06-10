from django.db import models
from django.utils import timezone

class User(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    image = models.TextField(default='https://avatars.mds.yandex.net/i?id=e8197f3d5210db81fe9863c7dff7e5bfe62b937e-12932351-images-thumbs&n=13')
    
    def __str__(self):
        return self.login

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=40, default='вкусный рецепт')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    incridients = models.TextField()
    image = models.TextField()
    rating = models.IntegerField(default=0)
    posted_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author_of_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_to = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.TextField(blank=True)
    content = models.TextField()
    comment_posted_at = models.DateTimeField(default=timezone.now)
    author_rating = models.IntegerField(default=0)
    comment_reaction = models.IntegerField(default=0) 

# Create your models here.
