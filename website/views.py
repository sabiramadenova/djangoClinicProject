from datetime import timezone, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from website.models import Doctor, Post, Department
from .forms import PostForm


# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    return render(request, "index.html", {"departments": departments, "doctors": doctors})


def about(request):
    doctors = Doctor.objects.all()
    return render(request, "about.html", {"doctors": doctors})


def contact(request):
    # return HttpResponse("Hello world, nice to meet you!")
    return render(request, "contact.html", {})


def news(request, pk=-1):
    if pk == -1:
        posts = Post.objects.all()
        return render(request, "news.html", {"posts": posts})
    else:
        post = Post.objects.get(id=pk)
        return render(request, 'blog-details.html', {"post": post})


def services(request):
    return render(request, "services.html", {})


def about_team(request):
    doctors = Doctor.objects.all()
    return render(request, "about_team.html", {"doctors": doctors})


def post_new(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "create_post.html", context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.tags = request.POST['text']
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def personal_page(request, id):
    personal_information = Doctor.objects.get(pk=id)
    return render(request, 'personal_page.html', {"personal_information": personal_information})


