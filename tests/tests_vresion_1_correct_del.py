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
    # 1: Зайти на https://ya.ru/
    browser.get("https://ya.ru/")

    # 2: Проверить наличие поля поиска
    search_input = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    assert search_input.is_displayed()

    # 3: Ввести в поиск "Тензор"
    search_input.send_keys("Тензор")

    # 4: Проверить, что появилась таблица с подсказками (suggest)
    suggest_table = browser.find_element(By.CLASS_NAME, "mini-suggest__overlay_visible")
    assert suggest_table.is_displayed()

    # 5: Нажать Enter
    search_input.send_keys(Keys.ENTER)

    # 6: Проверить, что отображаются результаты поиска
    search_results = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.serp-item.serp-item_card'))
    )
    assert search_results.is_displayed()

    # 7: Проверить, что первая ссылка ведет на сайт tensor.ru
    first_link = search_results.find_element(By.TAG_NAME, 'a')
    href = first_link.get_attribute("href")
    assert "tensor.ru" in href


def test_yandex_image(browser):
    # 1. Зайти на ya.ru
    browser.get("https://ya.ru/")

    # 1.1. Нажать на поиск
    search_input = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    search_input.click()

    # 2. Проверить, что кнопка меню(сервисы) присутствует на странице
    menu_button = browser.find_element(By.CSS_SELECTOR, '.services-suggest__list-item-more')
    assert menu_button.is_displayed(), "Кнопка меню-сервисы не присутствует на странице"
    menu_button.click()

    # 3. Выбрать “Картинки”
    images_link = browser.find_element(By.XPATH, '//a[@href="https://yandex.ru/images/"]')
    images_link.click()

    # Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[-1])

    # Дождаться, пока URL станет ожидаемым
    expected_url = "https://yandex.ru/images/"
    WebDriverWait(browser, 10).until(EC.url_to_be(expected_url))

    # 4. Проверить, что перешли на URL https://yandex.ru/images/
    actual_url = browser.current_url
    assert actual_url == expected_url, f"Ожидался URL: {expected_url}, получен URL: {actual_url}"

    # 5. Открыть первую категорию
    first_category = browser.find_element(By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    first_category.click()

    # 6. Проверить, что название категории отображается в поле поиска
    search_input = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    assert search_input.get_attribute("value"), "Название категории не отображается в поле поиска"

    # 7. Открыть 1 картинку
    first_image = browser.find_element(By.CSS_SELECTOR, ".serp-item__link")
    first_image.click()

    # 8. Проверить, что картинка открылась
    image_8th = browser.find_element(By.CSS_SELECTOR, '.Link_view_default')
    assert image_8th.is_displayed(), "Картинка не открылась"

    # получаем название картинки на 8м шаге, чтоб сравнить с шагом 10 и 12
    image_8th_text = image_8th.text
    print(image_8th_text)

    # 9. Нажать кнопку вперед
    button_next = browser.find_element(By.CSS_SELECTOR, 'div.CircleButton_type_next')
    button_next.click()

    # 10. Проверить, что картинка сменилась, сравниваем текст картинки 8 и 10
    image_10th = browser.find_element(By.CSS_SELECTOR, '.Link_view_default')
    assert image_10th.text != image_8th_text, "Картинка осталась без изменений"

    # 11. Нажать назад
    button_back = browser.find_element(By.CSS_SELECTOR, 'div.CircleButton_type_prev')
    button_back.click()

    # 12. Проверить, что картинка осталась из шага 8
    image_12th = browser.find_element(By.CSS_SELECTOR, '.Link_view_default')
    assert image_12th.text == image_8th_text, "Картинка изменилась"
