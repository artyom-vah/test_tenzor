import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    # Инициализация WebDriver перед началом теста
    driver = webdriver.Firefox()
    yield driver
    # Завершение работы WebDriver после выполнения теста
    driver.quit()


def test_search_tensor(browser):
    # Шаг 1: Зайти на https://ya.ru/
    browser.get("https://ya.ru/")

    # Шаг 2: Проверить наличие поля поиска
    search_input = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    assert search_input.is_displayed()

    # Шаг 3: Ввести в поиск "Тензор"
    search_input.send_keys("Тензор")

    # Шаг 4: Проверить, что появилась таблица с подсказками (suggest)
    suggest_table = browser.find_element(By.CLASS_NAME, "mini-suggest__overlay_visible")
    assert suggest_table.is_displayed()

    # Шаг 5: Нажать Enter
    search_input.send_keys(Keys.ENTER)

    # Шаг 6: Проверить, что отображаются результаты поиска
    search_results = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.serp-item.serp-item_card'))
    )
    assert search_results.is_displayed()

    # Шаг 7: Проверить, что первая ссылка ведет на сайт tensor.ru
    first_link = search_results.find_element(By.TAG_NAME, 'a')
    href = first_link.get_attribute("href")
    assert "tensor.ru" in href
