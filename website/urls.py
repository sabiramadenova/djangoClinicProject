from django.conf.urls.static import static
from django.urls import path

from clinicProject import settings
from website import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news),
    path('services/', views.services, name='services'),
    path('about_team/', views.about_team, name='about_team'),
    path('post/new/', views.post_new, name='post_new'),
    path('personalpage/<int:id>/', views.personal_page, name='personalpage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)