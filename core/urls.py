from django.urls import path
from . import views
from core.views import user_registration

urlpatterns = [
    path('', views.index, name= 'Home'),
    path('about/', views.about, name= 'about'),
    path('management/', views.management, name= 'management'),
    path('students_leadership/', views.students_leadership, name= 'students_leadership'),
    path('academics/', views.academics, name= 'academics'),
    path('login/', views.login, name= 'login'),
    path('register/', user_registration, name='register'),

]