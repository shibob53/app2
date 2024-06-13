#ere is the code I used to solve my issue:

from flask import Flask,request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
from time import sleep
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

driver = driversetup()

@app.route('/getuser', methods=['GET'])
def getuser():
  #data = request.get_json()
  #s=data['s']
  return driver.current_url

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
@app.route('/user', methods=['GET'])
def user():
  #data = request.get_json()
  #s=data['s']
  try:
    driver.get("https://sakani.sa/app/authentication/login")
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
  except Exception as e:
    current_url = f"An error occurred: {e}"
    print(current_url)
    #finally:
        #driver.quit()
    
  return f'{current_url} - Hello from Render'
if __name__ == '__main__':
    # NEW CODE
    #p = Thread(target=get_next_note, args=(notes_pressed,))
    #p.start()
    app.run(debug=True)
    #app.run(host='0.0.0.0', use_reloader=False)
    #p.join()&w
