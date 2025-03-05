from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = Options()

chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--start-maximized")

chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get("https://practice-automation.com/form-fields/")

name_field = driver.find_element(By.ID, "name-input")
name_field.send_keys("Fedor")

pass_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
pass_field.send_keys("qWe_123")

milk_checkbox = driver.find_element(By.ID, "drink2")
coffee_checkbox = driver.find_element(By.ID, "drink3")
milk_checkbox.click()
coffee_checkbox.click()

color_radiobutton = driver.find_element(By.ID, "color3")
color_radiobutton.click()

answes = driver.find_element(By.ID, "automation")
answers_yes = driver.find_element(By.XPATH, 
"/html/body/div[1]/div[2]/div/div/main/div/article/div/form/select/option[2]")
answes.click()
answers_yes.click()

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("parenkov.fedor@gmail.com")


ul_element = driver.find_element(By.XPATH, 
"/html/body/div[1]/div[2]/div/div/main/div/article/div/form/ul")

li_elements = ul_element.find_elements(By.TAG_NAME, "li")

lst = []
temp = []

for li in li_elements:
    lst.append(li.text)

print(lst)

for i in range(len(lst)):
    temp.append(len(lst[i]))

print(temp)

words_number = len(lst)
max_lenth_word = lst[temp.index(max(temp))]

del lst, temp

message_field = driver.find_element(By.ID, "message")
message_field.send_keys(words_number)
message_field.send_keys(Keys.ENTER)
message_field.send_keys(max_lenth_word)

submit_button = driver.find_element(By.ID, "submit-btn")
submit_button.click()

alert_message = wait.until(EC.alert_is_present())

driver.switch_to.alert

print(alert_message.text) # Message received!

time.sleep(5)

alert_message.accept()

time.sleep(5)

driver.quit()
