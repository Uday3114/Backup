from django.shortcuts import render

# Create your views here.

def switzerland(request):
	msg = "Works in Switzerland"
	my_dict = {'msg':msg}

	return render(request,'countryapp/display2.html',context=my_dict)

def newzeland(request):
	msg = "Works in Newzeland"
	my_dict = {'msg':msg}

	return render(request,'countryapp/display2.html',context=my_dict)

