from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get("https://httpbin.org/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9, f"Expected 9, got {len(links)}"

    for link in links:
        assert link.is_displayed()

    first_link_text = links[0].text
    assert "1" in first_link_text

    driver.quit()
