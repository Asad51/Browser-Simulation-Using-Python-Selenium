import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#opening browser
driver = webdriver.Chrome()
driver.get("http://www.gmail.com/")
assert "Gmail" in driver.title
time.sleep(5)

##User Details
userEmail = "you@example.com"
userPwd = "password"

#enter email address
driver.find_element_by_name("identifier").send_keys(userEmail)
driver.find_element_by_id("identifierNext").click()
time.sleep(5)

#enter password
driver.find_element_by_name("password").send_keys(userPwd)
driver.find_element_by_id("passwordNext").click()
time.sleep(20)

#composing email
#clicking compose button
driver.find_element_by_css_selector(".aic .z0 div").click()
time.sleep(10)

#Receiver
driver.find_element_by_css_selector(".eV .oj .wO textarea").send_keys(
    "asad.cse.ru.15@gmail.com")
time.sleep(5)

#subject
driver.find_element_by_css_selector(".bAs .az6 input").send_keys(
    "Dummy Message")
time.sleep(5)

#Message Body
driver.find_element_by_css_selector(".Ap .Au div").send_keys("Hey, what's up?")
time.sleep(5)

driver.find_element_by_css_selector(".btC .Up .btA .aoO").click()
time.sleep(30)

driver.close();
