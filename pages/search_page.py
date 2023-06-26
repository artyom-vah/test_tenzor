from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.yandex_locators import SearchPageLocators


class SearchPage:
    """Поиск страницы на Яндексе."""
    def __init__(self, browser):
        """Инициализация класса SearchPag"""
        self.browser = browser

    def load_page(self):
        """Загрузка страницы поиска https://ya.ru/."""
        self.browser.get("https://ya.ru/")

    def is_search_input_displayed(self):
        """Проверка отображения поля ввода."""
        search_input = self.browser.find_element(*SearchPageLocators.SEARCH_INPUT)
        return search_input.is_displayed()

    def enter_search_query(self, query):
        """Ввод поискового запроса в поле поиска."""
        search_input = self.browser.find_element(*SearchPageLocators.SEARCH_INPUT)
        search_input.send_keys(query)

    def is_suggest_table_displayed(self):
        """Проверка отображения таблицы с подсказками (suggest)."""
        suggest_table = self.browser.find_element(*SearchPageLocators.SUGGEST_TABLE)
        return suggest_table.is_displayed()

    def press_enter(self):
        """Нажатие клавиши Enter."""
        search_input = self.browser.find_element(*SearchPageLocators.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)

    def are_search_results_displayed(self):
        """Проверка отображения результатов поиска."""
        search_results = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(SearchPageLocators.SEARCH_RESULTS)
        )
        return search_results.is_displayed()

    def is_first_link_pointing_to_tensor_ru(self):
        """Проверка, что первая ссылка ведет на сайт tensor.ru."""
        search_results = self.browser.find_element(*SearchPageLocators.SEARCH_RESULTS)
        first_link = search_results.find_element(*SearchPageLocators.FIRST_LINK)
        href = first_link.get_attribute("href")
        return "tensor.ru" in href