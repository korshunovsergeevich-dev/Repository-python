from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException


class CalculatorPage:
    """Page Object для страницы калькулятора с задержкой."""

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")
    # Универсальный локатор для оверлея/лоадера на странице slow-calculator
    OVERLAY = (
        By.CSS_SELECTOR, ".loader, .overlay, .modal-backdrop, div[class*="
        "'loading']")

    # Кнопки
    BUTTONS = {
        "7": (By.XPATH, "//span[text()='7']"),
        "+": (By.XPATH, "//span[text()='+']"),
        "8": (By.XPATH, "//span[text()='8']"),
        "=": (By.XPATH, "//span[text()='=']"),
    }

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver (selenium.webdriver)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https:/"
            "/bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку в поле ввода.

        :param seconds: значение задержки в секундах (int)
        """
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button: str) -> None:
        """
        Нажимает кнопку на калькуляторе с обработкой перекрытия элементами.

        :param button: символ кнопки (например, '7', '+', '=') (str)
        """
        locator = self.BUTTONS.get(button)
        if locator is None:
            raise ValueError(
                f"Кнопка '{button}' не найдена в словаре BUTTONS"
            )

        element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
        except TimeoutException:
            pass

        try:
            element.click()
        except ElementClickInterceptedException:
            # ИСПРАВЛЕНО: arguments[0] вместо arguments
            self.driver.execute_script(
                "arguments[0].click();", element
            )

    def get_result(self) -> str:
        """
        Получает текст результата на экране.

        :return: текст результата (str)
        """
        self.wait.until(EC.text_to_be_present_in_element(self.SCREEN, "15"))
        result_element = self.driver.find_element(*self.SCREEN)
        return result_element.text
