
import time, requests, json
import zetaCrossChain
from util.commonUtil import Common
from globalvar import *
import logging
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import *
from widgetModel import *
import xlwt 
import xlrd

# data = jsonUtil.load_js("testfile/1.json")


class requestTemp:

 @classmethod
 def get_token(self,address,cookie_str):
    url = f"https://labs.zetachain.com/api/get-zeta"
    data = {"address":address}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4173.2 Safari/537.36",
               "Accept": "*/*",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Accept-Encoding": "gzip, deflate, br",
               "Referer": "https://labs.zetachain.com/",
               "Content-Type": "application/json",
               "Origin": "https://labs.zetachain.com",
               "Content-Length": "777",
               "Connection": "keep-alive",
               "path":"/api/save-transaction",
               "origin":"https://labs.zetachain.com",
               "referer":"https://labs.zetachain.com/swap",
               "sec-ch-ua-platform":"Windows",
               "sec-fetch-dest":"empty",
               "sec-fetch-mode":"cors",
               "sec-fetch-site":"same-origin",
               "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
               "cookie":cookie_str,
               }
    
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    print(response.text)
    return response.json()

 @classmethod
 def saveTransaction(self,hash_str,address,cookie_str):
    
    url = f"https://labs.zetachain.com/api/save-transaction"
    data = {
    "sourceChainId": "80001",
    "sourceChainTxHash": hash_str,
    "walletAddress": address
    }
    
    print(json.dumps(data))
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4173.2 Safari/537.36",
               "Accept": "*/*",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Accept-Encoding": "gzip, deflate, br",
               "Referer": "https://labs.zetachain.com/",
               "Content-Type": "application/json",
               "Origin": "https://labs.zetachain.com",
               "Content-Length": "777",
               "Connection": "keep-alive",
               "path":"/api/save-transaction",
               "origin":"https://labs.zetachain.com",
               "referer":"https://labs.zetachain.com/swap",
               "sec-ch-ua-platform":"Windows",
               "sec-fetch-dest":"empty",
               "sec-fetch-mode":"cors",
               "sec-fetch-site":"same-origin",
               "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
               "cookie":cookie_str,
               }
    
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    print(response.text)
    return response.json()


 @classmethod
 def openADS(self,ads_id):
  
     resp = requests.get(open_url+ads_id).json()
     if resp["code"] != 0:
        #  logging.info(resp["msg"])
         logging.info("please check ads_id")
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
     logging.info(val)
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
     print(private_key)
     
     address = Common.AutoGetElement(By.XPATH,"//div[@class='ellip-address-wrapper']",driver).text
     print(address)
     
     var0="window.open('{}')".format("https://labs.zetachain.com/leaderboard") 
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
     Common.closeAds(ads_id)
     return dict0
     



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
         





# dict=requestTemp.openADS("j3lor6e")
# account_dicts = jsonUtil.load_js("config/account.json")
requestTemp.getExcelData()

for i  in range(0,len(account_data)):
 try:
#    print(account_data[i]["address"])  
#    print(requestTemp.get_token(account_data[i]["address"],account_data[i]["cookie_str"]))
     
   zetaCrossChain.approveZeta(account_data[i]["privateKey"],account_data[i]["address"])
   time.sleep(10)
   hash_str=zetaCrossChain.testContract(account_data[i]["privateKey"],account_data[i]["address"])
   time.sleep(10)
   print(requestTemp.saveTransaction(hash_str,account_data[i]["address"],account_data[i]["cookie_str"]))
 except Exception as e  :
   print(e)
