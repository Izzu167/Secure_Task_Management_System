from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import AuditLog

# Helper function untuk dapatkan IP Address pengguna
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# =========================================================
# 1. REGISTER VIEW
# =========================================================
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Rekod Audit Log
            AuditLog.objects.create(
                user=user,
                action="User Registered",
                ip_address=get_client_ip(request)
            )
            
            messages.success(request, "Pendaftaran berjaya! Selamat datang.")
            return redirect('user_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# =========================================================
# 2. LOGIN VIEW
# =========================================================
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Rekod Audit Log
            AuditLog.objects.create(
                user=user,
                action="Login",
                ip_address=get_client_ip(request)
            )

            # Redirect ikut Role (Admin vs User)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, "Nama pengguna atau kata laluan salah.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# =========================================================
# 3. LOGOUT VIEW
# =========================================================
@login_required
def logout_view(request):
    # Rekod Audit Log sebelum logout
    AuditLog.objects.create(
        user=request.user,
        action="Logout",
        ip_address=get_client_ip(request)
    )
    
    logout(request)
    messages.info(request, "Anda telah log keluar.")
    return redirect('login_view')

# =========================================================
# 4. PROFILE VIEW (Logik untuk Upload Gambar)
# =========================================================
@login_required
def profile_view(request):
    if request.method == 'POST':
        # PENTING: request.FILES wajib ada untuk terima gambar
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            
            # Rekod Audit Log bila update profile
            AuditLog.objects.create(
                user=request.user,
                action="Profile Updated",
                ip_address=get_client_ip(request)
            )
            
            messages.success(request, 'Profil berjaya dikemaskini!')
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})

# =========================================================
# 5. CHANGE PASSWORD VIEW (Logik Tukar Password)
# =========================================================
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # PENTING: Update session supaya user tak kena tendang keluar (logout)
            update_session_auth_hash(request, user)  
            
            # Rekod Audit Log
            AuditLog.objects.create(
                user=request.user,
                action="Password Changed",
                ip_address=get_client_ip(request)
            )
            
            messages.success(request, 'Kata laluan berjaya ditukar!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Sila perbetulkan ralat di bawah.')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'accounts/change_password.html', {'form': form})