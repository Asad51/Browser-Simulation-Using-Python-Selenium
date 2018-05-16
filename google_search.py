import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

key = "python"
driver = webdriver.Chrome()
driver.get("http://www.google.com/")
assert "Google" in driver.title
t = randint(10,15)
time.sleep(t)
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys(key)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
t = randint(10,15)
time.sleep(t)
driver.close()