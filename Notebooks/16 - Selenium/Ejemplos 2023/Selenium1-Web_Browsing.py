from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('chromedriver.exe')

url = "https://www.google.com/"
driver.get(url)

time.sleep(2)

text_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
text_input.send_keys("Hello World")

time.sleep(2)

# search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
# search_button.click()

actions = ActionChains(driver) 
actions.send_keys(Keys.RETURN)
actions.perform()

#text_input.sendKeys(Keys.RETURN);

time.sleep(2)