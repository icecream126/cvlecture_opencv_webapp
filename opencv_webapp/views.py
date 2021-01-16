from django.shortcuts import render, redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
#request가 오면 opencv_webapp의 first_view.html로 가란ㄴ 뜻이 된다
def first_view(request):
    return render(request,'opencv_webapp/first_view.html',{})

def uimage(request):
    #UploadImageForm : Image를 업로드할 때 사용할 함수
    #FileSystemStorage : Image를 저장할 때 사용할 함수

    #글을 쓰려고 할때는 if문으로 들어가고 아닐 때는 else로 빠짐
    if request.method =='POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'opencv_webapp/uimage.html',{'form':form, 'uploaded_file_url':uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request,'opencv_webapp/uimage.html', {'form':form})