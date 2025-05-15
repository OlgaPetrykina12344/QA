from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_example_website():

    driver = webdriver.Chrome()

    try:

        driver.get("https://example.com")
        print("Страница example.com загружена")
        assert "Example" in driver.title, f"Заголовок должен содержать 'Example', получен: {driver.title}"
        print("✓ Заголовок содержит 'Example'")
        more_info_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'More information')]"))
        )
        more_info_link.click()
        print("✓ Клик по 'More information' выполнен")
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.iana.org/help/example-domains")
        )
        print(f"✓ Перенаправление на {driver.current_url} подтверждено")

    except TimeoutException as e:
        print(f"Таймаут при ожидании элемента: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_example_website()