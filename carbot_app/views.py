import time

from django.shortcuts import render
from django.http import HttpResponse
# import carbotfun
from . import carbotfun


# from django.http
# Create your views here.
def index(request):
    # return HttpResponse('This is the carbot application')
    return render(request, 'forms.html')


def cars(request):
    res = carbotfun.carbot().findingtime()
    print(res)
    if res == 2:
        return HttpResponse('This page is not accessible')
    else:
        return HttpResponse('page is accessible')


def formdata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password_ = request.POST.get('password')
        link_ = request.POST.get('link')
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))
        print(hours, minutes )
        time.sleep(minutes*1 + hours*60*60)

        try:
            res, title=carbotfun.carbot(email=email, password=password_,link=link_).findingtime()
            print("In formdata function, res is", res,"title is ", title)
            if res == 2:
                return HttpResponse('Auction has not been started for the requested page with title: ' + title)
            else:
                return HttpResponse('Auction has  been started for the requested page with title:' + title)
        except:
            xx=carbotfun.carbot(email=email, password=password_,link=link_).findingtime()
            return HttpResponse('In except, Action has not been started for the requested page with title: '+xx)

        # return HttpResponse('Hours and minutes are : '  )
