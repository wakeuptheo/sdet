from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FillOutForm:

    # объект драйвера из фикстуры
    def __init__(self, driver):  # driver из conftest.py
        self.driver: WebDriver = driver  # аннотация типа WebDriver

    def open_page(self, url):
        self.driver.get(url)

    def set_name(self, name):
        name_field = self.driver.find_element(By.ID, "name-input")
        name_field.send_keys(name)

    def set_password(self, password):
        password_field = self.driver.find_element(
            By.CSS_SELECTOR, "input[type='password']"
        )
        password_field.send_keys(password)

    def select_drink(self, drink1, drink2):
        milk_checkbox = self.driver.find_element(By.ID, drink1)
        milk_checkbox.click()

        coffee_checkbox = self.driver.find_element(By.ID, drink2)
        coffee_checkbox.click()

    def select_color(self, color):
        color_radiobutton = self.driver.find_element(By.ID, color)
        color_radiobutton.click()

    def select_answer(self, answer_option):
        answer_list = self.driver.find_element(By.ID, "automation")
        answer_list.click()

        answer = self.driver.find_element(
            By.XPATH,
            f"/html/body/div[1]/div[2]/div/div/main/div/article/div/form/select/option[{answer_option}]",
        )
        answer.click()

    def set_email(self, email):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys(email)

    def write_message(self):
        # элементы списка Automation tools
        ul_element = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/ul"
        )
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")

        strs, nums = [], []

        # создаем список из значений элементов li
        for li in li_elements:
            strs.append(li.text)

        # создаем список с количеством символов элементов li
        for i in range(len(strs)):
            nums.append(len(strs[i]))

        # количество инструментов в Automation tools
        words_number = len(strs)
        # инструмент Automation tools с наибольшим количеством символов
        max_lenth_word = strs[nums.index(max(nums))]

        del strs, nums

        # заполняем поле Message
        message_field = self.driver.find_element(By.ID, "message")
        message_field.send_keys(words_number)
        message_field.send_keys(Keys.ENTER)
        message_field.send_keys(max_lenth_word)

    def click_submit(self):
        submit_button = self.driver.find_element(By.ID, "submit-btn")
        submit_button.click()
