

import string
from xmlrpc.client import Boolean
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from util.commonUtil import Common
from selenium.webdriver.common.by import *
from time import sleep
from loguru import *
from globalvar import *
from widgetModel import *
from util.jsonUtil import *
import json
import xlwt
import xlrd


b=[]

class layoutMain:


  @classmethod
  def openADS(self,ads_id):
  
     resp = requests.get("http://local.adspower.com:50325/api/v1/browser/start?open_tabs=1&headless=0&user_id="+ads_id).json()
     if resp["code"] != 0:
        #  logger.info(resp["msg"])
         logger.info("please check ads_id")
         sys.exit()
     
     chrome_driver = resp["data"]["webdriver"]
     chrome_options = Options()
     chrome_options.add_experimental_option(
         "debuggerAddress", resp["data"]["ws"]["selenium"])
     driver = webdriver.Chrome(chrome_driver, options=chrome_options)   
    #  temp = "window.open('chrome-extension://gcakedikjhjoejpaededegmppnbfdpmp/home.html#initialize/welcome')"
    #  driver.execute_script(temp)
     driver.get("chrome-extension://gcakedikjhjoejpaededegmppnbfdpmp/home.html#initialize/welcome")
     driver.switch_to.window(
           driver.window_handles[len(driver.window_handles)-1])
    # 输入密码
    #  //*[@id="password"]
     val=Common.check_element_exists(By.XPATH, "//*[@id=\"password\"]", driver)
     
     Common.AutoInput(By.XPATH, "//*[@id=\"password\"]", "w7217459", driver)
    #  点击Unlock
    #  //*[@id="app-content"]/div/div[3]/div/div/button
     Common.AutoClick(
         By.XPATH, "//*[@id=\"app-content\"]/div/div[3]/div/div/button", driver)
     #点击三个点
     
     Common.AutoClick(By.XPATH,"//button[@data-testid='account-options-menu-button']",driver)
     
     Common.AutoClick(By.XPATH,"//button[@data-testid='account-options-menu__account-details']",driver)
     
     Common.AutoClick(By.XPATH,"//button[text()='Export Private Key']",driver)
     
     Common.AutoInput(By.XPATH, "//input[@type='password']", "w7217459", driver)
     
     Common.AutoClick(By.XPATH, "//button[text()='Confirm']", driver)
     
     private_key = Common.AutoGetElement(By.XPATH,"//div[@class='export-private-key-modal__private-key-display']",driver).text
     
     address = Common.AutoGetElement(By.XPATH,"//div[@class='ellip-address-wrapper']",driver).text
     
     var0="window.open('{}')".format("https://labs.zetachain.com/leaderboard")
     print(var0)
     driver.execute_script(var0)
     driver.switch_to.window(
          driver.window_handles[len(driver.window_handles)-1])
    #  var1="{}={}; {}={}; {}={}; {}={}"
     var1=""
     cookies = driver.get_cookies()
     for cookie in cookies:
     # 值打印cookie中的name和value
      var1=var1+cookie['name']+"="+cookie['value']+"; "
     print(var1) 
     
     dict0={"privateKey":private_key,"address":address,"adsId":ads_id,"cookie_str":var1}
     
     b.append(dict0)
     
     Common.closeAds(ads_id)


@classmethod
def getExcelData(self):
    # 文件打开窗口，路径"D:\\"是窗口打开默认显示的路径，最后一个参数文件的过滤，不满足条件的不会显示
    fileName="data.xls"
    print(fileName)
    if fileName:
        print(f"file: {fileName}")
        excel = xlrd.open_workbook(fileName)
        sheet = excel.sheet_by_index(0)
        account_data.clear()
        #导入数据
        for i in range(1, sheet.nrows):
         row_list = sheet.row_values(i)
         account_data.append({"privateKey":row_list[1],"address":row_list[0],"adsId":row_list[3],"cookie_str":row_list[2]})
        print(len(account_data))

a=[
"j3lor6e","j3lor6d","j3lor6c","j3lor6b","j3lor6a","j3lor69","j3lor68","j3lor67","j3lor66","j3lor65",
"j3lor6q","j3lor6p","j3lor6n","j3lor6m","j3lor6l","j3lor6k","j3lor6j","j3lor6i","j3lor6h","j3lor6g",
"j3lor91","j3lor90","j3lor8y","j3lor8x","j3lor8w","j3lor8v","j3lor8u","j3lor8t","j3lor8s","j3lor8r",
"j3lor8q","j3lor8p","j3lor8o","j3lor8n","j3lor8m","j3lor8l","j3lor8k","j3lor8j","j3lor8i","j3lor8h",
"j3lor8g","j3lor8f","j3lor8e","j3lor8d","j3lor8c","j3lor8b","j3lor8a","j3lor89","j3lor88","j3lor87",
"j3lor86","j3lor85","j3lor84","j3lor83","j3lor82","j3lor81","j3lor80","j3lor7y","j3lor7x","j3lor7w",
"j3lor7v","j3lor7u","j3lor7t","j3lor7s","j3lor7r","j3lor7q","j3lor7p","j3lor7o","j3lor7n","j3lor7m",
"j3lor7l","j3lor7k","j3lor7j","j3lor7i","j3lor7h","j3lor7g","j3lor7f","j3lor7e","j3lor7d","j3lor7c",
"j3lor7b","j3lor7a","j3lor79","j3lor78","j3lor77","j3lor76","j3lor75","j3lor74","j3lor73","j3lor72",
"j3lor71","j3lor70","j3lor6y","j3lor6x","j3lor6w","j3lor6v","j3lor6u","j3lor6t","j3lor6s","j3lor6r",
]
# "j3lor6e","j3lor6d","j3lor6c","j3lor6b","j3lor6a","j3lor69","j3lor68","j3lor67","j3lor66","j3lor65",
# "j3lor6q","j3lor6p","j3lor6n","j3lor6m","j3lor6l","j3lor6k","j3lor6j","j3lor6i","j3lor6h","j3lor6g",
# "j3lor91","j3lor90","j3lor8y","j3lor8x","j3lor8w","j3lor8v","j3lor8u","j3lor8t","j3lor8s","j3lor8r",
# "j3lor8q","j3lor8p","j3lor8o","j3lor8n","j3lor8m","j3lor8l","j3lor8k","j3lor8j","j3lor8i","j3lor8h",
# "j3lor8g","j3lor8f","j3lor8e","j3lor8d","j3lor8c","j3lor8b","j3lor8a","j3lor89","j3lor88","j3lor87",
# "j3lor86","j3lor85","j3lor84","j3lor83","j3lor82","j3lor81","j3lor80","j3lor7y","j3lor7x","j3lor7w",
# "j3lor7v","j3lor7u","j3lor7t","j3lor7s","j3lor7r","j3lor7q","j3lor7p","j3lor7o","j3lor7n","j3lor7m",
# "j3lor7l","j3lor7k","j3lor7j","j3lor7i","j3lor7h","j3lor7g","j3lor7f","j3lor7e","j3lor7d","j3lor7c",
# "j3lor7b","j3lor7a","j3lor79","j3lor78","j3lor77","j3lor76","j3lor75","j3lor74","j3lor73","j3lor72",
# "j3lor71","j3lor70","j3lor6y","j3lor6x","j3lor6w","j3lor6v","j3lor6u","j3lor6t","j3lor6s","j3lor6r",

c=["j3lor65",]

for i  in range(0,len(a)):
    print("打开"+a[i])
    try:
     addressInfo=layoutMain.openADS(a[i])
    except Exception as e:
     print(e)
    print(json.dumps(b))
    
xl = xlwt.Workbook(encoding='utf-8')
ws = xl.add_sheet("data导出", cell_overwrite_ok=True)


ws.write(0,0,"地址")
ws.write(0,1,"私钥") 
ws.write(0,2,"cookie") 
ws.write(0,3,"ads_id")

for i in range(0,len(b)):
   ws.write(i+1,0,b[i]["privateKey"])
   ws.write(i+1,1,b[i]["address"]) 
   ws.write(i+1,2,b[i]["cookie_str"]) 
   ws.write(i+1,3,b[i]["adsId"])
# timestamp=datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d %H%M%S')   
xl.save('data导出.xls')     

    
# 260 261 262
#  "j3lor7b","j3lor7a","j3lor79","j3lor78","j3lor77","j3lor76","j3lor75"
# "j3lor7v","j3lor7u","j3lor7t","j3lor7s","j3lor7r","j3lor7q","j3lor7p","j3lor7o","j3lor7n","j3lor7m",
# "j3lor7l","j3lor7k","j3lor7j","j3lor7i","j3lor7h","j3lor7g","j3lor7f","j3lor7e","j3lor7d","j3lor7c",