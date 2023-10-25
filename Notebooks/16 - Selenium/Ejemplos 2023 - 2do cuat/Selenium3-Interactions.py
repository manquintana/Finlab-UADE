# These days, most of the web apps are using AJAX techniques. 
# When a page is loaded by the browser, the elements within that page may load at different time intervals.
# This makes locating elements difficult: if an element is not yet present in the DOM, a locate function will 
# raise an ElementNotVisibleException exception. 
# Using waits, we can solve this issue. 
# Waiting provides some slack between actions performed - 
# mostly locating an element or any other operation with the element.
#
# Y lo que no queremos es justamente "explicitar" el timeout, lo que podríamos hacer sin problemas...
# Sino que queremos seleccionar un elemento una vez que esté disponible
#
# Nuestro objetivo en este ejercicio será posicionar el mapa de Google en Madrid de manera automatizada
# Pensemos los pasos necesarios:
# 1. Abrir Google Earth
# 2. Acceder al cuadro de búsqueda
# 3. Escribir "Madrid"
# 4. Confirmar la búsqueda





from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains 
import time
# ...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://earth.google.com/web/'

service = Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

menu = WebDriverWait(driver,15).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/flutter-view/flt-text-editing-host/form/input[1]'))
    #EC.element_to_be_clickable((By.XPATH, '/html/body/earth-app//paper-drawer-panel/div/earth-toolbar'))
    )

print('Elemento encontrado o Timeout')

time.sleep(15)

body = driver.find_element('xpath', '/html/body')
body.click()

time.sleep(2)

#text_box = driver.find_element('class', 'flt-text-editing')
#text_box.send_keys('Madrid')
#time.sleep(15)
#a = ActionChains(driver)
#m = driver.find_element_by_xpath('/html/body/earth-app//paper-drawer-panel/div/earth-toolbar//earth-gm2-icon-button[2]//iron-icon')
#a.move_to_element(m).perform()
#m.click()
# ESTO YA NO FUNCIONA, GOOGLE EARTH HIZO ESTE ELEMENTO "NO INTERACTUABLE"!! HAY QUE BUSCAR OTRA MANERA

#search.send_keys('Madrid')
#search.send_keys(Keys.Enter)