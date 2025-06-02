from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Use Django built-in login/logout views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),

    # Custom views
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),

    # Dashboards
    path('dashboard/superadmin/', views.superadmin_dashboard, name='superadmin_dashboard'),
    path('dashboard/schooladmin/', views.schooladmin_dashboard, name='schooladmin_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),

    # Registration
    path('register/', views.register_user, name='register'),

    # Welcome page
    path('', views.welcome_view, name='welcome'),
]
