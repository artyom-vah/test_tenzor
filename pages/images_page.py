from locators.yandex_locators import ImagesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImagesPage:
    """Поиск и работа с картинками на Яндексе."""
    def __init__(self, browser):
        self.browser = browser

    def go_to_yandex_page(self):
        """Шаг 1: Зайти на ya.ru."""
        self.browser.get("https://ya.ru/")

    def click_on_search(self):
        """Шаг 1.1: Нажать на поиск чтобы появилась кнопка меню (сервисы)."""
        search_input = self.browser.find_element(*ImagesPageLocators.SEARCH_INPUT)
        search_input.click()

    def is_menu_button_displayed(self):
        """Шаг 2: Проверить, что кнопка меню (сервисы) присутствует на странице."""
        return self.browser.find_element(*ImagesPageLocators.MENU_BUTTON).is_displayed()

    def open_menu(self):
        """Шаг 3: Открыть меню."""
        menu_button = self.browser.find_element(*ImagesPageLocators.MENU_BUTTON)
        menu_button.click()

    def select_images(self):
        """Шаг 3.1: Выбрать "Картинки."""
        images_link = self.browser.find_element(*ImagesPageLocators.IMAGES_LINK)
        images_link.click()

    def switch_to_new_tab(self):
        """Шаг 3.2: Переключиться на новую вкладку."""
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def wait_for_url_to_be(self, expected_url, timeout=10):
        """Шаг 3.3: Дождаться, пока страница картинок откроется."""
        WebDriverWait(self.browser, timeout).until(EC.url_to_be(expected_url))

    def get_current_url(self):
        """Шаг 4: Получаем текущую url."""
        return self.browser.current_url

    def open_first_category(self):
        """Шаг 5: Открыть первую категорию."""
        first_category = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ImagesPageLocators.CATEGORY))
        first_category.click()

    def is_search_input_value_displayed(self):
        """Шаг 6: Проверить, что название категории отображается в поле поиска."""
        search_input = self.browser.find_element(*ImagesPageLocators.SEARCH_INPUT)
        return bool(search_input.get_attribute("value"))

    def open_first_image(self):
        """Шаг 7: Открыть первую картинку."""
        first_image = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ImagesPageLocators.FIRST_IMAGE)
        )
        first_image.click()

    def image_is_open(self):
        """Шаг 8: Проверить, что картинка открылась"""
        image_8th = self.browser.find_element(*ImagesPageLocators.IMAGE)
        return image_8th.is_displayed()

    def get_current_image_text(self):
        """Шаг 8.1, 10, 12 : Получаем название картинки на 8-м шаге, чтобы сравнить с шагами 10 и 12"""
        image = self.browser.find_element(*ImagesPageLocators.IMAGE)
        return image.text

    def click_next_button(self):
        """Шаг 9: Нажать кнопку вперед."""
        button_next = self.browser.find_element(*ImagesPageLocators.NEXT_BUTTON)
        button_next.click()

    def click_previous_button(self):
        """Шаг 11: Нажать кнопку назад."""
        button_back = self.browser.find_element(*ImagesPageLocators.PREVIOUS_BUTTON)
        button_back.click()
