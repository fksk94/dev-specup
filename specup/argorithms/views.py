from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .models import Argorithm, Comment
from .forms import ArgorithmForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    argorithms = Argorithm.objects.all()
    context = {
        'argorithms':argorithms,
    }
    return render(request, "argorithms/index.html", context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = ArgorithmForm(request.POST)
        if form.is_valid():
            argorithm = form.save(commit=False)
            argorithm.user = request.user
            argorithm.save()
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
    comment_form = CommentForm()
    comments = argorithm.comment_set.all()
    context = {
        'argorithm':argorithm,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'argorithms/detail.html', context)

@require_http_methods(['GET','POST'])
def update(request, pk):
    argorithm = get_object_or_404(Argorithm, pk=pk)
    if request.user == argorithm.user:
        if request.method == "POST":
            form = ArgorithmForm(request.POST, instance=argorithm)
            if form.is_valid():
                form.save()
                return redirect("argorithms:detail", pk)
        else:
            form = ArgorithmForm(instance=argorithm)
    else:
        return redirect("argorithms:index")
    context = {
        'form':form,
        'argorithm':argorithm,
    }
    return render(request, "argorithms/update.html", context)

@require_POST
def delete(request, pk):
    argorithm = get_object_or_404(Argorithm, pk=pk)
    if request.user == argorithm.user:
        argorithm.delete()
        return redirect("argorithms:index")
    return redirect("argorithms:detail", pk)

@require_POST
def comments_create(request, pk):
    argorithm = get_object_or_404(Argorithm, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.argorithm = argorithm
        comment.save()
        return redirect("argorithms:detail", pk)
    context = {
        "comment_form" : comment_form,
    }
    return render(request, 'argorithms/detail.html', context)

@require_POST
def comments_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('argorithms:detail', pk)