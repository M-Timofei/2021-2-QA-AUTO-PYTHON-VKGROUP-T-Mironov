from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class,"responseHead-module-button")]')
    LOGIN_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    INPUT_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class,"authForm-module-button")]')
    INVALID_LOGIN_LOCATOR = (By.XPATH, '//*[contains(@class, "notify-module-error")]')
    INVALID_PASSWORD_LOCATOR = (By.XPATH, '//*[@class="formMsg_title"]')

class DashboardPageLocators:
    NEW_COMPANY_LOCATOR_1 = (By.XPATH, '//*[@href="/campaign/new"]')
    NEW_COMPANY_LOCATOR_2 = (By.XPATH, '//*[contains(@class, "dashboard-module-createButtonWrap")]/*[@data-test="button"]/div[contains(@class, "button-module-textWrapper")]')
    AUDIENCE_LOCATOR = (By.XPATH, '//*[@href="/segments"]')

class BasePageLocators:
    SPINNER_LOCATOR = (By.XPATH, '//*[contains(@class,"spinner_")]')

class CampaignPageLocators:
    TRAFFIC_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class,"column-list-item _traffic")]')
    INPUT_URL_LOCATOR = (By.XPATH, '//*[contains(@data-gtm-id,"ad_url_text")]')
    INPUT_COMPANY_NAME_LOCATOR = (By.XPATH, '//*[contains(@class,"input input_campaign-name")]/*[contains(@class,"input__wrap")]/*')
    INPUT_DAILY_LOCATOR = (By.XPATH, '//*[contains(@class,"budget-setting__input-wrap js-budget-setting-daily")]/*[contains(@class,"input")]/*[contains(@class,"input__wrap")]/*')
    INPUT_TOTAL_LOCATOR = (By.XPATH, '//*[contains(@class,"budget-setting__input-wrap js-budget-setting-total")]/*[contains(@class,"input")]/*[contains(@class,"input__wrap")]/*')
    CAROUSEL_LOCATOR = (By.ID, 'patterns_carousel_26')
    UPLOAD_IMG_600_LOCATOR = (By.XPATH, '//*[contains(@class,"upload-module-wrapper")]//*[contains(@data-test,"600")]')
    UPLOAD_IMG_256_LOCATOR = (By.XPATH, '//*[contains(@class,"upload-module-wrapper")]//*[contains(@data-test,"256")]')
    CAROUSEL_1_LOCATOR = (By.XPATH, '//*[contains(@class,"roles-module-slidesTabsItem") and contains(text(), "1")]')
    CAROUSEL_2_LOCATOR = (By.XPATH, '//*[contains(@class,"roles-module-slidesTabsItem") and contains(text(), "2")]')
    CAROUSEL_3_LOCATOR = (By.XPATH, '//*[contains(@class,"roles-module-slidesTabsItem") and contains(text(), "3")]')
    LINK_FOR_SLIDE_1_LOCATOR = (By.XPATH, '//*[contains(@data-name,"url_slide_1")]')
    LINK_FOR_SLIDE_2_LOCATOR = (By.XPATH, '//*[contains(@data-name,"url_slide_2")]')
    LINK_FOR_SLIDE_3_LOCATOR = (By.XPATH, '//*[contains(@data-name,"url_slide_3")]')
    HEADING_FOR_SLID_1_LOCATOR = (By.XPATH, '//*[contains(@data-name,"title_25_slide_1")]')
    HEADING_FOR_SLID_2_LOCATOR = (By.XPATH, '//*[contains(@data-name,"title_25_slide_2")]')
    HEADING_FOR_SLID_3_LOCATOR = (By.XPATH, '//*[contains(@data-name,"title_25_slide_3")]')
    MAIN_HEADING_LOCATOR = (By.XPATH, '//*[@data-name="title_25"]')
    MAIN_TEXT_LOCATOR = (By.XPATH, '//*[@data-name="text_50"]')
    SAVE_PROJECT_LOCATOR = (By.XPATH, '//*[contains(@data-test,"submit_banner_button")]/*[contains(@class,"button-module-textWrapper")]')
    CREATE_COMPANY_LOCATOR = (By.XPATH, '//*[contains(@class,"footer__button")]/*[contains(@class,"button button_submit")]')
    NAME_OF_COMPANY_LOCATOR = (By.XPATH, '//*[contains(@class, "header-module-noWrap")]')
    EMPTY_NAME_OF_COMPANY_LOCATOR = (By.XPATH, '//*[contains(@class, "dashboard-module-notifyText")]')
    MENU_LOCATOR = (By.XPATH, '//*[contains(@class, "tableControls-module-controlsWrap")]/*[contains(@class, "select-module-selectWrap")]')
    MENU_DELETE_LOCATOR = (By.XPATH, '//*[@data-id="8"]')
    INTERNAL_ERROR_LOCATOR = (By.XPATH, '//*[@class="footer__error js-error-wrap"]')
    PREVIEW_COMPANY_LOCATOR = (By.XPATH, '//*[contains(@class,"bannerPreview-module-actionsLeft")]')


class SegmentsPageLocators:
    NEW_SEGMENT_LOCATOR_1 = (By.XPATH, '//*[@href="/segments/segments_list/new/"]')
    NEW_SEGMENT_LOCATOR_2 = (By.XPATH, '//*[contains(@class, "button button_submit")]/*')
    CHECKBOX_LOCATOR = (By.XPATH, '//*[contains(@class, "adding-segments-source__checkbox")]')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "js-add-button")]/*[@data-class-name="Submit"]')
    INPUT_SEGMENT_NAME_LOCATOR = (By.XPATH, '//*[contains(@class, "input_create-segment-form")]//*[contains(@class, "input__inp js-form-element")]')
    CREATE_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "button_submit")]/*[contains(@class, "button__text")]')
    NAME_OF_SEGMENT = (By.XPATH, '//*[contains(@class, "label-module-label")]')
    DELETE_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "button_confirm-remove")]')
    DELETE_WINDOW_LOCATOR = (By.XPATH, '//*[contains(@class, "delete-confirm-list")]')