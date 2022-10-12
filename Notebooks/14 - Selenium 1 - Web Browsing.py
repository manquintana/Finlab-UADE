
# Descargar el driver para chrome: https://chromedriver.chromium.org/downloads

from selenium import webdriver
import time

driver = webdriver.Chrome('Introducir_ruta_al_driver_correspondiente\chromedriver.exe')

url = "https://www.google.com/"
driver.get(url)

time.sleep(2)

text_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
text_input.send_keys("Hello World")

time.sleep(2)

search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
search_button.click()

time.sleep(2)