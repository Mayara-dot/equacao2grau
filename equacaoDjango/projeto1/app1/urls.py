from django.urls import path, include
from .views import index, create, modify

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('modify/<int:user_id>', modify, name='modify'),
]
