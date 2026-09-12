import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shop_page import LoginPage


@allure.feature("Магазин (SauceDemo)")
@allure.description("Тест оформления заказа в интернет-магазине")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Оформление заказа")
def test_checkout_flow():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    try:
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу входа"):
            login_page.open()

        with allure.step("Войти под валидным пользователем"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            inventory_page = login_page.click_login()

        with allure.step("Добавить товары в корзину"):
            inventory_page.add_backpack()
            inventory_page.add_tshirt()

        with allure.step("Перейти в корзину и проверить товары"):
            cart_page = inventory_page.go_to_cart()
            items = cart_page.check_cart_contents()
            assert len(items) >= 2, "В корзине должно быть не менее 2 товаров"

        with allure.step("Нажать Checkout и заполнить форму"):
            checkout_page = cart_page.click_checkout()
            checkout_page.fill_checkout_form("John", "Doe", "12345")
            checkout_page.click_continue()

        with allure.step("Проверить итоговую стоимость"):
            total_text = checkout_page.get_total_price()
            allure.attach(
                f"Ожидаемый префикс: 'Total: $', Фактический: '{total_text}'",
                name="Результат проверки итоговой стоимости",
                attachment_type=allure.attachment_type.TEXT,
            )
            # ИСПРАВЛЕННАЯ СТРОКА: корректный assert без «висячей» запятой
            assert total_text.startswith("Total: $")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот при ошибке",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(str(
            e), name="Сообщение об ошибке",
             attachment_type=allure.attachment_type.TEXT)
        raise
    finally:
        driver.quit()
