import selenium
import webdriver_manager
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
from selenium import webdriver
import json
from django.templatetags.static import static
from pathlib import Path
from django.http.response import HttpResponse
from . import views
class carbot():
    def __init__(self, email, password, link, bid_price):
        self.email = email
        self.password = password
        self.bid_price = bid_price
        self.link = link
        self.getbrowser()
        self.login()
        self.desired_car_page()
        # self.card_info()
        #self.biding()
        # self.findingtime()

        # self.gettingAllDealers()
        # self.clickOnDealer(toclick)

    def joinerLower(self, str_):
        joined = ''.join(str_.split(' '))
        lowerJoined = joined.lower()

        return lowerJoined

    def cred_all(self):
        # path_=Path(__file__).parents[1] + '\static\credentials.json'
        path_ = str(Path(__file__).parents[1]) + '\static\credentials.json'
        # cred_json = json.load(path_)

        credentials = open(path_)
        cred_json = json.load(credentials)
        return cred_json['email'], cred_json['password'], cred_json['car_page']

    def getbrowser(self):
        print("getting browser")
        # options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--incognito")
        options.add_argument("--nogpu")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280,1280")
        options.add_argument("--no-sandbox")
        options.add_argument("--enable-javascript")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')

        # self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options )
        self.browser = webdriver.Chrome(options=options )
        try:
            self.browser.get('https://cars.bidspirit.com/ui/home?lang=en')
            time.sleep(10)
            self.browser.maximize_window()
            print("visited to website")
        except:
            self.browser.quit()

    def login(self):
        # getting credentials
        # email, password, _ = self.cred_all()


        # print(email, password)
        try:
            # clicking on login
            print("started login procedure")
            login = self.browser.execute_script('return document.getElementsByClassName("text ng-binding")[0];')
            self.browser.execute_script('arguments[0].click()', login)
            time.sleep(5)
            # self.email = self.email
            # self.password = self.password

            # entering value at username
            # self.browser.execute_script('document.getElementsByName("email")[0].value="{}";'.format(email))
            self.browser.find_element(By.XPATH, '//input[@name="email"]').send_keys(self.email)
            # time.sleep(5)

            # entering value at password
            # self.browser.execute_script('document.getElementById("loginPasswordInput").value="{}";'.format(password))
            self.browser.find_element(By.ID, 'loginPasswordInput').send_keys(self.password)
            # time.sleep(5)

            # clicking on submit button
            submit = self.browser.execute_script('return document.getElementsByClassName("text ng-binding")[2];')
            self.browser.execute_script('arguments[0].click()', submit)
            # time.sleep(5)
            print("login procedure is executed")
        except:
            self.browser.quit()

    def redirection_to_live(self):
        try:
            time.sleep(5)
            print("in redirect to live now")
            try:
                print("2nd try")
                live_auc= self.browser.execute_script('return document.getElementsByClassName("btn btn-primary");')
                self.browser.execute_script('arguments[0].click()',live_auc)

                time.sleep(10)
                self.browser.switch_to_window(self.browser.window_handles[1])
            except:
                print("2nd try except")
                # self.browser.get(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/div/button[1]").click()
                # self.browser.switch_to.frame(self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/button[1]").click())
                self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/button[1]").click()
                time.sleep(3)
                self.browser.switch_to.window(self.browser.window_handles[1])
                time.sleep(20)
                # self.browser.switch_to.window(self.browser.window_handles[1])
        except:
            print("In exception of redirect")
            # pass

    def ID_check(self):
        # try:
        print("in the id  check")
        time.sleep(5)
        id1 = self.browser.find_element(By.XPATH,'(//div[@class="picContainer "]/div[@class="pic"])[2]')
        print("String contains ID is: ", id1)
        id2 = id1.get_attribute("style")
        print("String contains ID is:", id2)
        all_ids= self.browser.find_elements(By.XPATH,'//div[@class="item "]')
        print("Here are all the ids", all_ids)
        all_ids1=all_ids.get_attribute("itemid")

        print("Here is all ids ", all_ids1)


        if '17573' in str(id2):
            print("Yes, it is in that.")

        # except:
        #     pass
    def desired_car_page(self):
        try:
            print("going to desired car page")
            # _, _, car_page = self.cred_all()
            car_page=self.link
            self.browser.get(car_page)
            time.sleep(20)
            print("on to desired car page")
            self.redirection_to_live()
            # self.ID_check()
        except:
            print("unable to reach desired car page")
            self.browser.quit()
            print("browser quit")

    def biding(self):
        print("In bidding nows")
        # clicking the bid price
        self.browser.find_element(By.XPATH, '//div[@class="price text"]').click()
        time.sleep(3)
        self.browser.find_element(By.XPATH,"//div[contains(text(), 'I Agree')]").click()
        time.sleep(5)
        print('clicked on bidding')
    def pricevaluemaker(self, raw_price_str):
        list_=list_= [i for i in raw_price_str if i.isdigit()]
        price = int("".join(list_))

        return price

    def findingtime(self):
        # time_ = self.browser.find_element(By.XPATH, "//div[@class='timer']").text
        # print(time_)
    #     document.getElementsByClassName("circleTimer")['item']
        try:
            print("In finding time function now")
            time.sleep(10)
            getting_value=0
            while getting_value <5:
                try:
                    print("trying to get value : ", getting_value)
                    sub=self.browser.execute_script("document.getElementsByClassName('mainCurrency')[0].textContent");
                    print("This is sub : ",  sub)
                    # if currency is mentioned
                    if sub:
                        # as we have currency, no need for while loop anymore
                        getting_value =5

                        # extracting price and converting to int
                        bid_value = self.pricevaluemaker(sub)
                        # comparing mentioned bid on website with the bid price by user
                        if bid_value <= self.bid_price:
                            # clicking on bid price
                            self.biding()
                            bid_price_is_greater = True
                        else:
                            bid_price_is_greater = False

                    else:
                        sub = self.browser.find_element(By.XPATH,'//div[@class="mainCurrency"]').text
                        print("This is sub in else: ", sub)
                        # if currency is mentioned
                        if sub:
                            # as we have currency, no need for while loop anymore
                            getting_value = 5
                            # extracting price and converting to int
                            bid_value = self.pricevaluemaker(sub)
                            # comparing mentioned bid on website with the bid price by user
                            if bid_value <= self.bid_price:
                                # clicking on bid price
                                self.biding()
                                bid_price_is_greater = True
                            else:
                                bid_price_is_greater = False


                        getting_value = getting_value + 1

                except:
                    getting_value = getting_value+1
                    bid_value=0
                    bid_price_is_greater = False



            print( "bid value is : ", bid_value, "type is",type(bid_value))
            page=1
            title_ = self.browser.title
            print("found title is ", title_)
            if sub:
                print('Auction has been started')
                self.browser.quit()
                return page, title_, bid_value, self.bid_price, bid_price_is_greater
            else:
                print('Auction is not started ')
                title_ = self.browser.title
                page = 2
                self.browser.quit()
                return page, title_,bid_value, self.bid_price, bid_price_is_greater


        except:
            print('In exception of finding time')
            title_ = self.browser.title
            page=2
            self.browser.quit()
            return page, title_, bid_value, self.bid_price, bid_price_is_greater




    def card_info(self):
        # CLICK TO PARTICIPATE
        participate = self.browser.execute_script('return document.getElementsByClassName("text ng-binding")[5];')
        self.browser.execute_script('arguments[0].click()', participate)
        time.sleep(10)

        # radio
        radio = self.browser.execute_script('return document.getElementsByClassName("float ng-pristine ng-untouched ng-valid ng-empty")[0];')
        self.browser.execute_script('arguments[0].click()',radio)
        time.sleep(10)

        self.browser.find_element(By.XPATH, '//input[@id=txtCardNumber"]').send_keys('iii')
        # ok
        ok = self.browser.execute_script(
            'return document.getElementsByClassName("btn btn-primary")[0];')
        self.browser.execute_script('arguments[0].click()', ok)



        # pass



    def gettingAllDealers(self):
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # # browser.get('https://cars.bidspirit.com/ui/home?lang=en')
        # self.browser.maximize_window()

        self.browser.get('https://cars.bidspirit.com/ui/home?lang=en')
        time.sleep(5)
        all_dealers = self.browser.execute_script('return document.getElementsByClassName("ng-binding ng-scope");')
        print(all_dealers)
        self.list_dealers = []

        for i in range(len(all_dealers)):
            every_dealer = self.browser.execute_script(
                "return document.getElementsByClassName('ng-binding ng-scope')[{}].textContent;".format(i))
            self.list_dealers.append(self.joinerLower(every_dealer))

        return self.list_dealers

    def clickOnDealer(self, to_click):
        to_click_lower = self.joinerLower(to_click)
        print(to_click_lower)
        desired_dealer = self.list_dealers.index(to_click_lower)
        print(to_click_lower, desired_dealer)
        # time.sleep(5)
        one = self.browser.execute_script(
            "return document.getElementsByClassName('ng-binding ng-scope')[{}];".format(desired_dealer))
        self.browser.execute_script('arguments[0].click()', one)
        time.sleep(15)
        print(one)


# carbot()
# time.sleep(10)
# browser.close()
