import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
driver.get("http://www.gmail.com/")
assert "Gmail" in driver.title
time.sleep(5)

##login to email
#login details
userEmail = "someone@example.com"
userPwd = "password"

#entering email address
driver.find_element_by_name("identifier").send_keys(userEmail)
driver.find_element_by_id("identifierNext").click()
time.sleep(5)

#entering password
driver.find_element_by_name("password").send_keys(userPwd)
driver.find_element_by_id("passwordNext").click()
time.sleep(30)

##important declarations
persons = [{
    "email": "asad.cse@yahoo.com",
    "birthday": "1996-05-17",
    "marriageday": "2022-03-21"
}, {
    "email": "asad.cse.ru.15@gmail.com",
    "birthday": "1996-03-13",
    "marriageday": "2022-05-17"
}]

emailSubject = {
    "birthday": "Birthday Greetings",
    "marriageday": "Marriage Day Wishing"
}

emailBody = {
    "birthday": "Happy Birthday to You",
    "marriageday": "Happy Marriage Day"
}

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
                sendMail(email, emailSubject[item], emailBody[item]) #sending mail
                print("Email has sent to " + email + " at his/her " + item);
                time.sleep(20)


time.sleep(100)

driver.close()
