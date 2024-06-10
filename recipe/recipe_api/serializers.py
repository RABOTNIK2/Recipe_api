from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Recipe
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    author_of_comment = serializers.StringRelatedField()
    comment_to = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = "__all__"
         