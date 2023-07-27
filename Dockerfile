# 指定使用的语言镜像
FROM python:3.6
# 设置环境变量，方便后续使用
ENV PATH /usr/local/bin:$PATH
# 设置镜像内工作目录
WORKDIR /code
# 复制当前项目代码到工作目录中
ADD . /code
# 安装项目依赖
RUN pip install -r requirements.txt
# 运行项目的命令行命令
CMD ["/backend/docker_start.sh"]