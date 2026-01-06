from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# =========================================================
# 1. BORANG PENDAFTARAN (REGISTER)
# =========================================================
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        # Kami hanya paparkan username & email.
        # Password diuruskan automatik oleh UserCreationForm.
        fields = ("username", "email")

    # Validasi: Pastikan email belum digunakan
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ini sudah digunakan.")
        return email

    # Save: Paksa setiap pendaftaran baru menjadi 'user' biasa
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'user'  # Set default role kepada 'user' demi keselamatan
        if commit:
            user.save()
        return user

# =========================================================
# 2. BORANG PROFIL (PROFILE) - WAJIB ADA UNTUK GAMBAR
# =========================================================
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # User boleh edit Username, Email, dan Gambar (Avatar)
        fields = ['username', 'email', 'avatar']

# =========================================================
# 3. BORANG LOGIN (STANDARD)
# =========================================================
class CustomAuthenticationForm(AuthenticationForm):
    pass