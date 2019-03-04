# accounts/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile')
    url(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)