"""uploat_imgs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import index,uploat_img
# server 用来处理静态文件的函数
from uploat_imgs import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    # 配置上传文件的路由
    url(r'^upload',uploat_img,name='upload'),
    # 配置一个获取上传文件的路由，使用django自带的serve 函数获取图片
    # serve 中主要的功能: 根据media绝对路径和path参数路径拼接完整路径，打开路径下的文件进行读取操作，封装response 返回response对象
    # 1
    url(r"^media/(?P<path>.*)$",serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    url(r'^$',index, name='index'),
    url(r'^admin/', admin.site.urls),]
# 2 配置路由的方法 自动创建路由
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
