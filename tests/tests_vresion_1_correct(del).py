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


def test_search_yandex(browser):
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


def test_yandex_image(browser):
    # 1. Зайти на ya.ru
    browser.get("https://ya.ru")

    # 2. Нажать на поиск
    search_input = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    search_input.click()

    # 3. Открыть все окно-меню "все сервисы" и выбрать "картинки"
    services_menu = browser.find_element(By.CSS_SELECTOR, ".services-suggest__item-more")
    assert services_menu.is_displayed()
    services_menu.click()

    images_link = browser.find_element(By.CSS_SELECTOR, "div.services-more-popup__section-content:nth-child(1) > span:nth-child(9) > a:nth-child(2)")
    images_link.click()

    browser.get("https://yandex.ru/images/")

    # 5. Проверить, что перешли на url https://yandex.ru/images/
    assert browser.current_url == "https://yandex.ru/images/"

    # 6. Открыть первую категорию
    first_category = browser.find_element(By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    first_category.click()

    # 7. Открыть 1 картинку
    first_image = browser.find_element(By.CSS_SELECTOR, ".serp-item__link")
    first_image.click()

    # 8. Проверить, что картинка открылась
    assert "https://yandex.ru/images/" in browser.current_url

    # 9. Нажать кнопку вперед
    browser.back()

    # 10. Проверить, что картинка сменилась
    assert "https://yandex.ru/images/" in browser.current_url

    # 11. Нажать назад
    browser.forward()

    # 12. Проверить, что картинка осталась из шага 8
    assert "https://yandex.ru/images/" in browser.current_url
