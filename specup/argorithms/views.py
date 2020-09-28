from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .models import Argorithm
from .forms import ArgorithmForm

# Create your views here.
@require_safe
def index(request):
    argorithms = Argorithm.objects.all()
    context = {
        'argorithms':argorithms,
    }
    return render(request, "argorithms/index.html", context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = ArgorithmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("argorithms:index")
    else:
        form = ArgorithmForm()
    context = {
        "form":form,
    }
    return render(request, "argorithms/create.html", context)

@require_safe
def detail(request, pk):
    argorithm = get_object_or_404(Argorithm, pk=pk)
    context = {
        'argorithm':argorithm,
    }
    return render(request, 'argorithms/detail.html', context)

@require_http_methods(['GET','POST'])
def update(request, pk):
    argorithm = get_object_or_404(Argorithm, pk=pk)
    if request.method == "POST":
        form = ArgorithmForm(request.POST, instance=argorithm)
        if form.is_valid():
            form.save()
            return redirect("argorithms:detail", pk)
    else:
        form = ArgorithmForm(instance=argorithm)
    context = {
        'form':form,
        'argorithm':argorithm,
    }
    return render(request, "argorithms/update.html", context)

@require_POST
def delete(request, pk):
    argorithm = Argorithm.objects.get(pk=pk)
    argorithm.delete()
    return redirect("argorithms:index")