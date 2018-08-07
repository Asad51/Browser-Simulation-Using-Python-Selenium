#Group : Group1
#Target : Automatically sending emails to specific email address on special days

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
        print("Already sent emails today.\n")
        sys.exit(0)
except IOError:
    print("Can't open file")

try:
    fp = open("files.log", "w")
    fp.write(d)
finally:
    print("Date: " + d)

### login into google account
def login(email, password):
    #entering email address
    driver.find_element_by_name("identifier").send_keys(email)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(5)

    #entering password
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(20)

###sending mail to specific person
def sendMail(email, subject, msgBody):
    #composing email
    #clicking compose button
    driver.find_element_by_css_selector(".aic .z0 div").click()
    time.sleep(15)

    #Entering receiver
    driver.find_element_by_css_selector(".eV .oj .wO textarea").send_keys(
        email)
    time.sleep(5)

    #Entering subject
    driver.find_element_by_css_selector(".bAs .az6 input").send_keys(subject)
    time.sleep(5)

    #Message Body
    driver.find_element_by_css_selector(".Ap .Au div").send_keys(msgBody)
    time.sleep(5)

    #sending email
    driver.find_element_by_css_selector(".btC .Up .btA .aoO").click()

#opening browser
driver = webdriver.Chrome()
driver.get(
    "https://accounts.google.com/AccountChooser?service=mail&amp;continue=https://mail.google.com/mail/"
)
assert "Gmail" in driver.title
time.sleep(5)

##important declarations

#login details
userEmail = "yourEmailAddress@example.com" #user's email
userPwd = "yourPassword"         #user's password

persons = [{
    "email": "asad.cse@yahoo.com",
    "birthday": "1996-05-17",
    "marriageday": "2022-08-07"
}, {
    "email": "asad.cse.ru.15@gmail.com",
    "birthday": "1996-08-07",
    "marriageday": "2022-07-09"
}]

emailSubject = {
    "birthday": "Birthday Greetings",
    "marriageday": "Marriage Day Wishing"
}

emailBody = {
    "birthday": "Happy Birthday to You",
    "marriageday": "Happy Marriage Day"
}

##login to email
try:
    login(userEmail, userPwd)
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
                    #driver.find_element_by_css_selector(".aic .z0 div")
                    print("Email has sent to " + email + " at his/her " + item);
                    time.sleep(20)
                except:
                    print("Can't send emails.")
                    driver.close()
                    sys.exit(0)


time.sleep(20)

driver.close()
