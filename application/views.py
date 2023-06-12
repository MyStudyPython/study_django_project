# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello world ! ")

# 引入redirect用于重定向地址
from django.shortcuts import render, redirect

# Create your views here.
# 导入数据模型Article
from .models import Article

from django.http import HttpResponse

# 引入刚才定义的ArticleForm表单类
from .forms import ArticleForm


def article_list(request):
    # 取出所有博客文学
    articles = Article.objects.all()
    # 需要传递给模版
    context = {"articles": articles}
    # render 函数：载入模版，并返回context对象
    return render(request, "article/list.html", context)


# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = Article.objects.get(id=id)
    # 需要传递给模板的对象
    context = {"article": article}
    # 载入模板，并返回context对象
    return render(request, "article/detail.html", context)


# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 作者为当前请求的用户名
            new_article.author = request.user
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文
        context = {"article_post_form": article_post_form}
        # 返回模板
        return render(request, "article/create.html", context)
