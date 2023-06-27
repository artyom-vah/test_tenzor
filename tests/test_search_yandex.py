from pages.search_page import SearchPage


def test_search_yandex(browser):
    """Тестирование 1го сценарий - Поиск в яндексе"""

    # Создание экземпляра SearchPage
    search_page = SearchPage(browser)

    # Шаг 1: Зайти на https://ya.ru/
    search_page.load_page_ya_ru()

    # Шаг 2: Проверить наличие поля поиска
    assert search_page.is_search_input_displayed(), "Поле поиска не отображается на странице"

    # Шаг 3: Ввести в поиск "Тензор"
    search_page.enter_search_query("Тензор")

    # Шаг 4: Проверить, что появилась таблица с подсказками (suggest)
    assert search_page.is_suggest_table_displayed(), "Таблица с подсказками (suggest) не отображается на странице"

    # Шаг 5: Нажать Enter
    search_page.press_enter()

    # Шаг 6: Проверить, что отображаются результаты поиска
    assert search_page.are_search_results_displayed(), "Результаты поиска не отображается на странице"

    # Шаг 7: Проверить, что первая ссылка ведет на сайт tensor.ru
    assert search_page.is_first_link_pointing_to_tensor_ru(), "Первая ссылка не ведет на сайт tensor.ru"
