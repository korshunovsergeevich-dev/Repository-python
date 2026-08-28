from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.shop_page import LoginPage


def test_saucedemo_checkout():
    # Настройка Firefox
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)

    try:
        # Создаем Page Object страницы авторизации
        login_page = LoginPage(driver)

        # 1. Открыть сайт
        login_page.open()

        # 2. Авторизация
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")

        inventory_page = login_page.click_login()

        # 3. Добавить товары в корзину
        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()

        # 4. Перейти в корзину
        cart_page = inventory_page.go_to_cart()

        # 5. Проверить содержимое корзины
        cart_items = cart_page.check_cart_contents()
        assert len(cart_items) == 3

        # 6. Нажать Checkout
        checkout_page = cart_page.click_checkout()

        # 7. Заполнить данные покупателя
        checkout_page.fill_checkout_form(
            first_name="Андрей",
            last_name="Коршунов",
            zip_code="12345"
        )

        # 8. Нажать Continue
        checkout_page.click_continue()

        # 9. Получить итоговую стоимость
        total_price = checkout_page.get_total_price()

        # 10. Проверить итоговую стоимость
        assert total_price == "Total: $58.29"

    finally:
        # 11. Закрыть браузер
        driver.quit()
