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

# 准备开发环境
本系列博文实现博客网站使用到的开发相关的技术和软件版本如下：

**服务端**：Python 3.9

**Web框架**：Django 4.10

**数据库**：MySQL mysql-8.0.13-winx64

**开发工具IDE**：vscode

**前端框架**：Bootstrap 5

大家参考学习的时候最好使用相同的版本，下面简单介绍相关软件的安装和环境配置。

## Python3
### Python3 下载
Python3 最新源码，二进制文档，新闻资讯等可以在 Python 的官网查看到：

Python 官网：[Welcome to Python.org](https://www.python.org/)

你可以在以下链接中下载 Python 的文档，你可以下载 HTML、PDF 和 PostScript 等格式的文档。

Python文档下载地址：[Our Documentation | Python.org](https://www.python.org/doc/)

Python 安装
Python 已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。

我们需要下载适用于使用平台安装包，然后安装 Python。

以下为在 Window 平台上安装 Python 的简单步骤。

打开 WEB 浏览器访问 [Python Releases for Windows | Python.org](https://www.python.org/downloads/windows/) ，一般就下载 Windows installer，x86 表示是 32 位机子的，x86-64 表示 64 位机子的。

![](https://img-blog.csdnimg.cn/img_convert/e3d3a0bb0eccb2b3994be3e8d081d36f.png)

安装过程中记得勾选 **Add Python 3.X to PATH**,**否则需要我们手工去添加电脑的环境变量.**
![](https://img-blog.csdnimg.cn/img_convert/435ee997008208a32dd388652e38e2b9.png)

安装完成后按 Win+R 键，输入 cmd 调出命令提示符，输入 python:出现如下界面说明安装成功.
![](https://img-blog.csdnimg.cn/img_convert/a8796ec2436005195f5a4af80016b38a.png)

#### 万一我们在之前安装的时候没有勾选添加到环境变量,手工添加Windows环境变量的方法如下:
**在 Windows 设置环境变量**
在环境变量中添加Python目录：

**在命令提示框中(cmd)** : 输入

path=%path%;C:\Python

按下"Enter"。

**注意**: C:\Python 是Python的安装目录。

也可以通过以下方式设置：

1. 右键点击"计算机"，然后点击"属性"
2. 然后点击"高级系统设置"
3. 选择"系统变量"窗口下面的"Path",双击即可！
4. 然后在"Path"行，添加python安装路径即可(我的D:\Python32)，所以在后面，添加该路径即可。 **ps：记住，路径直接用分号"；"隔开！**
5. 最后设置成功以后，在cmd命令行，输入命令"python"，就可以有相关显示。
![](https://img-blog.csdnimg.cn/img_convert/e937ac174038b4fd385087c42c4799f1.png)

## Django
这里我们先不安装Django，待我们配置好虚拟环境后再安装。

## MySQL
### 安装MySQL
安装包下载地址:[MySQL :: Download MySQL Installer](https://dev.mysql.com/downloads/windows/installer/8.0.html)

建议选择离线版,下载后直接安装.
![](https://img-blog.csdnimg.cn/img_convert/ef2e8336367741cc710dd4cbaafd0d6d.png)

点击 Download 进行下载，弹出页面让你注册或者登录，我们如果不想登录或注册的话，只需要点击 No thanks, just start my download 按钮即可。
![](https://img-blog.csdnimg.cn/26ee9b851abc4a48a6b2cbc240900819.png)

详细安装教程:[MySQL安装教程（2023年，4月）](https://blog.csdn.net/hh2093531258/article/details/130340540?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-130340540-blog-115282713.235%5Ev38%5Epc_relevant_sort_base2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-130340540-blog-115282713.235%5Ev38%5Epc_relevant_sort_base2&utm_relevant_index=5)

## MongoDB数据库(这次没用上)
### 安装MongoDB
安装包下载地址:[MongoDB Community Server Download](https://www.mongodb.com/try/download/community)
![](https://pic4.zhimg.com/80/v2-072c070613ae9d031f5dcab7991edb3f_720w.webp)

一路下一步安装，路径不要出现空格中文等特殊字符

不要勾选 Install MongoDB Compass

![](https://img-blog.csdnimg.cn/fa79fa49f73b4b1d97e444dabd7e5147.png)

### 下载MongoDB Shell (老版本是和安装工具打包在一起 新版本分开了 需要重新下载)
安装包下载地址:[MongoDB Shell Download](https://www.mongodb.com/try/download/shell)
![](https://pic4.zhimg.com/80/v2-072c070613ae9d031f5dcab7991edb3f_720w.webp)

下载 zip 包     将zip包里面的bin 目录下的 文件 拷贝到 MongoDB 安装目标 bin 目录下:
![](https://img-blog.csdnimg.cn/4cf3c624c7da40c0930ff244398405e3.png)

### 设置环境变量
将 MongoDB 安装目录下bin 目录  设置 全局变量 path 下的 环境变量
### 在命令提示符窗口输入 mongod
弹出以下内容后继续输入 mongosh运行mongosh 进入命令行模式
![](https://pic3.zhimg.com/80/v2-e51d179a24535e73f51dc8ae4d901bf2_720w.webp)

输入 use admin

输入 db.createUser({ user: "root", pwd: "123456", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] })
![](https://img-blog.csdnimg.cn/2cf86873bbf64db491a55d530a3740a0.png)

如上图 代表执行成功

到此为止  用户名:root  密码:123456 设置好了

最后使用 Navicat 连接
![](https://img-blog.csdnimg.cn/b396d2bae449495f91a82a83776df777.png)

### MongoDB常用语句
show dbs（databases）: 显示所有数据库
![](https://pic3.zhimg.com/80/v2-6e5067767b6b259c6e1159216b88499a_720w.webp)

use xxxx: 使用指定数据库/创建数据库（新库中插入数据才可以显示新库）

db: 当前正在使用的数据库
![](https://pic4.zhimg.com/80/v2-28b099a3609255a1f215973f045a3cd7_720w.webp)

db.dropDatabase(): 删除当前数据库

show collections: 显示当前数据库中所有的集合

### 插入内容，如果表名不存在则新建一个表
```sh
db.用户表.insert({名字:"张三", 年龄:18, 爱好:['吃','睡','玩' ]})
```
![](https://pic3.zhimg.com/80/v2-9036f17d23e42f8b6fde2c80421af35e_720w.webp)

### 修改数据，multi如果多条数据满足条件是否修改
```sh
将名字为张三的数据，年龄修改为19
db.用户表.update({名字:'张三'},{$set:{年龄:19}},{multi:true})
```
![](https://pic2.zhimg.com/80/v2-b06c6b4dc1870486ff6bc077c575fbc5_720w.webp)

### 删除数据
```sh
清空集合的所有数据db.用户表.remove({})
删除集合 collectionsdb.用户表.drop()
删除数据库 db.dropDatabase()
删除一个数据db.用户表.deleteOne()
删除多行数据db.用户表.deleteMany()


db.用户表.deleteOne({年龄:19})
```

![](https://pic3.zhimg.com/80/v2-3edd12af798cd68382b8b543e0cb5786_720w.webp)

### 查询数据
```sh
db.用户表.find() 查询所有
db.用户表.find({"字段":"固定值"})  查询满足条件的所有数据
db.用户表.findOne({条件})  查询满足条件的第一条数据
db.getCollection('用户表').find({"字段1":"固定值1","字段2":"固定值2"})
```

### Python连接MongoDB数据库
```python
import pymongo


def 连接对象(数据库名):
    连接数据库=pymongo.MongoClient(host='192.168.0.151',port=27017)
    数据库=连接数据库[数据库名]
    return 数据库


print(连接对象('aiyou'))
def 增加数据(表名,数据):
    数据库=连接对象('aiyou')
    print(数据库)
    数据库[表名].insert_one(数据)


增加数据('用户表',{"名字":"赵六","年龄":18})
```

# vscode配置虚拟环境
## 安装扩展插件
![](https://img-blog.csdnimg.cn/img_convert/573e87ef8eee93e44479243efb7f04bd.png)
## 打开我们的vscode选择一个文件夹创建django项目
这里也可以直接在终端创建，但是为了不占用C盘空间和防止目录不好找到，先在D盘创建空白文件夹进入后再终端创建。创建项目命令：
```sh
django-admin startproject Blog
```
![](https://img-blog.csdnimg.cn/img_convert/bcf59456a6a6bcb9db2e672c74973599.png)

## 为创建的项目创建虚拟环境
这个时候需要打开创建的项目的根目录，而不是空白文件夹作为根目录，需要进入创建的项目文件夹，也就是Blog目录，可以终端直接cd进入也可以重新打开进入Blog文件夹，然后终端输入：
```sh
python -m venv venv
```
创建虚拟环境：

![](https://img-blog.csdnimg.cn/img_convert/dd865ae35a2e55e75ce82c562fd6d6b4.png)

这里注意会遇到一些问题，比如下图的：

![](https://img-blog.csdnimg.cn/img_convert/aed647946698143551ec75881f1a7808.png)

显示没有这个文件或目录，这样的问题解决办法是首先python默认路径改成anaconda3下面的：

![](https://img-blog.csdnimg.cn/img_convert/068613fda4e67df401705df22a2258f3.png)

然后再将报错中路径缺少的python.exe和pythonw.exe从anaconda3目录下复制到报错中nt目录下:
![](https://img-blog.csdnimg.cn/img_convert/134b8cf0f59424761c67f4305e3b62ff.png)
![](https://img-blog.csdnimg.cn/img_convert/f397339c1c894265e70be9dc0dd1d99e.png)
然后重新输入命令python -m venv venv就成功创建了，完美解决！

## 选择解释器
一定注意要从创建的项目文件打卡，能避免低级错误。同时按下Shift+Ctrl+P搜索python解释器，然后选择我们创建的虚拟环境：
![](https://img-blog.csdnimg.cn/img_convert/8c1d8f28df37419cc21b968768acb1c6.png)
![](https://img-blog.csdnimg.cn/img_convert/ace4c3f33967d98612daf78e99ff590e.png)
这里我出现了一个错误，默认的python路径和创建项目的python不一样而且版本不同，后面修改了默认路径就OK了

## 调试使用创建的Django项目
创建好虚拟环境后，新建终端就可以用虚拟环境运行了，如图：
![](https://img-blog.csdnimg.cn/img_convert/606da47debf5ebc6590880b5ef45c3ab.png)

但是此时我们需要重新下载一下django包，因为使用的虚拟环境：
```sh
pip install django
```
然后进行调试：

![](https://img-blog.csdnimg.cn/img_convert/72c0851257b48eac3cd6f8dc818f8cbe.png)

```sh
python manage.py runserver
```
点击运行成功后终端显示：

![](https://img-blog.csdnimg.cn/img_convert/1dcddb1e1d1094d7fab77b1827d0bf80.png)

**报错信息翻译**
您有18个未应用的迁移。在应用程序迁移之前，您的项目可能无法正常工作：管理员、身份验证、内容类型、会话。
运行“python管理”。py migrate’来应用它们。

**报错原因**
有18个未应用的迁移。小伙伴们执行下面代码重建表结构即可！！！

**解决方法**
1. 先执行下面的代码，它可以让我们在修改Model后可以在不影响现有数据的前提下重建表结构：
   ```py
   python manage.py migrate
   ```

   ![](https://img-blog.csdnimg.cn/974357a46e7144aab7a78d410678d269.png)

2. 再次启动服务器
  ```py
   python manage.py runserver
  ```
  ![](https://img-blog.csdnimg.cn/74d9a46ced284a34a8440844d575a435.png)


## 项目文件解释
![](https://img-blog.csdnimg.cn/img_convert/3ff578d60419e5679bc700cf254e1225.png)
Bolg

manage.py // 项目管理、启动、创建app、数据管理都在这里，不要动它

Bolg

__init__.py  // 初始化文件，一般情况下无须修改。

settings.py // 项目的配置文件，很多操作也在这里（链接数据库）

urls.py // url和python函数的对应关系都在这里，操作基本都在这里

asgi.py // 异步接受网络请求的

wsgi.py // 同步接受网络请求的

## 创建APP（startapp）
app不是应用，是功能的划分，创建app需要靠manage.py，终端输入：
```sh
python manage.py startapp application01
```
![](https://img-blog.csdnimg.cn/img_convert/3150ae2731b248613e101b83ab66b5ac.png)

__init__.py：初始化文件，一般情况下无须修改。

admin.py：后台管理的配置文件 , 后期我们的可以通过他管理我们的model和数据库。

apps.py：django菜单文件。

models.py：模型文件，用于创建模型和数据库表的映射关系，用于项目和数据库之间的数据处理。

views.py：视图文件，用于实现我们具体的Web请求和返回响应。

tests.py：测试文件。