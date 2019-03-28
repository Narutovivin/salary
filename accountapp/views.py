from django.shortcuts import render
from accountapp.models import salary
from accountapp.forms import salaryform
from accountapp.forms import salaryModelForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


# Create your views here.
       
        
def ShowsalaryDetails(request):         
	records=salary.objects.all()
	return render(request,'account.html',{'rec':records})

def sform(request):

 if request.method =='POST':
                form=salaryforms(request.POST)
                if form.is_valid():
                 eid=forms.cleaned_data['eid']
                 ename=form.cleaned_data['ename']
                 eaccountno=form.cleaned_data['accountno']
                 ephoneno=form.cleaned_data['ephoneno']
                 doj=form.cleaned_data['doj']
                 email=form.cleaned_data['e-mail']
                print(eid,ename,eaccountno,ephoneno,doj,email)
 form=salaryform()
 return render(request,'manage.html',{'form':form})
def GetsformDetails(request):

 if request.method =='POST':
                form=salaryModelForm(request.POST)
                if form.is_valid():
                   form.save()
                return HttpResponseRedirect("http://127.0.0.1:8000")   
                   
 form=salaryModelForm()
 return render(request,'manage.html',{'form':form})

def sendmail(request):
   send_mail('hi vivin','interview','itsvivin95@gmail.com',['ss0911814@gmail.com'],fail_silently = False)
   return render(request,'index.html')
