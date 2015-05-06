# Create your views here
import urllib2, httplib, oauth2
import RichFunction
import requests, json
from django.shortcuts import render, render_to_response
from PRICD.models import SupportedDevices, TempUsers, UserCodes, UserCodesFit
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
     return render(request, 'index.html')

def test(request):
     return render(request, 'index1.html')

def home(request):
     return render(request, 'home.html')

def fitbit(request):
     #z = RichFunction.fitbit.Fitbit()
     #auth_url, auth_token = z.GetRequestToken()
     myusername = request.user.username
     auth_token = UserCodesFit.objects.get(username=myusername).mytoken
     token = request.GET.get('oauth_token', '')
     oauth_verifier= request.GET.get('oauth_verifier', '')
     connection=httplib.HTTPSConnection('api.fitbit.com')
     consumer = oauth2.Consumer('83ca2257101b5cd7714256b599a3d8cf', 'b7e3d96976abaf196537b553ed932a8e')
     signmethod = oauth2.SignatureMethod_PLAINTEXT()
     oauth_request = oauth2.Request.from_consumer_and_token(consumer, token=auth_token, http_url="http://api.fitibt.com/oauth/access_token", parameters={'oauth_verifier': oauth_verifier})
     oauth_request.sign_request(signmethod, consumer, auth_token)
     connection.request(oauth_request.method, "http://api.fitbit.com/oauth/access_token", headers=oauth_request.to_header())
     resp = connection.getresponse()
     s = resp.read()
     access_token = s
     #myusername = request.user.username
     try:
          oldcode = UserCodesFit.objects.get(username=myusername).delete()
     except:
          oldcode="donothing"

     #newcode = UserCodesFit(username=myusername, mycode=access_token)
     #newcode.save()
     return HttpResponse(str(auth_token) + str(oauth_verifier) + s)

def conected(request):
     myc = request.GET.get('code', '')
     myusername = request.user.username
     try:
          oldcode = UserCodesFit.objects.get(username=myusername).delete()
     except:
          oldcode="donothing"

     newcode = UserCodesFit(username=myusername, mycode=finalresult)
     newcode.save()
     #return HttpResponse("token "+finalresult)
     return HttpResponseRedirect("../success")
     
     url="https://jawbone.com/auth/oauth2/token/?code="+myc+"&client_id=GnHK7CopBDI"+"&client_secret=a45718af2e59e61731e023bdb029038fc87849ff"+"&grant_type=authorization_code"
     myresult = urllib2.urlopen(url)
     myresults = myresult.read()
     finalresult = myresults.split(":")[1].split(",")[0].replace(" ","").replace('"',"")
     try:
          oldcode = UserCodes.objects.get(username=myusername).delete()
     except:
          oldcode="donothing"

     newcode = UserCodes(username=myusername, mycode=finalresult)
     newcode.save()
     #return HttpResponse("token "+finalresult)
     return HttpResponseRedirect("../success")

def checkSess(request):
     if request.user.is_authenticated():
          return HttpResponse("Session success")
     else:
          return HttpResponse("Session Fail")

def someData(request):
     myusername = request.user.username
     token = UserCodes.objects.get(username=myusername).mycode
     headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer '+token, 'Accept': 'application/json'}
     url = "https://jawbone.com/nudge/api/v.1.1/users/@me"
     r = requests.get(url,headers=headers)
     rr = r.text
     return HttpResponse(rr)

def about(request):
     return render(request, 'about.html')

def team(request):
     return render(request, "team.html")

def pTest(request, someid):
     return HttpResponse("This is a test,you passed the parameter %s." % someid) 

def loginme(request):
     return render(request, "login.html")

def signup(request):
     return render(request, "signup.html")

def adduser(request):
     currentUser = request.GET.get('username')
     mypass = request.GET.get('passw')
     user = User.objects.create_user(username=currentUser,password=mypass)
     user.save()
     return HttpResponseRedirect("../success")

def logsucess(request):
     currentUser = request.GET.get('username') 
     mypass = request.GET.get('passw')
     user = authenticate(username=currentUser, password=mypass)
     if user is not None:
          if user.is_active:
               login(request,user)
               return HttpResponseRedirect("../success")
          else:
               return HttpResponse("Password valid user disabled")
     else:
          return HttpResponseRedirect("../login")
     #allusers = TempUsers.objects.all()
     

def success(request):
     #z = RichFunction.fitbit.Fitbit()
     #auth_url, auth_token = z.GetRequestToken()

     if request.user.is_authenticated():
          myusername=request.user.username
          try:
               #auth_token = UserCodesFit.objects.gets(username=myusername).mytoken
               auth_url =  UserCodesFit.objects.gets(username=myusername).url
               if(auth_url == None):
                    z = RichFunction.fitbit.Fitbit()
                    auth_url, auth_token = z.GetRequestToken()
                    newcode = UserCodesFit(username=myusername, url=auth_url, mytoken=auth_token)
                    newcode.save()           
               else:
                    auth_url = auth_url
          except:
               z = RichFunction.fitbit.Fitbit()
               auth_url, auth_token = z.GetRequestToken()
               newcode = UserCodesFit(username=myusername, url=auth_url, mytoken=auth_token)
               newcode.save()
          
          template = loader.get_template("registered.html")
          try:
               token = UserCodes.objects.get(username=myusername).mycode
               headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer '+token, 'Accept': 'application/json'}
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me"
               r = requests.get(url,headers=headers)
               rr = r.text
               hindex = rr.find("height")
               myheight= rr[hindex:len(rr)].split(",")[0].split(":")[1].replace(" ","").replace("}", "").replace('"',"").replace("null", "Not Entered Yet")
               windex = rr.find("weight")
               myweight= rr[windex:len(rr)].split(",")[0].split(":")[1].replace(" ","").replace("}", "").replace('"',"").replace("null", "Not Entered Yet")
               findex = rr.find("first")
               myfirst = rr[findex:len(rr)].split(",")[0].split(":")[1].replace(" ","").replace("}","").replace('"',"")
               lindex = rr.find("last")
               mylast = rr[lindex:len(rr)].split(",")[0].split(":")[1].replace(" ","").replace("}", "").replace('"',"").replace("null", "Not Entered Yet")
               #API Call One done
               #API Call Two
               #url = "https://jawbone.com/nudge/api/v.1.1/users/@me/body_events"
               #r = requests.get(url,headers=headers)
               #rr = r.text
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me/moves"
               r = requests.get(url,headers=headers)
               moves = json.loads(r.text)
               mymoves = moves['data']['items']
               steps=[]
               mykm = []
               calories=[]
               time_active=[]
               moves_date=[]
               for mov in mymoves:
                    steps.append(mov['details']['steps'])
                    mykm.append(mov['details']['km'])
                    calories.append(mov['details']['calories'])
                    time_active.append(mov['details']['active_time'])
                    moves_date.append(mov['date'])
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me/goals"
               #r = requests.get(url,headers=headers)
               #rr = r.text          
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me/workouts"
               #r = requests.get(url,headers=headers)
               #rr = r.text
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me/mood"
               #r = requests.get(url,headers=headers)
               #rr = r.text
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me/trends"
               #r = requests.get(url,headers=headers)
               #rr = r.text
               url = "https://jawbone.com/nudge/api/v.1.1/users/@me/sleeps"
               r = requests.get(url,headers=headers)
               rr = r.text
               sleeps = json.loads(r.text)
               sleepList = sleeps['data']['items']
               sleep_date=[]
               sleep_duration=[]
               for sli in sleepList:
                    sli['title']
                    sleep_duration.append(sli['details']['duration'])
                    temp = sli['date']
                    sleep_date.append(temp)
               #url = "https://jawbone.com/nudge/api/v.1.1/users/@me/workouts"
               #r = requests.get(url,headers=headers)
               #rr = r.text


               context = RequestContext(request, {
                     'firstname': myfirst,
                     'lastname': mylast,
                     'height': myheight,
                     'weight': myweight,
                     'sleepDuration': sleep_duration,
                     'sleepDate': sleep_date,
                     'steps': steps,
                     'mykm': mykm,
                     'calories': calories,
                     'time_active': time_active,
                     'moves_date': moves_date,
                     'auth_url': auth_url,
               })
               return HttpResponse(template.render(context))
          except:
               template = loader.get_template("registered.html")
               context = RequestContext(request,{
                    'auth_url': auth_url,
               })
               return HttpResponse(template.render(context))
     else:
          template = loader.get_template("registered.html")
          context = RequestContext(request,{
                'auth_url': auth_url,
          })
          return HttpResponse(template.render(context))

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
