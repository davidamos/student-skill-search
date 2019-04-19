# accounts/urls.py
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/add/', views.post_course, name='post_course'),
    path('courses/', views.all_courses, name='all_courses'),
    path('courses/add', views.add_course, name='add_course'),
    path('courses/majors', views.list_majors, name='list_majors'),
    path('courses/majors/<slug:course_code>', views.specified_major, name='specified_major'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('profile/you', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^messages/', include('postman.urls', namespace='postman')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
