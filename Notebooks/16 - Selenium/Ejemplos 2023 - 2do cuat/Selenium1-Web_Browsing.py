from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# ###################
# Notas!!! 2do cuat. 2023
# Selenium 4.3.0
# * Deprecated find_element_by_* and find_elements_by_* are now removed (#10712)
# Tambien cambiaron el método webdriver, ahora si se quiere ejecutar un driver local, hay que hacerlo instanciando la clase "Service"
# Básicamente cambió todo fue un cambio de versión muuuuy abarcativo y no tiene retro-compatibilidad.
# ###################
# https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath
# ###################

#driver = webdriver.Chrome(executable_path="route_to_driver")
service = Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.google.com/'
driver.get(url)

time.sleep(5)

#text_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
text_input = driver.find_element('xpath','//*[@id="APjFqb"]')
text_input.send_keys("Hermetica")

time.sleep(5)

# search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
# search_button.click()
clic_out = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]')
clic_out.click()

time.sleep(5)

search_button = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
search_button.click()

# actions = ActionChains(driver)
# actions.send_keys(Keys.RETURN)
# actions.perform()

time.sleep(5)