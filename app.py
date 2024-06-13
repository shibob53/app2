#ere is the code I used to solve my issue:

from flask import Flask,request,jsonify
from selenium import webdriver
#from selenium import webdriver
#from bs4 import BeautifulSoup
#from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as ChromeService
import os
import random
#from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options

#import mido
from threading import Thread
import json
app = Flask(__name__)

# List to store pressed keysnotes_pressed.
#notes_pressed ={}
def driversetup():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Selenium in headless mode
    options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("lang=en")
    #options.add_argument("start-maximized")
    #options.add_argument("disable-infobars")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--incognito")
    #options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    #driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver

ldriver = driversetup()

@app.route('/sms', methods=['POST'])
def getuser():
  data = request.get_json()
  s=data['sms']
  url = "https://sakani.sa/app/land-projects/"+data['url']
  res = sms_code(s,url,ldriver)
  #if res==200:
  return jsonify(res=res),res
  #else:
    #ldriver.quit()
    #ldriver.close()
    #ldriver = driversetup()
    #return jsonify(res=res),res
  #return driver.current_url

"""
@app.route('/get_notes', methods=['GET'])
def return_pressed_notes():
    return json.dumps(list(notes_pressed.keys()))
@app.route('/get_note', methods=['POST'])
def return_pressed_note():
    data = request.get_json()
    s = data['s'] 
    p = Thread(target=get_next_note, args=(notes_pressed,s,))
    p.start()
    return "json.dumps(notes_pressed)"
# Funnction to translate midi key numbers to note letters
#def translate_key(key_num):
    

# Function that returns recently played note
def get_next_note(notes_pressed,s):
    # Open port to listen for note presses
    for i in range(s):
      sleep(3)
      notes_pressed[i]= driversetup()
      print("#########")
      print(i)
# Run main program
"""
@app.route('/user', methods=['POST'])
def user():
  data = request.get_json()
  uid=data['id']
  password=data["password"]
  res = login(uid,password,ldriver)
 
  #if res==200:
  return jsonify(res=res),res
  #else:
   # ldriver.quit()
   # ldriver.close()
    #ldriver = driversetup()
    #return jsonify(res=res),res
  """
  try:
    driver.get("https://sakani.sa/app/authentication/login")
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
  except Exception as e:
    current_url = f"An error occurred: {e}"
    print(current_url)
    #finally:
        #driver.quit()
  """
  
def login(n_id,password,driver):
    #global driver
    #global L_id

    #driver=driversetup()
    driver.get("https://sakani.sa/app/authentication/login")
    try:
      WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.ID, 'nationId'))).send_keys(n_id)

      WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    except Exception as e:
      #driver.quit()
      #driver.close()
      return 400

    Btn_login = driver.find_elements(By.CSS_SELECTOR, '.btn-primary')
    if len( Btn_login)<1:
      #driver.quit()
      #driver.close()
      return 400
    driver.execute_script("arguments[0].click();", Btn_login[0])
    try:
      Rt = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.flex-auto'))
            )
    except Exception as e:
      if "رقم الهوية او كلمة المرور غير صحيحة" in driver.find_element(By.XPATH, "/html/body").text:
        #driver.quit()
        #driver.close()
        return 300
      #driver.quit()
      #driver.close()
      return 400
    #List_driver[n_id]=[driver,0]
    #L_id.append(n_id)
    return 200  
    


def sms_code(sms,url,driver):
    #global driver
    #return driver.current_url
    #return List_driver
    #global L_id
    #if len(L_id)<1:
      #return 401
    #md=""
   # for i in List_driver:
    #  if List_driver[i][1]==0:
     #   md=i
     #   driver = List_driver[i][0]
      #  List_driver[i][1]=1
   # if md=="":
   #   return 400

    #n_d = L_id[0]
    #del L_id[0]

    if len(sms)==4:
      print(1)

      try:
        Rt = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.flex-auto'))
            )
        print(2)
        if len(Rt)<4:
          #driver.quit()
          #driver.close()
          print(3)
          return 401
        for i in range(4):
          print(4)
          Rt[i].send_keys(sms[i])
      except Exception as e:
        print(5)
        #driver.quit()
        #driver.close()
        return 402
      Btnsms = driver.find_elements(By.CSS_SELECTOR, '.btn-primary')
      print(6)
      if len(Btnsms)<4:
        print (7)
        #driver.quit()
        #driver.close()
        return 403
      driver.execute_script("arguments[0].click();", Btnsms[3])
      print (8)
      if WebDriverWait(driver, 150).until(EC.url_contains("marketplace")):
        print (9)
        driver.get(url)
    else:
      print (10)
      driver.get(url)
    try:
      if "محجوز بالكامل" in driver.find_element(By.XPATH, "/html/body").text:
         return 350
      if "الحجز غير متاح" in driver.find_element(By.XPATH, "/html/body").text:
         return 450
      Btn_new=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[text()='بدء حجز جديد']")))
      driver.execute_script("arguments[0].click();", Btn_new)
      print (11)
    except Exception as e:
      print (12)
      if "محجوز بالكامل" in driver.find_element(By.XPATH, "/html/body").text:
         return 355
    try:
      Lis = WebDriverWait(driver, 150).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'text-neutral-n5')]"))
            )
      print (13)
      if len(Lis)<1:
        print (14)
        #driver.quit()
        #driver.close()
        return 300
      X=random.randint(0,len(Lis))
      print (15)
      print (len(Lis))
      driver.execute_script("arguments[0].click();", Lis[X])
    except Exception as e:
      print (16)
      #driver.quit()
      #driver.close()
      return 404
    try:
      Btn_land=WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//span[text()='حجز قطعة أرض']")))
      driver.execute_script("arguments[0].click();", Btn_land)
      print (17)
    except Exception as e:
      print (18)
      #driver.quit()
      #driver.close()
      return 405
    try:
      Btn_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[text()=' وقع لاحقًا ']")))
      driver.execute_script("arguments[0].click();", Btn_ok)
      print (19)
    except Exception as e:
      print (20)
      if "الحجز غير متاح" in driver.find_element(By.XPATH, "/html/body").text:
         return 455
    #driver.quit()
     #driver.close()
    print (21)
    return 200    
  #return f'{current_url} - Hello from Render'
if __name__ == '__main__':
    # NEW CODE
    #p = Thread(target=get_next_note, args=(notes_pressed,))
    #p.start()
    app.run(host='0.0.0.0', use_reloader=False)
    #p.join()&w
