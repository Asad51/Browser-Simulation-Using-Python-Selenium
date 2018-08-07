import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://mail.yahoo.com/")
assert "Yahoo" in driver.title
t = randint(5,7)
time.sleep(t)

email = driver.find_element_by_name("username")
email.clear()
email.send_keys("asadul441@yahoo.com")
t = randint(5,7)
time.sleep(t)

emailNext = driver.find_element_by_name("signin")
emailNext.click()
t = randint(5,7)
time.sleep(t)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("%@$@dul15%")
t = randint(5,7)
time.sleep(t)

passwordNext = driver.find_element_by_name("verifyPassword")
passwordNext.click()
t = randint(5,7)
time.sleep(t)

compose = driver.find_element_by_css_selector("#app > div.I_ZnwrMC.D_F.em_N.o_h.W_6D6F.H_6D6F > div > div.a_3rehn.W_3o4BO.s_3o4BO.cZ10Gnkk_ZM1sUU.D_F.ek_BB.em_0 > nav > div > div:nth-child(1) > a")
compose.click();
t = randint(5,7)
time.sleep(t)

to = driver.find_element_by_css_selector("#message-to-field")
to.clear()
to.send_keys("asad.cse.ru.15@gmail.com")
t = randint(5,7)
time.sleep(t)
to.send_keys(Keys.TAB)

subject = driver.find_element_by_css_selector("#mail-app-component > div.p_a.R_0.T_0.L_0.B_0.D_F > div > div.compose-header.en_0 > div:nth-child(3) > div > div > input")
subject.clear()
subject.send_keys("Special Days")
t = randint(5,7)
time.sleep(t)
subject.send_keys(Keys.TAB)

msg = driver.find_element_by_css_selector("#editor-container > div.rte.em_N.ir_0.o_h.N_6Fd5");
msg.clear()
msg.send_keys("Hey, What's up?")
t = randint(5,7)
time.sleep(t)
#msg.send_keys(Keys.TAB)

driver.find_element_by_css_selector("#mail-app-component > div.p_a.R_0.T_0.L_0.B_0.D_F > div > div.em_N.D_F.ek_BB.p_R.o_h > div:nth-child(2) > div > button").click()