from django.shortcuts import render

# Create your views here.
def css(request):

    return render(request,'css.html')


def home(request):
    return render(request,'index.html')