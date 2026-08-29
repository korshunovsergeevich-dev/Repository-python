from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")

    # Кнопки
    BUTTONS = {
        "7": (By.XPATH, "//span[text()='7']"),
        "+": (By.XPATH, "//span[text()='+']"),
        "8": (By.XPATH, "//span[text()='8']"),
        "=": (By.XPATH, "//span[text()='=']"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        # Открывает страницу калькулятора
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        # Устанавливает задержку в поле ввода
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTONS[button])).click()

    def get_result(self):
        # Возвращает текст результата на экране
        self.wait.until(EC.text_to_be_present_in_element(self.SCREEN, "15")
                        )

        result_element = self.driver.find_element(*self.SCREEN)
        return result_element.text
