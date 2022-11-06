

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

class discordLogin:


  @classmethod
  def openADS(self,ads_id,token):
  
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
     
     var0="window.open('{}')".format("https://discord.com/channels/@me")
     driver.switch_to.window(
      driver.window_handles[len(driver.window_handles)-1])
     driver.execute_script(var0)
     driver.switch_to.window(
          driver.window_handles[len(driver.window_handles)-1])
    #  var1="{}={}; {}={}; {}={}; {}={}"
     script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """
     print(script + f'\nlogin("{token}")')   
     driver.execute_script(script + f'\nlogin("{token}")')   
     sleep(10)
     
     Common.closeAds(ads_id)
     
  @classmethod
  def getExcelData(self):
    # 文件打开窗口，路径"D:\\"是窗口打开默认显示的路径，最后一个参数文件的过滤，不满足条件的不会显示
    fileName="discord_data.xls"
    print(fileName)
    if fileName:
        print(f"file: {fileName}")
        excel = xlrd.open_workbook(fileName)
        sheet = excel.sheet_by_index(0)
        b.clear()
        #导入数据
        for i in range(1, sheet.nrows):
         row_list = sheet.row_values(i)
         b.append({"adsId":row_list[0],"token":row_list[1]})
        print(b)
        
        
        
        

discordLogin.getExcelData()

for i  in range(0,len(b)):

    discordLogin.openADS(b[i]["adsId"],b[i]["token"])
    # try:
     
    # except Exception as e:
    #  print(e)

    