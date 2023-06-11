from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #Permite hacer tareas complejas
import time
url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'

driver = webdriver.Chrome('chromedriver.exe')
#driver.maximize_window()
driver.get(url)
source1 = driver.find_element_by_xpath('//*[@id="box3"]')
destination1 = driver.find_element_by_xpath('//*[@id="box103"]')

source2 = driver.find_element_by_xpath('//*[@id="box7"]')
destination2 = driver.find_element_by_xpath('//*[@id="box107"]')

actions = ActionChains(driver) #ActionChains crea una cola de acciones, donde se podrán concatenar cuantas querramos.
actions.drag_and_drop(source1, destination1) # Agregamos una accion a la cola
actions.drag_and_drop(source2, destination2) # Agregamos una accion a la cola
actions.perform() # Ejecutamos la cola de acciones
time.sleep(5)