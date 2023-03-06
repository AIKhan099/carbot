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
    def __init__(self, email, password, link):
        self.email = email
        self.password = password
        self.link = link
        self.getbrowser()
        self.login()
        self.desired_car_page()
        # self.card_info()
        self.biding()
        self.findingtime()

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
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get('https://cars.bidspirit.com/ui/home?lang=en')
        time.sleep(10)
        self.browser.maximize_window()

    def login(self):
        # getting credentials
        # email, password, _ = self.cred_all()


        # print(email, password)

        # clicking on login
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

    def desired_car_page(self):
        # _, _, car_page = self.cred_all()
        car_page=self.link
        self.browser.get(car_page)
        time.sleep(15)

    def findingtime(self):
        # time_ = self.browser.find_element(By.XPATH, "//div[@class='timer']").text
        # print(time_)
    #     document.getElementsByClassName("circleTimer")['item']
        try:

            time.sleep(30)
            sub=self.browser.execute_script("document.getElementsByClassName('mainCurrency')[0].textContent");
            print(sub)

            if sub:
                print('done'*100)
            else:
                print('not found')

        except:
            print('not found except ')
            page=2
            return page

    def biding(self):
        # self.browser.find_element(By.XPATH, '//div[@class="bid button en noSelect"]').click()
        # text_=self.browser.find_element(By.XPATH,'//div[@class="price text"]').text
        # print('*'*100, text_)

        # try_ = self.browser.execute_script('return document.getElementsByClassName("btn btn-primary ng-binding ng-scope")[0];')
        # self.browser.execute_script('arguments[0].click()', try_)
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Live auction')]").click()
        time.sleep(10)
        c = self.browser.window_handles[1]
        # switch to tab browser
        self.browser.switch_to.window(c)

        bid=self.browser.execute_script('return document.getElementsByClassName("bid button en noSelect")[0];')
        self.browser.execute_script('arguments[0].click()', bid)

        val = bid=self.browser.execute_script('return document.getElementsByClassName("bid button en noSelect")[0].textContent;')
        print(val)

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
