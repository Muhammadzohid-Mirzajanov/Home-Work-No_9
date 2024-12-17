from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_flowers, name='all_flowers'),  # Barcha gullarni ko'rsatadi
    path('type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),  # Turlar bo'yicha gullar
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),  # Bitta gulni batafsil
]
