from locators.yandex_locators import ImagesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImagesPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_yandex_page(self):
        self.browser.get("https://ya.ru/")

    def switch_to_new_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def search(self):
        search_input = self.browser.find_element(*ImagesPageLocators.SEARCH_INPUT)
        search_input.click()

    def is_menu_button_displayed(self):
        return self.browser.find_element(*ImagesPageLocators.MENU_BUTTON).is_displayed()

    def open_menu(self):
        menu_button = self.browser.find_element(*ImagesPageLocators.MENU_BUTTON)
        menu_button.click()

    def select_images(self):
        images_link = self.browser.find_element(*ImagesPageLocators.IMAGES_LINK)
        images_link.click()

    def get_current_url(self):
        return self.browser.current_url

    def open_first_category(self):
        first_category = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ImagesPageLocators.CATEGORY))
        first_category.click()

    def is_search_input_value_displayed(self):
        search_input = self.browser.find_element(*ImagesPageLocators.SEARCH_INPUT)
        return bool(search_input.get_attribute("value"))

    def open_first_image(self):
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()

    def is_image_displayed(self):
        image_8th = self.browser.find_element(*ImagesPageLocators.IMAGE)
        return image_8th.is_displayed()

    def get_current_image_text(self):
        image = self.browser.find_element(*ImagesPageLocators.IMAGE)
        return image.text

    def click_next_button(self):
        button_next = self.browser.find_element(*ImagesPageLocators.NEXT_BUTTON)
        button_next.click()

    def click_previous_button(self):
        button_back = self.browser.find_element(*ImagesPageLocators.PREVIOUS_BUTTON)
        button_back.click()
