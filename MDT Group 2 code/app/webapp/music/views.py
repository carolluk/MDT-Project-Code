# Create your views here
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
import subprocess
import csv

def index(request):
     return render(request, 'index.html')

def hadoop(request):
     return render(request, 'hadoop.html')

def hadoop2(request):
     mydate = request.GET.get('date', '')
     mydate = str(mydate)
     probability=subprocess.check_output(["python","/home/rarcher/ImprovedScripts/myprocess.py","'"+mydate+"'"])

     template = loader.get_template("hadoop2.html")
     #probability=subprocess.check_output(["python", "/home/rarcher/ImprovedScripts/myprocess.py",str(mydate)])    

     context = RequestContext(request, {
          'Probability1': probability[0],
          'Probability2': probability[1],
          'Probability3': probability[2],
     })
     return HttpResponse(template.render(context))

def venn(request):
     return render(request, 'ven1.html')

def venn2(request):
     myinput = request.GET.get('phrase', '')
     myinputArray = myinput.split(" ")
     try:
          arg1=myinputArray[0]
     except:
          arg1 ="thiswillresultinnoresults"
     try:
          arg2=myinputArray[1]
     except:
          arg2 =""
     try:
          arg3=myinputArray[2]
     except:
          arg3 =""
     try:
          arg4=myinputArray[3]
     except:
          arg4 =""
     try:
          arg5=myinputArray[4]
     except:
          arg5 =""

     phrase = subprocess.check_output(["python", "/home/rarcher/ImprovedScripts/analysisVirt1.py",arg1,arg2,arg3,arg4,arg5])
     template = loader.get_template("ven2.html")
     context = RequestContext(request, {
           'phrase': phrase,
      })
     return HttpResponse(template.render(context))
