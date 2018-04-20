import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.bing.com/")
assert "Bing" in driver.title
t = randint(10,15)
time.sleep(t)
search_form = driver.find_element_by_name("q")
search_form.clear()
search_form.send_keys("Automatic Browser Simulation")
search_button = driver.find_element_by_name("go")
search_button.click();
assert "No results found." not in driver.page_source
t = randint(10,15)
time.sleep(t)
driver.close()