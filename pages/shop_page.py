from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.inventory_list = (By.CLASS_NAME, "inventory_list")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(
                self.username_input
            )
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(
                self.password_input
            )
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.inventory_list
            )
        )

        return InventoryPage(self.driver)


class InventoryPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.backpack_button = (
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )

        self.tshirt_button = (
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt"
        )

        self.onesie_button = (
            By.ID,
            "add-to-cart-sauce-labs-onesie"
        )

        self.cart_icon = (
            By.CLASS_NAME,
            "shopping_cart_container"
        )

    def add_backpack(self):
        """Добавить Sauce Labs Backpack в корзину."""
        self.wait.until(
            EC.element_to_be_clickable(
                self.backpack_button
            )
        ).click()

    def add_tshirt(self):
        """Добавить Sauce Labs Bolt T-Shirt в корзину."""
        self.wait.until(
            EC.element_to_be_clickable(
                self.tshirt_button
            )
        ).click()

    def add_onesie(self):
        """Добавить Sauce Labs Onesie в корзину."""
        self.wait.until(
            EC.element_to_be_clickable(
                self.onesie_button
            )
        ).click()

    def go_to_cart(self):
        """Перейти в корзину."""
        self.wait.until(
            EC.element_to_be_clickable(
                self.cart_icon
            )
        ).click()

        return CartPage(self.driver)


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def check_cart_contents(self):
        """Проверить, что корзина содержит товары."""
        items = self.wait.until(
            EC.presence_of_all_elements_located(
                self.cart_items
            )
        )

        return items

    def click_checkout(self):
        """Нажать кнопку Checkout."""
        self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        ).click()

        return CheckoutPage(self.driver)


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")

        self.continue_button = (By.ID, "continue")

        self.total_label = (
            By.CLASS_NAME,
            "summary_total_label"
        )

    def fill_checkout_form(
        self,
        first_name,
        last_name,
        zip_code
    ):
        """Заполнить форму оформления заказа."""

        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name_input
            )
        ).send_keys(first_name)

        self.wait.until(
            EC.visibility_of_element_located(
                self.last_name_input
            )
        ).send_keys(last_name)

        self.wait.until(
            EC.visibility_of_element_located(
                self.zip_code_input
            )
        ).send_keys(zip_code)

    def click_continue(self):
        """Нажать кнопку Continue."""
        self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        ).click()

    def get_total_price(self):
        """Получить итоговую стоимость заказа."""
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                self.total_label
            )
        )

        return total_element.text
