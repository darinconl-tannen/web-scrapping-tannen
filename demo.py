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

#driver_path = 'C:\\Users\\ingri\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\chromedriver_py\\chromedriver_win32.exe'
#driver_path = 'C:\Users\ingri\AppData\Local\Programs\Python\Python312\Lib\site-packages\chromedriver_py\chromedriver_win64.exe'
# driver_path = 'C:\\Users\\ingri\\OneDrive\\Escritorio\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome()


# driver.set_window_position(1000, 0)
# driver.maximize_window()
# time.sleep(10)

driver.get('https://eltiempo.es')

time.sleep(10)

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                                          'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')))).click()

print('ejecuto')

time.sleep(40)


driver.quit()
#option = webdriver.ChromeOptions()