from django.urls import path
from . import views

urlpatterns = [
    path('math/easy/', views.math_easy, name='math_easy'),
    path('math/normal/', views.math_normal, name='math_normal'),
    path('math/hard/', views.math_hard, name='math_hard'),
    
    path('physics/easy/', views.physics_easy, name='physics_easy'),
    path('physics/normal/', views.physics_normal, name='physics_normal'),
    path('physics/hard/', views.physics_hard, name='physics_hard'),

    path('informatics/easy/', views.informatics_easy, name='informatics_easy'),
    path('informatics/normal/', views.informatics_normal, name='informatics_normal'),
    path('informatics/hard/', views.informatics_hard, name='informatics_hard'),
]