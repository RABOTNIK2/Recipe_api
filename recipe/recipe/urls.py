"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipe_api import views


categorypatterns= [
    path('catlist/', views.CategoryAPIList.as_view()),
    path('cat_create/', views.CategoryCreate.as_view()),
    path('cat_detail/<int:pk>/', views.CategoryDetail.as_view(), name = 'cat-detail'),
]

userpatterns = [
    path('user_lc/', views.UserAPIList.as_view()),
    path('user_detail/<int:pk>/', views.UserDetail.as_view())
]

recipepatterns= [
    path('recipe_list/', views.RecipeAPIList.as_view()),
    path('recipe_create/', views.RecipeCreate.as_view()),
    path('recipe_detail/<int:pk>/', views.RecipeDetail.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe_api/', include(categorypatterns)),
    path('recipe_api/', include(userpatterns)),
    path('recipe_api/', include(recipepatterns)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
