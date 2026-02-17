from django.shortcuts import render

from b_courses .models import *

# Create your views here.

def course_detail(request):
    queryset=Video.objects.all()
    context={'videos':queryset}

    return render(request,'course_detail.html',context)

def layout(request):
    return render(request,'layout.html')