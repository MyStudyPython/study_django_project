# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello world ! ")


from django.shortcuts import render

# Create your views here.

# 导入数据模型Article
from .models import Article


def article_list(request):
    # 取出所有博客文学
    articles = Article.objects.all()
    # 需要传递给模版
    context = {"articles": articles}
    # render 函数：载入模版，并返回context对象
    return render(request, "article/list.html", context)
