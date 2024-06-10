import django_filters
from .models import *
from django import forms

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['login']
        
class CommentFilter(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields = (
            ('comment_posted_at', 'comment_posted_at'),       
            ('comment_reaction', 'comment_reaction')
        )
    )

class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Поиск блюда')
    category = django_filters.ModelChoiceFilter(
        queryset = Category.objects.all(),
        empty_label = 'Все категории',
        label = 'Категория',
        widget = forms.Select(attrs={'class': 'form-control'}),
        
    )
    
    order_by = django_filters.OrderingFilter(
        fields = (
            ('posted_at', 'posted_at'),
            ('rating', 'rating'),
        )
    )
    
    class Meta:
        model = Recipe
        fields = []