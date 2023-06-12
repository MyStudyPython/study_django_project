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
from django.urls import path, re_path

# 引入app视图
# from application import views
# 引入app视图
import application.views
import userprofile.views

app_name = "article"

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('hello/', views.hello),
    # path("article/", views.article_list),  # 展示文章
    re_path(r"^$", application.views.article_list),
    # 修改此项，增加name参数
    path("list/", application.views.article_list, name="list"),  # 文章列表
    path("detail/<int:id>/", application.views.article_detail, name="detail"),  # 文章详情
    path("create/", application.views.article_create, name="create"),  # 写文章
    path("delete/<int:id>/", application.views.article_delete, name="delete"),  # 删除文章
    path("update/<int:id>/", application.views.article_update, name="update"),  # 更新文章
    # 增加用户管理
    path("login/", userprofile.views.user_login, name="login"),
    path("logout/", userprofile.views.user_logout, name="logout"),
]
