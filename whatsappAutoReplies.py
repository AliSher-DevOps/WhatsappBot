from selenium import webdriver
from csv import reader
import time
import pandas as pd
driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(15)
try:
    df = pd.read_csv('data.csv')
    for number,mess in zip(df['number'],df['Message']):
        address = "https://web.whatsapp.com/send?phone="+number
        driver.get(address)
        time.sleep(10)
        message = "".join(mess.splitlines())        
        text_box =  driver.find_element_by_class_name('_2A8P4')
        text_box.send_keys(message)
        time.sleep(2)
        button = driver.find_element_by_class_name("_1E0Oz")
        button.click()
        time.sleep(5)
       
except:
    print("No Internet or Slow Internet. Please re-run the script")











