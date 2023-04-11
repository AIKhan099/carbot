import time

from django.shortcuts import render
from django.http import HttpResponse
from .models import Session
from . import carbotfun


# from django.http
# Create your views here.
def index(request):
    # request.session['session']=['bid check ended']
    # if 'session' not in request.session:
    #     request.session['session']=['bid check ended']
    #     print('session 2 : ', request.session['session'])
    #     return render(request, 'forms.html')
    # if 'session' in request.session and request.session['session'][0]=='bid check ended':
    #     print('session 3 : ', request.session['session'])
    #     return render(request, 'forms.html')
    # else:
    #     return HttpResponse("already bid check is undergoing")
    # return  render(request, 'forms.html')
    return render(request, 'forms.html')


def cars(request):
    res = carbotfun.carbot().findingtime()
    print(res)
    if res == 2:
        return HttpResponse('This page is not accessible')
    else:
        return HttpResponse('page is accessible')


def SessionsIdLists(request):
    SessionList = []
    session_id = request.session.session_key
    all_data2 = Session.objects.filter(session_id=session_id)
    for i in all_data2:
        print(i.session_id)
        SessionList.append(i.session_id)
    return SessionList


def formdata(request):
    print('In the form data ', '*' * 100)
    session_id = request.session.session_key

    if request.method == 'POST':

        # print("in form data now ", "session dic ", request.session['new-session'], " length is",
        #       len(request.session['new-session']))
        email = request.POST.get('email')
        password_ = request.POST.get('password')
        link_ = request.POST.get('link')
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))
        bid_price = int(request.POST.get('bid-price'))

        session_id_list = SessionsIdLists(request)
        print('Session list is : ', session_id_list, 'total count of session id is : ',
              session_id_list.count(session_id))
        print('Session list is : ', SessionsIdLists(request), 'total count of session id is : ',
              SessionsIdLists(request).count(session_id))

        # if 'email' not in request.session or request.session['email'] == 'empty':
        if 'email' in request.session:
            print('if statement, Within email', session_id, ' ', request.session.session_key, ' ',
                  request.session['email'])
            # if session_id == request.session.session_key and request.session['email'] == 'empty':
            if session_id not in session_id_list:
                print('Within if statement')
                request.session['email'] = email
                # request.session.modified = True
                print('session email 1 : ', request.session['email'])
                print(hours, minutes, 'bid price and type', bid_price, type(bid_price))
                print("waiting for time to be completed")
                print('Desired time is : ', minutes * 60 + hours * 60 * 60)
                # here change minutes*60 + hours*60*60, for time being to run faster we change it
                time.sleep(minutes * 60 + hours * 60 * 60)

                session_data = Session(session_id=request.session.session_key, session_status=request.session['email'])
                session_data.save()

                session_id_list = SessionsIdLists(request)
                print('Session list is : ', session_id_list, 'total count of session id is : ',
                      session_id_list.count(session_id))
                print('Session list is : ', SessionsIdLists(request), 'total count of session id is : ',
                      SessionsIdLists(request).count(session_id))

                try:

                    # calling the findingtime method
                    res, title, bid_value, bid_price, bid_price_is_greater = carbotfun.carbot(email=email,
                                                                                              password=password_,
                                                                                              link=link_,
                                                                                              bid_price=bid_price).findingtime()
                    print("In formdata function, res is", res, "title is ", title)

                    if res == 2:

                        bot_response = 'Auction has not been started for the requested page with title: \n' + title
                        response = render(request, 'response.html', {'bot_response': bot_response})
                        request.session['email'] = 'empty'
                        print('session email : ', request.session['email'])
                        # all_data = Session.objects.get(session_id = session_id)
                        print('*' * 100, 'all data is : ')
                        all_data2 = Session.objects.filter(session_id=session_id)
                        print('*' * 100, 'all data is : ', all_data2)
                        Session.objects.filter(session_id=session_id).delete()
                        return response

                    elif bid_price_is_greater:
                        request.session['email'] = 'empty'
                        # return HttpResponse(
                        #     'Auction has  been started for the requested page with title: \n' + title + ' \n Bid Value: ' + str(
                        #         bid_value) +
                        #     ' \n Bid Price by user :' + str(
                        #         bid_price) + " \n As requested bid by user is greater than bid price, bot has successfully participated.")

                        bot_response = 'Auction has  been started for the requested page with title: \n' + title + ' \n Bid Value: ' + str(
                            bid_value) + ' \n Bid Price by user :' + str(
                            bid_price) + " \n As requested bid by user is greater than bid price, bot has successfully participated."
                        response = render(request, 'response.html', {'bot_response': bot_response})
                        request.session['email'] = 'empty'
                        print('session email : ', request.session['email'])
                        # all_data = Session.objects.get(session_id = session_id)
                        print('*' * 100, 'all data is : ')
                        all_data2 = Session.objects.filter(session_id=session_id)
                        print('*' * 100, 'all data is : ', all_data2)
                        Session.objects.filter(session_id=session_id).delete()
                        return response

                    else:
                        request.session['email'] = 'empty'
                        # return HttpResponse(
                        #     "Bid value is less than what you have suggested." + ' Bid Value : ' + str(bid_value) +
                        #     ' Bid Price by user: ' + str(bid_price) + ". That's why, bot is unable to participate")
                        bot_response = "Bid value is less than what you have suggested." + ' Bid Value : ' + str(
                            bid_value) + ' Bid Price by user: ' + str(
                            bid_price) + ". That's why, bot is unable to participate"
                        response = render(request, 'response.html', {'bot_response': bot_response})
                        request.session['email'] = 'empty'
                        print('session email : ', request.session['email'])
                        # all_data = Session.objects.get(session_id = session_id)
                        print('*' * 100, 'all data is : ')
                        all_data2 = Session.objects.filter(session_id=session_id)
                        print('*' * 100, 'all data is : ', all_data2)
                        Session.objects.filter(session_id=session_id).delete()
                        return response
                except:
                    # xx = carbotfun.carbot(email=email, password=password_, link=link_).findingtime()
                    request.session['email'] = 'empty'
                    # return HttpResponse('In except, Action has not been started for the requested page with title: ')
                    bot_response = 'In except, Action has not been started for the requested page with title: '
                    response = render(request, 'response.html', {'bot_response': bot_response})
                    request.session['email'] = 'empty'
                    print('session email : ', request.session['email'])
                    # all_data = Session.objects.get(session_id = session_id)
                    print('*' * 100, 'all data is : ')
                    all_data2 = Session.objects.filter(session_id=session_id)
                    print('*' * 100, 'all data is : ', all_data2)
                    Session.objects.filter(session_id=session_id).delete()
                    return response
                # return HttpResponse('Hours and minutes are : '  )
            else:
                # bot_response = 'Session is already under process, wait untill the previous one is completed'
                # response = render(request, 'response.html', {'bot_response': bot_response})
                request.session['email'] = 'empty'
                return HttpResponse('You already have session. Let"s wait for that to be completed')
        else:
            request.session['email'] = 'empty'
            # return HttpResponse("First time")
            bot_response = 'This is the First Time you are at Car Bot. Kindly, go back and click submit again. '
            response = render(request, 'response.html', {'bot_response': bot_response})
            return response