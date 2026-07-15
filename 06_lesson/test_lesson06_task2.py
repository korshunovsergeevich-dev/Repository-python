from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
            "name": "sessionid",
            "value": "e782b1dd-a3b8-45fd-8e3a-393ccdada037",
            "domain": "gitflic.ru"
        })

    driver.get("https://gitflic.ru/user/korshunovandreas")

    url_user1 = driver.current_url

    time.sleep(3)
    driver.delete_all_cookies()

    driver.add_cookie({
            "name": "sessionid",
            "value": "023d7021-635c-4c53-8f00-86ba7bd6873c",
            "domain": "gitflic.ru"
        })

    driver.refresh()

    driver.get("https://gitflic.ru/user/id389694398")

    url_user2 = driver.current_url

    assert url_user1 != url_user2

    time.sleep(3)
    driver.quit()
