import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://adobeid-na1.services.adobe.com/renga-idprovider/pages/login?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FSunbreakWebUI1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Faccounts.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%2526reauth%253Dforce&client_id=SunbreakWebUI1&scope=AdobeID%2Copenid%2Csunbreak%2Cacct_mgmt_webui%2Cgnav%2Cadditional_info.account_type%2Csao.cce_private%2Ccreative_cloud%2Cread_countries_regions%2Cupdate_profile.password%2Cadditional_info.roles%2Cupdate_profile.optionalAgreements%2Cupdate_profile.change_password%2Cadditional_info.social%2Csocial.link%2Cunlink_social_account%2Creauthenticated&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FSunbreakWebUI1%3Fredirect_uri%3Dhttps%253A%252F%252Faccounts.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%2526reauth%253Dforce%26response_type%3Dtoken&display=web_v2&relay=25e70a36-4abe-425e-b360-17dbacf035ec&locale=en_US&flow_type=token&idp_flow_type=login&reauthenticate=force")
assert "Adobe" in driver.title
t = randint(10,15)
time.sleep(t)
email = driver.find_element_by_name("username")
email.clear()
email.send_keys("someone@gmail.com")
email.send_keys(Keys.TAB)
t = randint(5,10)
time.sleep(t)
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("your_password")
password.send_keys(Keys.RETURN)
assert "The Adobe ID and password do not match. Please try again." not in driver.page_source
t = randint(10,15)
time.sleep(t)
driver.get("https://helpx.adobe.com/creative-cloud/kb/creative-cloud-apps-download.html")
t = randint(10,15)
time.sleep(t)
driver.close()