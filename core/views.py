from django.shortcuts import render, redirect  # Tambah redirect di sini
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import AuditLog

# Fungsi Check: Adakah user ini Admin?
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def home(request):
    return render(request, 'core/home.html')

@login_required
def user_dashboard(request):
    return render(request, 'core/user_dashboard.html')

# --- BAHAGIAN ADMIN SAHAJA ---

@login_required
@user_passes_test(is_admin) # Hanya admin lepas
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
@user_passes_test(is_admin) # Hanya admin lepas
def audit_log_view(request):
    # Paparkan semua log, susun dari yang paling baru
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'core/audit_log.html', {'logs': logs})

# --- FUNGSI TUKAR BAHASA (BARU) ---
def change_language(request, lang_code):
    # 1. Simpan pilihan bahasa (ms atau en) dalam session pengguna
    request.session['lang'] = lang_code
    
    # 2. Redirect semula ke halaman di mana user berada tadi
    # Jika tiada referer, balik ke 'home'
    return redirect(request.META.get('HTTP_REFERER', 'home'))