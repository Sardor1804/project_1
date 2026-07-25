from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path("admin/", admin.site.urls),
    path("", include("subjects.urls")),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    # home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # apps
    path('subjects/', include('subjects.urls')),
    path('accounts/', include('accounts.urls')),

    # auth
    path('auth/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # i18n
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)