from pages.images_page import ImagesPage


def test_yandex_image(browser):
    # Создаем экземпляр страницы Яндекс.Картинки
    images_page = ImagesPage(browser)

    # 1. Зайти на ya.ru
    images_page.go_to_yandex_page()

    # 1.1. Нажать на поиск
    images_page.search()

    # 2. Проверить, что кнопка меню(сервисы) присутствует на странице
    assert images_page.is_menu_button_displayed(), "Кнопка меню-сервисы не присутствует на странице"

    # 3. Открыть меню и выбрать "Картинки"
    images_page.open_menu()
    images_page.select_images()

    # Переключиться на новую вкладку
    images_page.switch_to_new_tab()

    # Дождаться, пока URL станет ожидаемым
    expected_url = "https://yandex.ru/images/"
    images_page.wait_for_url_to_be(expected_url)

    actual_url = browser.current_url
    assert actual_url == expected_url, f"Ожидался URL: {expected_url}, получен URL: {actual_url}"

    # 4. Открыть первую категорию
    images_page.open_first_category()

    # 5. Проверить, что название категории отображается в поле поиска
    assert images_page.is_search_input_value_displayed(), "Название категории не отображается в поле поиска"

    # 6. Открыть первую картинку
    images_page.open_first_image()

    # 7. Проверить, что картинка открылась
    assert images_page.is_image_displayed(), "Картинка не открылась"

    # Получаем название картинки на 8-м шаге, чтобы сравнить с шагами 10 и 12
    image_8th_text = images_page.get_current_image_text()

    # 9. Нажать кнопку вперед
    images_page.click_next_button()

    # 10. Проверить, что картинка сменилась
    assert images_page.get_current_image_text() != image_8th_text, "Картинка осталась без изменений"

    # 11. Нажать назад
    images_page.click_previous_button()

    # 12. Проверить, что картинка осталась из шага 8
    assert images_page.get_current_image_text() == image_8th_text, "Картинка изменилась"
