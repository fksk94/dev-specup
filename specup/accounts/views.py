from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
@require_safe
def index(request):
    users = get_user_model().objects.all()
    context={
        "users":users,
    }
    return render(request, "accounts/index.html", context)

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect("argorithms:index")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_user = form.save()
            auth_login(request, user_user)
            return redirect('argorithms:index')
    else:
        form = CustomUserCreationForm()
    context = {
        "form":form,
    }
    return render(request, "accounts/signup.html", context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("argorithms:index")

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'argorithms:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, "accounts/login.html", context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('argorithms:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('argorithms:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('argorithms:index')

@login_required
@require_http_methods(['GET', 'POST'])
def user_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context={
        "form":form,
    }
    return render(request, "accounts/user_password.html", context)

@login_required
def profile(request, name):
    User = get_user_model()
    user_data = get_object_or_404(User, username=name)
    context={
        "user_data":user_data,
    }
    return render(request, "accounts/profile.html", context)