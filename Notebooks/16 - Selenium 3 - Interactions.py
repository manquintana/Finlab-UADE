# These days, most of the web apps are using AJAX techniques. 
# When a page is loaded by the browser, the elements within that page may load at different time intervals.
# This makes locating elements difficult: if an element is not yet present in the DOM, a locate function will 
# raise an ElementNotVisibleException exception. 
# Using waits, we can solve this issue. 
# Waiting provides some slack between actions performed - mostly locating an element or any other operation with the element.
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = 'https://earth.google.com/web/'

driver = webdriver.Chrome('Introducir ruta al driver aca')
driver.get(url)

#search = WebDriverWait(driver,15).until(
#    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/div/a/span/span'))
#    )
#search.click()
# ESTO YA NO FUNCIONA, GOOGLE EARTH HIZO ESTE ELEMENTO "NO INTERACTUABLE"!! HAY QUE BUSCAR OTRA MANERA

#search.send_keys('Madrid')
#search.send_keys(Keys.Enter)





