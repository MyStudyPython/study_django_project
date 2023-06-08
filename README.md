# study_django
> Python + Django4 搭建个人博客
# 搭建博客需要哪些技术，网站包括哪些内容
## 一、需要的和将得到的技术知识
> - Python：有一定基础最好，零基础也可以学习
> - Django：本系列博文将手把手教学搭建Django项目，完整的学习本系列博文基本能掌握Django的核心功能
> - 前端：一点点的HTML，CSS相关基础就可，主要使用Bootstrap框架来实现网页的展示和渲染，通过此系列博文将了解和掌握Bootstrap在实战项目的应用。
> - 数据库：本项目使用目前最流行的MySQL，本系列博文将手把手教学在Django项目中的MySQL数据库的连接和配置。

## 二、个人博客网站包含的内容和功能
一个典型的博客网站，主要包含如下几个功能模块：
![](https://img-blog.csdnimg.cn/img_convert/a42be2ca25f70849034c26581fe6d105.png)

1、用户管理：用户的注册和登录

2、文章管理：文章的新建，修改，查看以及文章列表展示和排序

3、评论管理：评论的添加，修改和删除

## 三、网站框架设计及实现思路
系统设计包括三部分：数据库设计，功能函数视图设计，前端页面设计
### 1. 数据库设计
按照前面的功能模块，我们需要自定义数据表如下：

博客文章表：ArticlePost

评论表：Comment

另外我们为了快速实现系统，用户管理功能实现我们直接基于Django自带的用户及认证模块。

### 2. 页面及功能设计
为了实现我们前面的功能模块我们设计如下几个功能页面：
![](https://img-blog.csdnimg.cn/img_convert/44c248d1d58a9d477d32eed735d36345.png)

#### 1、登录页面：

其中需要登录，校验，登录后同时需要存储用户信息在Session中，以备登录后的页面使用。

#### 2、注册页面：

提供注册信息表单，提交注册通过后，系统生成一个新的用户。

##### 3、首页（博文列表页）：

展示所有的博文列表并实现列表的分页功能，点击阅读链接可以查看文章详情，另外我们增加浏览量显示功能用于进行简单的数据统计。

#### 4、写文章页面：

撰写文章并发布文章

#### 5、文章详情页面：

展示文章详情，并提供修改文章，删除文章功能按钮。

#### 6、评论管理页面

添加评论，删除评论和显示评论。

#### 7、后台管理

为了快速实现系统我们将直接启用Django自带的Admin管理功能。