####  Group : Group1
####  Target : automatic email sending on special days to specific person using yahoo mail

import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# checking if already emails are sent or not
d = str(datetime.date.today()) + "\n"
try:
    fp = open("files.log", "r")
    txt = fp.read()
    if d == txt:
        print("Already emails are sent today.\n")
        sys.exit(0)
except IOError:
    print("Can't open file")

try:
    fp = open("files.log", "w")
    fp.write(d)
finally:
    print("Date: " + d)

###Login into yahoo account
def login(email, password):
    # enter username
    driver.find_element_by_name("username").send_keys(email)
    time.sleep(5)

    #click next button
    driver.find_element_by_name("signin").click()
    time.sleep(5)

    #enetr password
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(5)

    #click login
    driver.find_element_by_name("verifyPassword").click()
    time.sleep(5)

### sending mail to specific person
def sendMail(email, subject, msgBody):
    #composing email
    #clicking compose button
    driver.find_element_by_css_selector("#app > div.I_ZnwrMC.D_F.em_N.o_h.W_6D6F.H_6D6F > div > div.a_3rehn.W_3o4BO.s_3o4BO.cZ10Gnkk_ZM1sUU.D_F.ek_BB.em_0 > nav > div > div:nth-child(1) > a").click();
    time.sleep(5)
    
    # Enter receiver email
    driver.find_element_by_css_selector("#message-to-field").send_keys(email)
    time.sleep(5)

    # entering email subject
    driver.find_element_by_css_selector("#mail-app-component > div.p_a.R_0.T_0.L_0.B_0.D_F > div > div.compose-header.en_0 > div:nth-child(3) > div > div > input").send_keys(subject)
    time.sleep(5)

    # entering emails body
    driver.find_element_by_css_selector("#editor-container > div.rte.em_N.ir_0.o_h.N_6Fd5").send_keys(msgBody)
    time.sleep(5)

    # sending emails
    driver.find_element_by_css_selector("#mail-app-component > div.p_a.R_0.T_0.L_0.B_0.D_F > div > div.em_N.D_F.ek_BB.p_R.o_h > div:nth-child(2) > div > button").click()


#opening browser
driver = webdriver.Chrome()
driver.get("https://mail.yahoo.com/")
assert "Yahoo" in driver.title
time.sleep(5)

### user's email & password to login
userEmail = "yourEmailAddress@example.com"
userPassword = "yourPassword"

##important declarations
#person : details about receiver
persons = [{
    "email": "asad.cse@yahoo.com",
    "birthday": "1996-05-17",
    "marriageday": "2029-08-07"
}, {
    "email": "asad.cse.ru.15@gmail.com",
    "birthday": "1996-08-07",
    "marriageday": "2026-07-09"
}]

#email subject depending on specific day
emailSubject = {
    "birthday": "Birthday Greetings",
    "marriageday": "Marriage Day Wishing"
}

#email body
emailBody = {
    "birthday": "Happy Birthday to You",
    "marriageday": "Happy Marriage Day"
}

### logging into yahoo mail
try:
    login(userEmail, userPassword)
except:
    print("Can't login.")
    driver.close()
    sys.exit(0)

###checking date for sending emails
toDay = datetime.date.today().day
toMonth = datetime.date.today().month
for person in persons:
    for item in person:
        if(item.__contains__("email")): #picking email
            email = person[item]
        if (item.__contains__("day")):
            year, month, day = person[item].split('-')
            day = int(day)
            month = int(month)
            if (toDay == day and toMonth == month): #checking date
                try:
                    sendMail(email, emailSubject[item], emailBody[item]) #sending mail
                    print("Email has sent to " + email + " at his/her " + item);
                    time.sleep(20)
                except:
                    print("Can't send emails.")
                    driver.close()
                    sys.exit(0);

time.sleep(20)

driver.close()
