from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
from Xidmetler.models import *
from Anasahifa.models import home,description,Selector,Social
from Komanda.models import Komanda,Chart
from iş.models import Ugur,hesabat,Manager
from Anlayışlar.models import Maqala,Result,Members
from django.core.mail import send_mail
from .forms import contactusForm,subscribForm
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/admin/')  

        else: 
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request,'admin.login.html')




def Home(request):
    
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
           
    social = Social.objects.all()
    first = home.objects.first()
    all = home.objects.filter(status="p")[1:]
    descrip1 = description.objects.get(id=1)
    descrip2 = description.objects.get(id=2)
    selctor = Selector.objects.all()
        
    return render(request,'index.html',{'first':first,'all':all,'descript1':descrip1,'descript2':descrip2,
     'selector':selctor,'social':social})


    '''
    send = False
    if request.method == 'POST':
        form = subscribForm(request.POST)
        name ='subscrib'
        en = subscribForm(name=name)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['en']
            email = cd['Email']
            msg = "Ad:    {0}\nE-mail:     {1}".format(email)
            send_mail(email, 'mohammadharoonmozafary@gmail.com',['rasikh75k@gmail.com'], fail_silently=False)
            send = True
            return render(request, 'subscrib.html', {'form': form, 'send': send})

    form = contactusForm
    return render(request, 'subscrib.html', {'form': form})
'''


def about(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect("/",{'error':error_message})
    
    about = About.objects.all()
    team = about1.objects.all()
    selctor = Selector.objects.all()
    
    social = Social.objects.all()

    return render(request,'hakkinda.html',{'about':about,'team':team,'selector':selctor,'social':social})



def Service(request):    
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
        
    title1 = title.objects.get(id=1)
    title2 = title.objects.get(id=2)
    title3 = title.objects.get(id=3)
    servc = service1.objects.all()

    all = home.objects.filter(status="p")[1:]
    servc2 = service2.objects.get(id=7)
    servc2a = service2.objects.get(id=8)
    servc2b = service2.objects.get(id=9)
    servc2c = service2.objects.get(id=10)
    servclast = service2.objects.last()

    servc3 = service3.objects.get(id=1)
    servc3a = service3.objects.get(id=2)
    servc3b = service3.objects.get(id=3)
    servc3c = service3.objects.get(id=4)
 #   servclast1 = service3.objects.filter(id=5, status="p")
    servclast1 = service3.objects.last()

    servc4 = service4.objects.get(id=1)
    servc4a = service4.objects.get(id=2)
    servc4b = service4.objects.get(id=3)
    servc4c = service4.objects.get(id=4)
    servclast2 = service4.objects.last()
    selctor = Selector.objects.all()
    social = Social.objects.all()
   
    context = {'servc':servc,'servc2':servc2,'servc2a':servc2a,'servc2b':servc2b,'servc2c':servc2c,'servclast':servclast,
               'title1':title1,'title2':title2,'title3':title3,
               'servc3':servc3,'servc3a':servc3a,'servc3b':servc3b,'servc3c':servc3c,'servclast1':servclast1,
               'servc4': servc4,'servc4a': servc4a, 'servc4b': servc4b, 'servc4c': servc4c,'servclast2': servclast2,
               'selector':selctor,'social':social}

    return render(request,'xidmetler.html',context)

def Work(request):
    selctor = Selector.objects.all()
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    ugur = Ugur.objects.all()
    hesab = hesabat.objects.all()
    social = Social.objects.all()
    return render(request,'ish.html',{'ugur':ugur,'hesab':hesab,'social':social,'selector':selctor})
    
def ugur(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
        
    selctor = Selector.objects.all()
    social = Social.objects.all()
    hekaye = Ugur.objects.all()

    return render(request,'ugurlar.html',{'ugur':hekaye,'social':social,'selector':selctor})


def Ugurapost(request, pk):
    selctor = Selector.objects.all()
    social = Social.objects.all()
    heykaye = Ugur.objects.get(id=pk)
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    manager= Manager.objects.all()
       
    return render(request, 'ish2.html', {'posts': heykaye,'selector':selctor,'social':social,'manager':manager})


def contact(request):
    send = False
    if request.method == 'POST':
        form = contactusForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ad = 'İŞ'
            name = cd['Name']
            email = cd['Email']
            message = cd['Message']
            msg = "Ad:    {0}\nE-mail:     {1}\nMesaj:   {2}\n".format(name,email,message)
            send_mail(ad,msg,'mohammadharoonmozafary@gmail.com', ['mohammadharoonmozafary@gmail.com','rasikh75k@gmail.com'], fail_silently=False)
            send = True
            return render(request, 'teshekkur.html', {'form': form, 'send': send})







def hesab(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})

    selctor = Selector.objects.all()
    social = Social.objects.all()
    hesb = hesabat.objects.all()
    return render(request,'hesabatlar.ish.html',{'hesabat':hesb,'social':social,'selector':selctor})

def Hesabpost(request, pk): 
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    hesab = hesabat.objects.get(id=pk)
    manager= Manager.objects.all()
    social = Social.objects.all()
    selctor = Selector.objects.all()

    return render(request, 'hesabatlar2.html', {'posts': hesab,'manager':manager,'social':social,
    
    'selector':selctor})




def agreement(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
        
    selctor = Selector.objects.all()
    social = Social.objects.all()
    article = Maqala.objects.all()
    result= Result.objects.all()


    return render(request,'anlayis.html',{'article':article,'result':result,'social':social,'selector':selctor})

def maqala(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})

    social = Social.objects.all()
    selctor = Selector.objects.all()
    meqal = Maqala.objects.all()
    return render(request, 'meqale.html',{'meqale':meqal,'selector':selctor,'social':social})

def maqalapost(request, pk):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    selctor = Selector.objects.all()
    social = Social.objects.all()
    posts = Maqala.objects.get(id=pk)
    member = Members.objects.all()
    return render(request, 'anlayis2.html', {'posts': posts,'member':member,'social':social,'selector':selctor})






def resource (request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})


    social = Social.objects.all()
    selctor = Selector.objects.all()
    resourc = Result.objects.all()
    return render(request,'resurs.html',{'resource':resourc,'selector':selctor,'social':social})

def resurspost(request, pk):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    social = Social.objects.all()
    selctor = Selector.objects.all()
    resurs = Result.objects.get(id=pk)
    member = Members.objects.all()
    return render(request, 'resurs2.html', {'posts': resurs,'social':social,'selector':selctor,'member':member})






def komanda(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    social = Social.objects.all()
    kmnda = Komanda.objects.all()
    chrt = Chart.objects.all()
    selctor = Selector.objects.all()

    return render(request,'komandamiz.html',{'komanda': kmnda,'chart':chrt,'selector':selctor,'social':social})


def komandapost(request, pk):
    selctor = Selector.objects.all()
    social = Social.objects.all()
    chrt = Chart.objects.get(id=pk)
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    return render(request, 'komandamiz2.html', {'posts': chrt,'social':social,'selector':selctor})




def alaqa(request):
    if request.method == 'POST':
        email = request.POST['Email']
        error_message =None
        if (not email):
            error_message = "please type your email"
        if not error_message:
            email = request.POST['Email']
            send_mail('SUBSCRIBE', email, settings.EMAIL_HOST_USER, ['mohammadharoonmozafary@gmail.com'],
                  fail_silently=False)
        else:
            return redirect('/',{'error':error_message})
    social = Social.objects.all()
    send = False
    if request.method == 'POST':
        form = contactusForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ad = 'ƏLAQƏ'
            name = cd['Name']
            email = cd['Email']
            message = cd['Message']
            msg = "Ad:    {0}\nE-mail:     {1}\nMesaj:   {2}\n".format(name,email,message)
            send_mail(ad,msg,'mohammadharoonmozafary@gmail.com', ['mohammadharoonmozafary@gmail.com','rasikh75k@gmail.com'], fail_silently=False)
            send = True
            return render(request, 'elaqe.html', {'form': form, 'send': send})

    selctor = Selector.objects.all()
    form = contactusForm


    return render(request,'elaqe.html',{'form':form,'selector':selctor,'social':social})

