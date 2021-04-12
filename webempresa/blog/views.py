from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def blog(request):

    posts = Post.objects.all()
    # lo pasamos al template con el diccionario de contexto
    return render(request,"blog/blog.html",{'posts':posts})


def category(request, category_id):
    # forma rudimentaria de trabajar
    # category = get_object_or_404(Category, id=category_id)
    # posts = Post.objects.filter(categories=category)
    # return render(request,"blog/category.html",{'category':category,
    #                                             'posts':posts})
    category = get_object_or_404(Category, id=category_id)
    # posts = Post.objects.filter(categories=category)
    return render(request,"blog/category.html",{'category':category})

                                            



    # get_object_or_404(Category, id=category_id)
    # posts = Post.objects.filter(categories=category)
    # return render(request,"blog/category.html",{'category':category},{'posts':posts})