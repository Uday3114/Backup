from django.shortcuts import render
from .models import UploadingImage
from .forms import CricketerForm
from django.http import HttpResponse

# Create your views here.
def crickimgview(request):
	form = CricketerForm()
	if request.method=='POST':
		form = CricketerForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return success(request)
	return render(request,'imageapp/display.html',{'form':form})

def success(request):
	s1 = "<center><h1>Image was Sucessfully Uploaded</h1></center>"
	return HttpResponse(s1)


def display_crick_img(request):
	if request.method=='GET':
		cricketers = UploadingImage.objects.all()
		return render(request,'imageapp/image.html',{'cricketers':cricketers})

