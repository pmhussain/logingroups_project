from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name="register"),
    path('', views.userlogin, name="login"),
    path('hod_page', views.hod, name="hod"),
    path('staff_page', views.staff, name="staff"),
    path('student_page', views.student, name="student"),
    path('logout/', views.userlogout, name="logout"),
]
