import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--start-maximized")

    chrome_service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    request.cls.driver = driver
    yield
    driver.quit()
