from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', custom_logout, name='logout'),

    path('', recipes, name='recipes' ),
    path('update_recipe/<id>/', update_recipe, name='update_recipe'),
    path('delete_recipe/<id>/', delete_recipe, name='delete_recipe'),
    path('pdf/', pdf, name='pdf'),

]
