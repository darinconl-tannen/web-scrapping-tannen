#Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import pandas as pd


#Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver = webdriver.Chrome()


driver.get('https://apuestas.wplay.co/es')

time.sleep(10)

patron_xpath  = '/html/body/div[1]/div/div[3]/div/div/div[2]/div'

elementos_xpath = driver.find_element("xpath",patron_xpath)

print(elementos_xpath)
# cantidad_elementos = len(elementos_xpath)

# print(cantidad_elementos)


driver.quit()