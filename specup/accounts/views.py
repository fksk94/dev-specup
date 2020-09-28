from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_logtin, logout as auth_logout
from .forms import CustomUserCreationForm

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
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_user = form.save()
            auth_logtin(request, user_user)
            return redirect('argorithms:index')
    else:
        form = CustomUserCreationForm()
    context = {
        "form":form,
    }
    return render(request, "accounts/signup.html", context)
        


