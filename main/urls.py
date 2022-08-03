from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_user, name='log'),
    path('register/', views.register, name='reg'),
    path('teacher-register/', views.teach_reg, name='teach'),
    path('student-register/', views.stud_reg, name='stud'),
    path('logout-user/', views.user_logout, name='logout'),
]