
from django.shortcuts import render,HttpResponse,redirect
from app.models import Uploat_imags

# Create your views here.


def index(request):
    # 显示数据库的图片 用server函数
    imgs = Uploat_imags.objects.all()
    # if not imgs:
    #     imgs = 1
    return render(request,'index.html',{'imgs':imgs})
    # return render(request,'index.html')

def uploat_img(request):
    if request.method =='POST':
        # 1 获取上传的图片
        imgfile = request.FILES.get('img')
        # imgfile.size 文件大小  做文件上传限制
        # imgfile.content_type 文件类型 做文件类型判断
        # imgfile.name 文件名称
        # 2 创建数据模型对象
        print(imgfile,imgfile.name)
        print(imgfile.size)
        mg = Uploat_imags(img_src=imgfile,img_name=imgfile.name)
        mg.save()
        return redirect('/')
        # return render(request, 'index.html')
    elif request.method =='GET':
        imgs = Uploat_imags.objects.all()
        return render(request, 'index.html', {'imgs': imgs})