# study_django_project
此项目前后端不分离

- [ ] docker部署还未完成


# 运行
### 配置环境.env: ctrl + shift + p 创建环境
### 安装依赖环境: pip install -r requirements.txt
### 执行迁移命令: python manage.py makemigrations 和 python manage.py migrate
### 创建管理员：python manage.py createsuperuser
### 启动项目: python3 manage.py runserver


# 报错记录
## 问题一
```sh
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.3 or newer is required; you have 1.0.3.
```
### 解决方式
原因：
MySQLclient 目前只支持到 Python3.4，而我使用了更高版本的 python（Python3.7）

在setting.py同文件夹下的_init_.py加入以下内容

```python
import pymysql
 
pymysql.version_info = (1, 4, 13, "final", 0)   # 指定版本
pymysql.install_as_MySQLd
```
