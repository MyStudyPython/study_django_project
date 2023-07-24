from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User

from application.models import Article

# 博文的评论
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)