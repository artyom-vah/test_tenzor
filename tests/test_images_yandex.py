from pages.images_page import ImagesPage


def test_yandex_image(browser):
    images_page = ImagesPage(browser)

    # Открываем страницу ya.ru
    images_page.open_yandex_ru()

    # Нажамаем на поиск
    images_page.click_search()

    # Открываем меню 'все сервисы'
    images_page.open_services_menu()

    # Нажимаем на ссылку "картинки"
    images_page.click_images_link()

    # Переходим на страницу yandex.ru/images/
    images_page.open_yandex_images()

    # Открываем первую категорию
    images_page.open_first_category()

    # Открываем первую картинку
    images_page.open_first_image()

    # Проверяем, что находимся на странице yandex.ru/images/
    assert "https://yandex.ru/images/" in browser.current_url

    # Нажимаем кнопку "Назад" в браузере
    images_page.go_back()

    # Проверяем, что остались на странице yandex.ru/images/
    assert "https://yandex.ru/images/" in browser.current_url, "Не удалось вернуться на страницу yandex.ru/images/"

    # Нажимаем кнопку "Вперед" в браузере
    images_page.go_forward()

    # Проверяем, что картинка осталась из шага 8
    assert "https://yandex.ru/images/" in browser.current_url, "Картинка изменилась"
