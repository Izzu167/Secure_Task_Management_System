from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views 

# --- IMPORT PENTING UNTUK GAMBAR (MEDIA) ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- 1. Laluan Admin ---
    path('admin/', admin.site.urls),

    # --- 2. Sambungan ke App Lain ---
    path('accounts/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),

    # --- 3. Laluan Dashboard & Core Views ---
    path('home/', views.home, name='home'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('audit-log/', views.audit_log_view, name='audit_log'),

    # --- 4. Laluan Tukar Bahasa ---
    path('change-lang/<str:lang_code>/', views.change_language, name='change_language'),

    # --- 5. Redirect Halaman Utama ---
    path('', RedirectView.as_view(url='/accounts/login/'), name='index'),
]

# ==================================================================
# KOD WAJIB UNTUK PAPAR GAMBAR PROFIL
# Tanpa ini, gambar yang diupload akan jadi '404 Not Found'
# ==================================================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)