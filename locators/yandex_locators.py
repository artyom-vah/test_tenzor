from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__overlay_visible")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".serp-item.serp-item_card")
    FIRST_LINK = (By.TAG_NAME, "a")


class ImagesPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    SERVICES_MENU = (By.CSS_SELECTOR, ".services-suggest__item-more")
    IMAGES_LINK = (By.CSS_SELECTOR, "div.services-more-popup__section-content:nth-child(1) > span:nth-child(9) > a:nth-child(2)")
    FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item__link")


