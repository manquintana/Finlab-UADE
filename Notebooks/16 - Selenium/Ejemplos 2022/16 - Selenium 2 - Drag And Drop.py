from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #Permite hacer tareas complejas
import time
url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'

driver = webdriver.Chrome('Introducir_ruta_al_driver_correspondiente\chromedriver.exe')
#driver.maximize_window()
driver.get(url)
source = driver.find_element_by_xpath('//*[@id="box3"]')
destination = driver.find_element_by_xpath('//*[@id="box103"]')

actions = ActionChains(driver) #ActionChains crea una cola de acciones, donde se podrán concatenar cuantas querramos.
actions.drag_and_drop(source, destination) # Agregamos una accion a la cola
actions.perform() # Ejecutamos la cola de acciones
time.sleep(5)
