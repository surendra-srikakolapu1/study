from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [

    path('',views.index,name="index"),

    path('Djangoform/',views.Djangoform,name="Djangoform"),
    path('Djangomain/',views.Djangomain,name="Djangomain"),

    path('Jsonform/',views.Jsonform,name="Jsonform"),
    path('Jsonmain/',views.Jsonmain,name="Jsonmain"),

    path('Restform/',views.Restform,name="Restform"),
    path('Restmain/',views.Restmain,name="Restmain"),

    path('Htmlform/',views.Htmlform,name="Htmlform"),
    path('Htmlmain/',views.Htmlmain,name="Htmlmain"),

    path('Cssform/',views.Cssform,name="Cssform"),
    path('Cssmain/',views.Cssmain,name="Cssmain"),

    path('Bootstrapform/',views.Bootstrapform,name="Bootstrapform"),
    path('Bootstrapmain/',views.Bootstrapmain,name="Bootstrapmain"),

    path('Pythonform/',views.Pythonform,name="Pythonform"),
    path('Pythonmain/',views.Pythonmain,name="Pythonmain"),

    path('Jsform/',views.Jsform,name="Jsform"),
    path('Jsmain/',views.Jsmain,name="Jsmain"),
]
