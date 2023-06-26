from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__overlay_visible")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".serp-item.serp-item_card")
    FIRST_LINK = (By.TAG_NAME, "a")


class ImagesPageLocators:
    pass
