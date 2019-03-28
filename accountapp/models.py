from django.db import models
from django.utils import timezone

# Create your models here.

class salary(models.Model):
	eid=models.CharField(max_length=4)
	ename=models.CharField(max_length=20)
	eaccountno=models.IntegerField(max_length=20)
	ephoneno=models.IntegerField(max_length=20)
	doj=models.DateTimeField(default=timezone.now())
	email=models.EmailField(max_length=40, verbose_name='email',default='abcd@gmail.com')
	def __str__(self):
		return self.ename	
	
