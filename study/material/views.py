from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request,'index.html')



def Djangoform(request):
    form = DjangoModelForm
    Djangoform = {'form':form}

    if request.method == 'POST':
        form = DjangoModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Djangomain')
    return render(request,'django-form.html',Djangoform)

def Djangomain(request):
    djangos = Django.objects.all()
    context = {'djangos':djangos}
    return render(request,'django-main.html',context)




def Jsonform(request):
    form = JsonModelForm
    Jsonform = {'form':form}

    if request.method == 'POST':
        form = JsonModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Jsonmain')
    return render(request,'json-form.html',Jsonform)

def Jsonmain(request):
    jsons = Json.objects.all()
    context = {'jsons':jsons}
    return render(request,'json-main.html',context)




def Restform(request):
    form = RestModelForm
    Restform = {'form':form}

    if request.method == 'POST':
        form = RestModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Restmain')
    return render(request,'rest-form.html',Restform)

def Restmain(request):
    rests = Rest.objects.all()
    context = {'rests':rests}
    return render(request,'rest-main.html',context)





def Htmlform(request):
    form = HtmlModelForm
    Htmlform = {'form':form}

    if request.method == 'POST':
        form = HtmlModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Htmlmain')
    return render(request,'html-form.html',Htmlform)

def Htmlmain(request):
    htmls = Html.objects.all()
    context = {'htmls':htmls}
    return render(request,'html-main.html',context)





def Cssform(request):
    form = CssModelForm
    Cssform = {'form':form}

    if request.method == 'POST':
        form = CssModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Cssmain')
    return render(request,'css-form.html',Cssform)

def Cssmain(request):
    csss = Css.objects.all()
    context = {'csss':csss}
    return render(request,'css-main.html',context)





def Bootstrapform(request):
    form = BootstrapModelForm
    Bootstrapform = {'form':form}

    if request.method == 'POST':
        form = BootstrapModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Bootstrapmain')
    return render(request,'bootstrap-form.html',Bootstrapform)

def Bootstrapmain(request):
    bootstraps = Bootstrap.objects.all()
    context = {'bootstraps':bootstraps}
    return render(request,'bootstrap-main.html',context)





def Pythonform(request):
    form = PythonModelForm
    Pythonform = {'form':form}

    if request.method == 'POST':
        form = PythonModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Pythonmain')
    return render(request,'python-form.html',Pythonform)

def Pythonmain(request):
    pythons = Python.objects.all()
    context = {'pythons':pythons}
    return render(request,'python-main.html',context)





def Jsform(request):
    form = JsModelForm
    Jsform = {'form':form}

    if request.method == 'POST':
        form = JsModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Jsmain')
    return render(request,'js-form.html',Jsform)

def Jsmain(request):
    jss = Js.objects.all()
    context = {'jss':jss}
    return render(request,'js-main.html',context)
