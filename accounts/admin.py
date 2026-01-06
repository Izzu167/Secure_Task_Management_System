from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AuditLog

# 1. Konfigurasi untuk paparan CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Jawatan', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role & Jawatan', {'fields': ('role',)}),
    )

# 2. Konfigurasi untuk AuditLog
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'user', 'action', 'ip_address']
    list_filter = ['action', 'timestamp']
    search_fields = ['user__username', 'action']
    
    # SAYA DAH BUANG 'details' DARI SINI SUPAYA TIADA ERROR
    readonly_fields = ['timestamp', 'user', 'action', 'ip_address']

# 3. Daftar Model
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AuditLog, AuditLogAdmin)