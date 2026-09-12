import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calc_page import CalculatorPage


@allure.feature("Калькулятор с задержкой (slow-calculator)")
@allure.description(
    "Тест проверки работы калькулятора: "
    "установка задержки, ввод выражения 7 + 8, проверка результата"
)
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка сложения 7 + 8 на калькуляторе с задержкой")
def test_calculator_addition():
    """
    Сценарий:
      1. Открыть страницу калькулятора.
      2. Установить задержку 3 секунды.
      3. Нажать кнопки: 7, +, 8, =.
      4. Проверить, что результат равен 15.
    """
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        delay_seconds = 3
        with allure.step(f"Установить задержку: {delay_seconds} сек"):
            page.set_delay(delay_seconds)

        with allure.step("Нажать кнопки: 7, +, 8, ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Получить результат и проверить, что он равен 15"):
            result_text = page.get_result()
            allure.attach(
                f"Ожидаемый: 15, Фактический: {result_text}",
                name="Результат вычисления",
                attachment_type=allure.attachment_type.TEXT,
            )
            assert result_text == "15"

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот при ошибке",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            str(e),
            name="Сообщение об ошибке",
            attachment_type=allure.attachment_type.TEXT,
        )
        raise
    finally:
        driver.quit()
