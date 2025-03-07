### Проект UI-автотестов заполнения **[тестовой формы](https://practice-automation.com/form-fields/)**

Использованные зависимости:
```
Python 3.13.2
Pytest 8.3.4
Selenium 4.29.0
Webdriver-manager 4.0.2
Allure commandline 2.33.0
Allure-pytest 2.13.5
Allure-python-commons 2.13.5
```
### Установка пакетов
После создания виртуального окружения в терминале выполнить команду:
```
pip install -r requirements.txt
```
Глобально установить **[Allure Сommandline](https://github.com/allure-framework/allure2/releases/)**

### Запуск тестов с генерацией отчета Allure Report

```
pytest -v --alluredir=<путь/к/папке/allure-results>
```

### Просмотр отчета

```
allure serve <путь/к/папке/allure-results>
```
---
Ошибки SSL-сертификата в консоли **```...ERROR:ssl_client_socket_impl.cc(877)] handshake failed; returned -1, SSL error code 1, net_error -100 ```**  пытался убрать путем добавления опций браузера ```--ignore-certificate-errors``` ```--ignore-ssl-errors```, но не помогло. Из-за этого тест долго выполняется.