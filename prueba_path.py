#Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

import time
import pandas as pd

fecha_hoy = datetime.today().strftime('%Y%m%d_%H%M%S')

#Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument("--disable-notifications")

#driver_path = 'C:\\Users\\ingri\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\chromedriver_py\\chromedriver_win32.exe'
#driver_path = 'C:\Users\ingri\AppData\Local\Programs\Python\Python312\Lib\site-packages\chromedriver_py\chromedriver_win64.exe'
driver_path = 'C:\\Users\\ingri\\OneDrive\\Escritorio\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome()


# driver.set_window_position(1000, 0)
# driver.maximize_window()
# time.sleep(10)

driver.get('https://apuestas.wplay.co/es')

time.sleep(10)

# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
#                                                           'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')))).click()

# text_wplay = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div[3]/div/div/div[2]/div')
# text_wplay = text_wplay.text

texto_columnas = driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div')

# texto_columnas = driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[2]/div[3]/div/div/div[2]/div')
texto_columnas = texto_columnas.text

print(texto_columnas)

driver.quit()