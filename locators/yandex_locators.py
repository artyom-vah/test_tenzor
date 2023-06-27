from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__overlay_visible")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".serp-item.serp-item_card")
    FIRST_LINK = (By.TAG_NAME, "a")


class ImagesPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    MENU_BUTTON = (By.CSS_SELECTOR, ".services-suggest__list-item-more")
    IMAGES_LINK = (By.XPATH, "//a[@href='https://yandex.ru/images/']")
    CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item__link")
    IMAGE = (By.CSS_SELECTOR, ".Link_view_default")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div.CircleButton_type_next")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, "div.CircleButton_type_prev")
