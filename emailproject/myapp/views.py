from django.shortcuts import render
from emailproject import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method=="POST":
        to=request.POST['to']
        subject=request.POST['subject']
        body=request.POST['body']
        sender=settings.EMAIL_HOST_USER
        send_mail(subject,body,sender,[to])
        return HttpResponse("<h1> Please check the mail </h1>"+to)
    return render(request,'home.html')
