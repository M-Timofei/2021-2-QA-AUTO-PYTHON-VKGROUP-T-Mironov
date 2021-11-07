from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class,"responseHead-module-button")]')
    LOGIN_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    INPUT_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class,"authForm-module-button")]')
    INVALID_LOGIN_LOCATOR = (By.XPATH, '//div[contains(@class, "notify-module-error")]')
    INVALID_PASSWORD_LOCATOR = (By.XPATH, '//div[@class="formMsg_title"]')

class DashboardPageLocators:
    NEW_COMPANY_LOCATOR_1 = (By.XPATH, '//*[@href="/campaign/new"]')
    NEW_COMPANY_LOCATOR_2 = (By.XPATH, '//div[contains(@class, "createButtonWrap")]/div/div')
    AUDIENCE_LOCATOR = (By.XPATH, '//a[@href="/segments"]')

class BasePageLocators:
    SPINNER_LOCATOR = (By.XPATH, '//div[contains(@class,"spinner_")]')

class CampaignPageLocators():
    TRAFFIC_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class,"_traffic")]')
    INPUT_URL_LOCATOR = (By.XPATH, '//input[contains(@data-gtm-id,"ad_url_text")]')
    INPUT_COMPANY_NAME_LOCATOR = (By.XPATH, '//div[contains(@class,"input input_campaign-name")]//input')
    INPUT_DAILY_LOCATOR = (By.XPATH, '//div[contains(@class,"js-budget-setting-daily")]//input')
    INPUT_TOTAL_LOCATOR = (By.XPATH, '//div[contains(@class,"js-budget-setting-total")]//input')
    CAROUSEL_LOCATOR = (By.ID, 'patterns_carousel_26')
    UPLOAD_IMG_LOCATOR = lambda n: (By.XPATH, f'//div//input[contains(@data-test,"{n}")]')
    NUMBER_CAROUSEL_LOCATOR = lambda k: (By.XPATH, f'//li[contains(@class,"roles-module-slidesTabsItem") and contains(text(), "{k}")]')
    LINK_FOR_SLIDE_LOCATOR = lambda k: (By.XPATH, f'//input[contains(@data-name,"url_slide_{k}")]')
    HEADING_FOR_SLID_LOCATOR = lambda k: (By.XPATH, f'//input[contains(@data-name,"title_25_slide_{k}")]')
    MAIN_HEADING_LOCATOR = (By.XPATH, '//input[@data-name="title_25"]')
    MAIN_TEXT_LOCATOR = (By.XPATH, '//textarea[@data-name="text_50"]')
    SAVE_PROJECT_LOCATOR = (By.XPATH, '//div[contains(@data-test,"submit_banner_button")]/div')
    CREATE_COMPANY_LOCATOR = (By.XPATH, '//div[contains(@class,"footer__button")]/button')
    NAME_OF_COMPANY_LOCATOR = (By.XPATH, '//div[contains(@class, "header-module-noWrap")]')
    EMPTY_NAME_OF_COMPANY_LOCATOR = (By.XPATH, '//span[contains(@class, "dashboard-module-notifyText")]')
    MENU_LOCATOR = (By.XPATH, '//div[contains(@class, "tableControls-module")]/div[contains(@class, "selectWrap")]')
    MENU_DELETE_LOCATOR = (By.XPATH, '//li[@data-id="8"]')
    PREVIEW_COMPANY_LOCATOR = (By.XPATH, '//div[contains(@class,"bannerPreview-module-actionsLeft")]')


class SegmentsPageLocators:
    NEW_SEGMENT_LOCATOR_1 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    NEW_SEGMENT_LOCATOR_2 = (By.XPATH, '//button[contains(@class, "button_submit")]/div')
    CHECKBOX_LOCATOR = (By.XPATH, '//input[contains(@class, "js-main-source-checkbox")]')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "js-add-button")]//div')
    INPUT_SEGMENT_NAME_LOCATOR = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]//input')
    CREATE_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "button_submit")]/div')
    NAME_OF_SEGMENT = (By.XPATH, '//div[contains(@class, "label-module-label")]')
    DELETE_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')
    DELETE_WINDOW_LOCATOR = (By.XPATH, '//div[contains(@class, "delete-confirm-list")]')