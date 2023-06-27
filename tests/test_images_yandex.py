from pages.images_page import ImagesPage


def test_yandex_image(browser):
    """Тестирование 2го сценарий - Картинки на яндексе"""

    # Создаем экземпляр ImagesPage (страницы Яндекс.Картинки)
    images_page = ImagesPage(browser)

    # Шаг 1: Зайти на ya.ru
    images_page.go_to_yandex_page()

    # Шаг 1.1: Нажать на поиск чтобы появилась кнопка меню (сервисы)
    images_page.click_on_search()

    # Шаг 2: Проверить, что кнопка меню (сервисы) присутствует на странице
    assert images_page.is_menu_button_displayed(), "Кнопка меню-сервисы не присутствует на странице"

    # Шаг 3: Открыть меню
    images_page.open_menu()

    # Шаг 3.1: Выбрать "Картинки"
    images_page.select_images()

    # Шаг 3.2: Переключиться на новую вкладку
    images_page.switch_to_new_tab()

    # Шаг 3.3: Дождаться, пока страница картинок откроется
    expected_url = "https://yandex.ru/images/"
    images_page.wait_for_url_to_be(expected_url)

    # Шаг 4: Проверить, что перешли на url https://yandex.ru/images/
    actual_url = images_page.get_current_url()
    assert actual_url == expected_url, f"Ожидался URL: {expected_url}, получен URL: {actual_url}"

    # Шаг 5: Открыть первую категорию
    images_page.open_first_category()

    # Шаг 6: Проверить, что название категории отображается в поле поиска
    assert images_page.is_search_input_value_displayed(), "Название категории не отображается в поле поиска"

    # Шаг 7: Открыть первую картинку
    images_page.open_first_image()

    # Шаг 8: Проверить, что картинка открылась
    assert images_page.image_is_open(), "Картинка не открылась"

    # Шаг 8.1: Получаем название картинки на 8-м шаге, чтобы сравнить с шагами 10 и 12
    image_8th_text = images_page.get_current_image_text()

    # Шаг 9: Нажать кнопку вперед
    images_page.click_next_button()

    # Шаг 10: Проверить, что картинка сменилась
    assert images_page.get_current_image_text() != image_8th_text, "Картинка осталась без изменений"

    # Шаг 11: Нажать назад
    images_page.click_previous_button()

    # Шаг 12: Проверить, что картинка осталась из шага 8
    assert images_page.get_current_image_text() == image_8th_text, "Картинка изменилась"
