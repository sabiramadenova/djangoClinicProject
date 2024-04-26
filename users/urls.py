from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from clinicProject import settings
from .views import register, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)