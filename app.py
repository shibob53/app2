'''from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driversetup():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Selenium in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("lang=en")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver
    
app = Flask(__name__)

@app.route('/')
def hello_world():
  driver = driversetup()
  
  return driver.current_url + 'Hello from Koyeb'
 
 
if __name__ == "__main__":
    app.run()'''
from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import logging

app = Flask(__name__)

# إعداد تسجيل الرسائل
logging.basicConfig(level=logging.INFO)

def driversetup():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Selenium in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("lang=en")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver
driver = driversetup () 
@app.route('/')
def hello_world():
    logging.info("Received request at root endpoint")
    global driver# = driversetup()
    try:
        driver.get('https://www.google.com')
        current_url = driver.current_url
        logging.info(f"Current URL: {current_url}")
    except Exception as e:
        current_url = f"An error occurred: {e}"
        logging.error(current_url)
    finally:
        driver.quit()
    
    return f'{current_url} - Hello from Render'
@app.route('/hello')
def hello():
  global driver #= driversetup()
  
  return driver.current_url + ' Hello'
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logging.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port)



    
