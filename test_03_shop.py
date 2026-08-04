from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout():
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.saucedemo.com/")

    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

# Добавление товаров в корзину
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-onesie"
    ).click()

    cart_icon = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_container")))
    cart_icon.click()

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    first_name_input = wait.until(
        EC.visibility_of_element_located((By.ID, "first-name")))
    last_name_input = driver.find_element(By.ID, "last-name")
    zip_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Андрей")
    last_name_input.send_keys("Коршунов")
    zip_code_input.send_keys("12345")

    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()

    total_element = wait.until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    assert total_text == "Total: $58.29"

    driver.quit()
