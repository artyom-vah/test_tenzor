from locators.yandex_locators import ImagesPageLocators


class ImagesPage:
    def __init__(self, browser):
        self.browser = browser

    def open_yandex_ru(self):
        """# 1. Зайти на ya.ru"""
        self.browser.get("https://ya.ru")

    def click_search(self):
        search_input = self.browser.find_element(*ImagesPageLocators.SEARCH_INPUT)
        search_input.click()

    def open_services_menu(self):
        services_menu = self.browser.find_element(*ImagesPageLocators.SERVICES_MENU)
        services_menu.click()

    def click_images_link(self):
        images_link = self.browser.find_element(*ImagesPageLocators.IMAGES_LINK)
        images_link.click()

    def open_yandex_images(self):
        self.browser.get("https://yandex.ru/images/")

    def open_first_category(self):
        first_category = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY)
        first_category.click()

    def open_first_image(self):
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()
