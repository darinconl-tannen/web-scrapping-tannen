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

texto_columnas = driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[2]/div[3]/div/div')

# texto_columnas = driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[2]/div[3]/div/div/div[2]/div')
texto_columnas = texto_columnas.text


# print(texto_columnas)

time.sleep(20)


driver.quit()

#######################################################
########## PROCESAMIENTO DE DATOS #####################
#######################################################

# Dividir las líneas en eventos
lineas = texto_columnas.split('\n')

while 'st' in lineas:
    lineas.remove('st')

while 'Empate' in lineas:
    lineas.remove('Empate')

# lineas = [elem for elem in lineas if not (elem.isdigit() and len(elem) == 3)]

print(lineas)

hora = list()
fecha = list()
local_team = list()
local_bet = list()
draw_bet = list()
vis_team = list()
vis_bet = list()
market_amount = list()

for i in range(0, len(lineas), 8):
    hora.append(lineas[i])
    fecha.append(lineas[i+1])
    local_team.append(lineas[i+2])
    local_bet.append(lineas[i+3])
    draw_bet.append(lineas[i+4])
    vis_team.append(lineas[i+5])
    vis_bet.append(lineas[i+6])
    market_amount.append(lineas[i+7])

df = pd.DataFrame({'Hora': hora, 'fecha' : fecha, 'local_team': local_team, 'local_bet': local_bet, 'draw_bet': draw_bet, 'vis_team': vis_team, 'vis_bet': vis_bet, 'market_amount': market_amount })    

print(df)

df.to_csv(f'C:\\Users\\ingri\\OneDrive\\Escritorio\\web_scrapping\\bet_data_{fecha_hoy}.csv', index = False)
# Crear una lista de diccionarios para almacenar la información
