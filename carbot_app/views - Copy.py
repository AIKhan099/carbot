import time

from django.shortcuts import render
from django.http import HttpResponse
# import carbotfun
from . import carbotfun


# from django.http
# Create your views here.
def index(request):
    req = str(request.COOKIES.get('session'))
    print('the cookie is : ', req)
    if req == 'end_session':

        response = render(request, 'forms.html')
        response.set_cookie('session', 'session_going')
        print('oth time in .............')
        return response

    elif 'session' not in request.session:

        request.session['session'] = []
        response = render(request, 'forms.html')
        response.set_cookie('session', 'first_time')
        print('First time in .............')
        return response

    elif 'session' in request.session and request.COOKIES.get('session') == 'first_time':

        request.session['session'] = []
        response = render(request, 'forms.html')
        response.set_cookie('session', 'first_time')
        print('2nd time in .............')
        return response
    # just to manage, if it stuck in session going
    # elif 'session' in request.session and request.COOKIES.get('session') == 'session_going':
    #
    #     request.session['session'] = []
    #     response = render(request, 'forms.html')
    #     response.set_cookie('session', 'first_time')
    #     print('2nd time in .............')
    #     return response
    else:
        return HttpResponse('Session is underway already')
    # elif request.COOKIES.get('session') == 'session_going' or request.COOKIES.get('session') == 'first_time':
    #
    #     bot_response = 'Session has already been launched. If you haven"t, please delete cookies for our home page '
    #     response = render(request, 'response.html', {'bot_response':bot_response})
    #
    #     return response
def get(request):
    cookie = request.COOKIES.get('session')
    return HttpResponse("Cookie is : " + str(cookie))


def delete(request):
    response = render(request, 'forms.html')
    # response = HttpResponse("Cookie is : ")
    response.delete_cookie('session')
    return response


def cars(request):
    res = carbotfun.carbot().findingtime()
    print(res)
    if res == 2:
        return HttpResponse('This page is not accessible')
    else:
        return HttpResponse('page is accessible')


def formdata(request):
    cookie = request.COOKIES.get('session')
    print(cookie)
    if request.method == 'POST' and cookie == 'session_going' or cookie == 'first_time':
        request.session['new-session'] = [1]
        print("in form data now ", "session dic ", request.session['new-session'], " length is",
              len(request.session['new-session']))
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
                print('Where u mentioned end_session')
                bot_response = 'Auction has not been started for the requested page with title: \n' + title
                response = render(request, 'response.html', {'bot_response': bot_response})
                response.set_cookie('session', 'end_session')
                # return HttpResponse('Auction has not been started for the requested page with title: \n' + title)
                return response

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
    else:
        bot_response = 'Session is already under process, wait untill the previous one is completed'
        response = render(request, 'response.html', {'bot_response': bot_response})

        return response
