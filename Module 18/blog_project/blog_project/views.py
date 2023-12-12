from django.shortcuts import render
from posts.models import Post
from categories.models import Category

# def home(request):
#     data = Post.objects.all()
#     # print(data)
#     # for i in data:
#     #     # print(i.title)
#     #     for j in i.category.all():
#     #         print(j)
#     #     print()
#     categories = Category.objects.all()
#     return render(request, 'home.html', {'data': data, 'categories': categories})


def home(request, category_slug=None):
    data = Post.objects.all()
    # print(data)
    # for i in data:
    #     # print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()

    # if category_slug:
    #     data = data.filter(category__slug=category_slug)
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'categories': categories})