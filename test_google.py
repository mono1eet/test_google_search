import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_form_submission(browser):
    # Открываем тестовую страницу с формой
    browser.get("http://the-internet.herokuapp.com/login")
    
    # Заполняем форму
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    
    # Нажимаем кнопку входа
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Проверяем успешный вход
    success_message = browser.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text, "Ожидалось сообщение об успешном входе"

def test_invalid_login(browser):
    # Открываем страницу
    browser.get("http://the-internet.herokuapp.com/login")
    
    # Заполняем неправильные данные
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    username.send_keys("wronguser")
    password.send_keys("wrongpass")
    
    # Нажимаем кнопку входа
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Проверяем сообщение об ошибке
    error_message = browser.find_element(By.ID, "flash")
    assert "Your username is invalid!" in error_message.text, "Ожидалось сообщение об ошибке входа"
