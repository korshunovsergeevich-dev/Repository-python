import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_form_validation(driver):
    wait = WebDriverWait(driver, 30)

    driver.get(
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/data-types.html"
    )

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }
    for field_name, value in form_data.items():
        driver.find_element(
            By.NAME,
            field_name,
        ).send_keys(value)

    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']",
    ).click()

    zip_code = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code.get_attribute("class")

    successful_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in successful_fields:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class")
