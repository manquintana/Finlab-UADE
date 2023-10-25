from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains 
import time

url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
#driver = webdriver.Chrome('chromedriver.exe')
#driver.maximize_window()
service = Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

time.sleep(5)

source1 = driver.find_element('xpath', '//*[@id="box1"]')
destination1 = driver.find_element('xpath', '//*[@id="box101"]')

source2 = driver.find_element('xpath', '//*[@id="box2"]')
destination2 = driver.find_element('xpath', '//*[@id="box102"]')

source3 = driver.find_element('xpath', '//*[@id="box3"]')
destination3 = driver.find_element('xpath', '//*[@id="box103"]')

actions = ActionChains(driver) #ActionChains crea una cola de acciones, donde se podrán concatenar cuantas querramos.
actions.drag_and_drop(source1, destination1) # Agregamos una accion a la cola
actions.drag_and_drop(source2, destination2) # Agregamos una accion a la cola
actions.drag_and_drop(source3, destination3) # Agregamos una accion a la cola
actions.perform() # Ejecutamos la cola de acciones

time.sleep(5)