# from pathlib import Path
# import json
# pp=str(Path(__file__).parents[1])+'\static\credentials.json'
# pp1=Path(__file__).parent
# print(pp,pp1)
# # F:\AI\PROJECTS\feb\feb23\new\carbot\static\credentials.json
# credentials = open(pp)
# cred_json = json.load(credentials)
# print(cred_json)

# import selenium
# import webdriver_manager
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# # import pandas as pd
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
# options.add_argument("--incognito")
# options.add_argument("--nogpu")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1280,1280")
# options.add_argument("--no-sandbox")
# options.add_argument("--enable-javascript")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
#
# # self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options )
# browser = webdriver.Chrome(options=options )
#
# browser.get('https://reutgallery.bidspirit.com/?pt=f56bbfcd-717f-4579-b702-b8f423edb210&lang=en&fromPortal=1#live')
# time.sleep(10)
# browser.maximize_window()
#
# time.sleep(13)
# id_path = browser.find_element(By.XPATH,'(//div[@class="picContainer "]/div)[2]')
# print(id_path)
# id = id_path.get_attribute("style")
# url = str(id).split("url")[1].split(";")[0]
# print(id, '\n', type(id),'\n' ,url)
# print(url)
# if "cloned" in url:
#     print("it is in url")
#
# num = len(browser.find_elements(By.XPATH, '//div[@class="items"]/div'))
# print("Total number of matching is : ", num)
#
#
# def waiting_for_id(IdNum):
#     id_path = browser.find_element(By.XPATH, '(//div[@class="picContainer "]/div)[2]')
#     id = id_path.get_attribute("style")
#     url = str(id).split("url")[1].split(";")[0]
#     print(id, '\n', type(id), '\n', url)
#     no_id = True
#     while no_id:
#         try:
#             id_path = browser.find_element(By.XPATH, '(//div[@class="picContainer "]/div)[2]')
#             id = id_path.get_attribute("style")
#             url = str(id).split("url")[1].split(";")[0]
#             print(id, '\n', type(id), '\n', url)
#             if IdNum in url:
#                 print(f"product with {id} is on bid now")
#                 no_id = False
#             time.sleep(2)
#         except:
#             continue
#
# waiting_for_id("24885")
# # try:
# #     print(id["background-image"])
# # except:
# #     print(id["url"])

# id = 'z-index: 5; background-image: url("https://d2zofuu73zurgl.cloudfront.net/keren-ost/cloned-images/17200/009/a_ignore_q_80_w_1000_c_limit_009.jpg"); opacity: 0;'
id = 'background-image: url("https://d2zofuu73zurgl.cloudfront.net/cnymilitaria/cloned-images/20256/001/a_ignore_q_80_w_1000_c_limit_001.jpg"); z-index: 3; opacity: 1;'
url = str(id).split("url")[1].split(";")[0]
# print(id, '\n', type(id), '\n', url)
current_id = int(str(url.split("cloned-images")[1][:-2]).split("/")[1])
print(id, '\n', type(id), '\n', url, '\n', 'current running is is : ', current_id, type(current_id))

