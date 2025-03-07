import pytest
import allure
from pages.fillout_form import FillOutForm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestFillOutFormPage:

    URL = "https://practice-automation.com/form-fields/"
    NAME = "Fedor"
    PASSWORD = "qWe_123"
    DRINK_1 = "drink2"
    DRINK_2 = "drink3"
    COLOR = "color3"
    ANSWER = "2"
    EMAIL = "parenkov.fedor@gmail.com"

    def setup_method(self):
        self.fillout_form = FillOutForm(self.driver)

    @allure.feature("Тестовая форма")
    @allure.story("Заполнение тестовой формы")
    def test_fillout_form(self):
        with allure.step("Открыть страницу"):
            self.fillout_form.open_page(self.URL)
        with allure.step("Ввести имя"):
            self.fillout_form.set_name(self.NAME)
        with allure.step("Ввести пароль"):
            self.fillout_form.set_password(self.PASSWORD)
        with allure.step("Выбрать напитки"):
            self.fillout_form.select_drink(self.DRINK_1, self.DRINK_2)
        with allure.step("Выбрать цвет"):
            self.fillout_form.select_color(self.COLOR)
        with allure.step("Выбрать вариант ответа"):
            self.fillout_form.select_answer(self.ANSWER)
        with allure.step("Ввести email"):
            self.fillout_form.set_email(self.EMAIL)
        with allure.step("Заполнить поле Message"):
            self.fillout_form.write_message()
        with allure.step("Нажать кнопку Submit"):
            self.fillout_form.click_submit()

        wait = WebDriverWait(self.driver, 10)

        try:
            alert_message = wait.until(EC.alert_is_present())
            self.fillout_form.driver.switch_to.alert
        except TimeoutException:
            pytest.fail("No alert")

        assert alert_message.text == "Message received!"

        alert_message.accept()
