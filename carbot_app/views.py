import time

from django.shortcuts import render
from django.http import HttpResponse
# import carbotfun
from . import carbotfun


# from django.http
# Create your views here.
def index(request):
    if 'new-session' not in request.session:
        request.session['new-session']=[]

    # return HttpResponse('This is the carbot application')
        return render(request, 'forms.html')
    return HttpResponse("You are already in session")


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
        bid_price = int(request.POST.get('bid-price'))
        print(hours, minutes, 'bid price and type', bid_price, type(bid_price))
        print("waiting for time to be completed")
        print('Desired time is : ', minutes * 60 + hours * 60 * 60)
        # here change minutes*60 + hours*60*60, for time being to run faster we change it
        time.sleep(minutes * 60 + hours * 60 * 60)


        try:
            # calling the findingtime method
            res, title, bid_value, bid_price, bid_price_is_greater = carbotfun.carbot(email=email, password=password_,
                                                                                      link=link_,
                                                                                      bid_price=bid_price).findingtime()
            print("In formdata function, res is", res, "title is ", title)

            if res == 2:
                return HttpResponse('Auction has not been started for the requested page with title: \n' + title)
            elif bid_price_is_greater:
                return HttpResponse(
                    'Auction has  been started for the requested page with title: \n' + title + ' \n Bid Value: ' + str(
                        bid_value) +
                    ' \n Bid Price by user :' + str(
                        bid_price) + " \n As requested bid by user is greater than bid price, bot has successfully participated.")
            else:
                return HttpResponse(
                    "Bid value is less than what you have suggested." + ' Bid Value : ' + str(bid_value) +
                    ' Bid Price by user: ' + str(bid_price) + ". That's why, bot is unable to participate")
        except:
            xx = carbotfun.carbot(email=email, password=password_, link=link_).findingtime()
            return HttpResponse('In except, Action has not been started for the requested page with title: ' + xx)

        # return HttpResponse('Hours and minutes are : '  )
