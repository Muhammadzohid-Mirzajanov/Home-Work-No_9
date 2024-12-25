from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_flowers, name='all_flowers'),
    path('type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
    path('add/flower/', views.add_flower, name='add_flower'),
    path('add/type/', views.add_type, name='add_type'),
    path('type/update/<int:type_id>/', views.update_type, name='update_type'),
    path('flower/update/<int:flower_id>/', views.update_flower, name='update_flower'),
]
