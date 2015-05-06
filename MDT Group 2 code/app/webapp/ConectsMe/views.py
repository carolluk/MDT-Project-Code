# Create your views here
from django.shortcuts import render, render_to_response
from PRICD.models import SupportedDevices, TempUsers
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
     return render(request, 'index.html')

def test(request):
     return render(request, 'index1.html')

def home(request):
     return render(request, 'home.html')

def conected(request):
     return render(request, 'aboutconnected.html')

def about(request):
     return render(request, 'about.html')

def team(request):
     return render(request, "team.html")

def pTest(request, someid):
     return HttpResponse("This is a test,you passed the parameter %s." % someid) 

def login(request):
     return render(request, "login.html")

def signup(request):
     return render(request, "signup.html")

def adduser(request):
     currentUser = request.GET.get('username')
     mypass = request.GET.get('passw')
     newuser = TempUsers(username=currentUser,passw=mypass)
     newuser.save()
     return HttpResponseRedirect("../about")

def logsucess(request):
     currentUser = request.GET.get('username') 
     mypass = request.GET.get('passw')
     allusers = TempUsers.objects.all()
     allList = allusers.values_list()
     for user in allList:
          if(user[1]==currentUser):
               if(user[2]==mypass):
                    return HttpResponseRedirect("../about")
               else:
                    return HttpResponseRedirect("../failedlogin")
     return HttpResponseRedirect("../login")
     #u = TempUsers(username=currentUser,passw=mypass)
     #u.save()
     #return HttpResponseRedirect("../about")

def failedlogin(request):
     return render(request,"failedlogin.html")
     
def devices(request):
	devices = SupportedDevices.objects.all()
	template = loader.get_template('devices.html')
	context = RequestContext(request, {
		'devices_list': devices,
	})
	return HttpResponse(template.render(context))
	#output  = ','.join([p.device_text for p in devices])
	#return render(output)
