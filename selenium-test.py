# import dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# create an object of the chrome webdriver
driver = webdriver.Chrome()
# open selenium URL in chrome browser
driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("usmp" + Keys.ENTER)

# print resultant page title
print("Page title is: ")
print(driver.title)

# close browser window
driver.quit()
