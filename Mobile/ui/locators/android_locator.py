from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

class MainPageLocators():
    DENY_BUTTON = (MobileBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')

class SearchPageLocators():
    KEYBOARD = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    KEYBOARD_2 = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    INPUT_TEXT_LOCATOR = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    ENTER_SEARCH_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_send')
    RESULT_LOCATOR = (MobileBy.ID, 'ru.mail.search.electroscope:id/dialog_item')
    TEXT_IN_ARTICLE = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_content_text')
    LOW_PANEL = (MobileBy.XPATH, f'//android.view.ViewGroup[2]/android.widget.TextView')
    POPULATION_LOCATOR = (MobileBy.XPATH, "//android.widget.TextView[@text='население россии']")
    RADIO_NAME = (MobileBy.ID, 'ru.mail.search.electroscope:id/player_track_name')
    MENU_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')
    CARD_TITLE = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_title')

class NewsPageLocator():
    NEWS_FM = (By.XPATH, '//android.widget.TextView[contains(@text, "Вести")]')
    ITEM_NEWS = (MobileBy.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')

class AboutPageLocators():
    VERSION_ID = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_version')
    COPYRIGHT = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_copyright')

class MenuPageLocators():
    NEWS = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    ABOUT_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')