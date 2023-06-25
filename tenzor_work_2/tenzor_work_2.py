import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    # Завершение работы WebDriver после выполнения теста
    driver.quit()


def test_yandex_image_flow(browser):
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