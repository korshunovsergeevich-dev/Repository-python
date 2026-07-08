from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    custname_field = driver.find_element(By.NAME, "custname")

    custname_field.send_keys("Andrey")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click('Submit')

    assert driver.current_url("/post")

    driver.quit()
