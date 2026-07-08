from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click("HTML Form")

    assert driver.current_url.endswith("/forms/post")

    driver.back()

    assert driver.current_url.endswith("/httpbin")
