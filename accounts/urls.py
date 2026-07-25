from django.urls import path
from .views import (
    home,
    login_view,
    register_view,
    logout_view,
    profile_view,
    profile_english_view,
    finish_test,
    add_course,
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('profile/', profile_view, name='profile'),
    path('profile/english/', profile_english_view, name='profile_english'),

    path('finish-test/', finish_test, name='finish_test'),
    path('add-course/', add_course, name='add_course'),
]