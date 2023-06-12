"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 引入app视图
from application import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 添加app的url
    # path('hello/', views.hello),
    # 添加此项
    # path("article/", views.article_list),  # 展示文章
    # 修改此项，增加name参数
    path("list/", views.article_list, name="list"),  # 文章列表
    path("detail/<int:id>/", views.article_detail, name="detail"),  # 文章详情
    # 增加写文章
    path("create/", views.article_create, name="create"),
]
