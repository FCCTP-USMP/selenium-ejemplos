# import dependencies
import os
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()
# get env MICROSOFT_EMAIL with default value "None"
MICROSOFT_EMAIL = os.getenv('MICROSOFT_EMAIL')
MICROSOFT_PASSWORD = os.getenv('MICROSOFT_PASSWORD')

if MICROSOFT_EMAIL is None or len(MICROSOFT_EMAIL) == 0:
    raise Exception("Environtment variable MICROSOFT_EMAIL is required")

if MICROSOFT_PASSWORD is None or len(MICROSOFT_PASSWORD) == 0:
    raise Exception("Environtment variable MICROSOFT_PASSWORD is required")


options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# create an object of the chrome webdriver
driver = webdriver.Chrome(options=options)
driver.get("https://outlook.office.com/mail/")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    email_input = driver.find_element(By.NAME, 'loginfmt')
    email_input.send_keys(MICROSOFT_EMAIL+Keys.ENTER)

    password_input = driver.find_element(By.NAME, 'passwd')
    password_input.send_keys(MICROSOFT_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_attribute(
            (By.XPATH, '//input[@type="submit"]'), 'value', 'Iniciar sesión')
    )
    submit_button = driver.find_element(By.ID, 'idSIButton9')
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "text-title"), "¿Quiere mantener la sesión iniciada?")
    )
    submit_button = driver.find_element(By.ID, 'idSIButton9')
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//button[@aria-label="Correo nuevo"]'))
    )
    print("El botón de nuevo correo fue encontrado")

    new_email_button = driver.find_element(
        By.XPATH, '//button[@aria-label="Correo nuevo"]')
    new_email_button.click()

    print(driver.current_url)

    sleep(10)
finally:
    driver.quit()
