from selenium import webdriver
from pages.calc_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()

    calculator = CalculatorPage(driver)

    calculator.open()
    calculator.set_delay(45)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    assert calculator.get_result() == "15"

    driver.quit()
