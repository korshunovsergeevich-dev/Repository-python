from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = [
        "7", "+", "8", "="
    ]

    for btn_text in buttons:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[normalize-space()='{btn_text}']",))).click()

    result_wait = WebDriverWait(driver, 45)

    result_wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"),
            "15",
        )
    )

    result_text = driver.find_element(
        By.CLASS_NAME,
        "screen",
    ).text.strip()

    assert result_text == "15"

    driver.quit()
