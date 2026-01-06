from django.urls import path
from . import views

urlpatterns = [
    # Laluan sedia ada
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile_view, name='user_profile'),

    # --- TAMBAH INI: LALUAN TUKAR PASSWORD ---
    # Ini menghubungkan URL 'change-password/' dengan fungsi 'change_password_view'
    path('change-password/', views.change_password_view, name='change_password'),
]