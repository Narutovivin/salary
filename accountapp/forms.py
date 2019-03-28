from django import forms
from accountapp.models import salary
class salaryform(forms.Form):
  eid=forms.CharField()
  ename=forms.CharField()
  eaccountno=forms.IntegerField()
  ephoneno=forms.IntegerField()
  doj=forms.DateTimeField()
  email=models.EmailFiled()

class salaryModelForm(forms.ModelForm):
  class Meta:
    model=salary
    fields=('eid','ename','eaccountno','ephoneno','doj','email')
	
