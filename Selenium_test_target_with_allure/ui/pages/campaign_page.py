import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from random import randint
from ui.pages.base_page import BasePage
from ui.locators import target_locators
import os
from utils.decorators import wait
import numpy
from PIL import Image
from ui import urls

class CampaignPage(BasePage):
    url = urls.URL_CAMPANING
    locators = target_locators.CampaignPageLocators()

    def check_img_saved(self, dir, img_name):
        if img_name in os.listdir(dir):
            return True
        else:
            return False

    def create_img(self, image_path, size, k):
        img_name = str(size) + '_' + str(k) + '.png'
        imarray = numpy.random.rand(size, size, 3) * 255
        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save(os.path.join(image_path, img_name))
        wait(self.check_img_saved, error=AssertionError, check=True, dir=image_path, img_name=img_name)
        return img_name

    def upload_carousel(self, image_path):
        k = 0
        for locator in ((target_locators.CampaignPageLocators.CAROUSEL_1_LOCATOR, target_locators.CampaignPageLocators.LINK_FOR_SLIDE_1_LOCATOR, target_locators.CampaignPageLocators.HEADING_FOR_SLID_1_LOCATOR),
                        (target_locators.CampaignPageLocators.CAROUSEL_2_LOCATOR, target_locators.CampaignPageLocators.LINK_FOR_SLIDE_2_LOCATOR, target_locators.CampaignPageLocators.HEADING_FOR_SLID_2_LOCATOR),
                        (target_locators.CampaignPageLocators.CAROUSEL_3_LOCATOR, target_locators.CampaignPageLocators.LINK_FOR_SLIDE_3_LOCATOR, target_locators.CampaignPageLocators.HEADING_FOR_SLID_3_LOCATOR)):
            self.click(locator[0])
            k += 1
            img_name = self.create_img(image_path, 600, k)
            input_field = self.find(target_locators.CampaignPageLocators.UPLOAD_IMG_600_LOCATOR)
            input_field.send_keys(os.path.join(image_path, img_name))
            self.logger.debug(f'Image {img_name} is uploaded')
            self.input_data(locator[1], 'vk.com')
            self.input_data(locator[2], 'Slide'+str(k))

        img_name = self.create_img(image_path, 256, k=0)
        input_field = self.find(target_locators.CampaignPageLocators.UPLOAD_IMG_256_LOCATOR)
        input_field.send_keys(os.path.join(image_path, img_name))
        self.logger.debug(f'Image {img_name} is uploaded')

    def create_new_company(self, image_path):
        COMPANY_NAME = "Рекламная компания от " + str(datetime.now()) + ' №' + str(randint(1, 1000))
        self.logger.info(f'Inputting text data for {COMPANY_NAME}')
        with allure.step(f'Inputting text data for {COMPANY_NAME}'):
            self.wait_spinner()
            self.click(target_locators.CampaignPageLocators.TRAFFIC_BUTTON_LOCATOR)
            self.input_data(target_locators.CampaignPageLocators.INPUT_URL_LOCATOR, 'vk.com')
            self.input_data(target_locators.CampaignPageLocators.INPUT_COMPANY_NAME_LOCATOR, COMPANY_NAME)
            self.input_data(target_locators.CampaignPageLocators.INPUT_DAILY_LOCATOR, '100')
            self.input_data(target_locators.CampaignPageLocators.INPUT_TOTAL_LOCATOR, '100')
            self.wait(timeout=10).until(EC.element_to_be_clickable(target_locators.CampaignPageLocators.CAROUSEL_LOCATOR)).click()
            self.input_data(target_locators.CampaignPageLocators.MAIN_HEADING_LOCATOR, 'My target project')
            self.input_data(target_locators.CampaignPageLocators.MAIN_TEXT_LOCATOR, 'My target project for this site')

        self.logger.info('Uploading images')
        with allure.step('Uploading images'):
            self.upload_carousel(image_path)

        self.logger.info('Saving project')
        with allure.step('Saving project'):
            # По пречини того, что изображения могут не сразу подгрузиться, ретраем кнопку "Сохранить проект" через wait
            wait(self.check_for_create_project, error=AssertionError, timeout=60, check=True, spinner=False,
                 locator_for_click=target_locators.CampaignPageLocators.SAVE_PROJECT_LOCATOR,
                 locator_for_check=target_locators.CampaignPageLocators.PREVIEW_COMPANY_LOCATOR)
        self.logger.info('Creating project')
        with allure.step('Creating project'):
            # Возможна ошибка, при которой компания не создается при первом нажатии на кнопку, для этого также ретраем
            wait(self.check_for_create_project, error=AssertionError, timeout=60, check=True, spinner=True,
                 locator_for_click=target_locators.CampaignPageLocators.CREATE_COMPANY_LOCATOR,
                 locator_for_check=target_locators.CampaignPageLocators.NAME_OF_COMPANY_LOCATOR)

        self.logger.info('Assert project')
        with allure.step('Assert project'):
            assert COMPANY_NAME in self.driver.page_source

        self.logger.info('Deleting project')
        with allure.step('Deleting project'):
            # Убеждаемя, что компания удалена (были случаи, когда она не удалялась с первого раза)
            wait(self.check_delete_company, error=AssertionError, timeout=60, check=True,
                 name_of_company=COMPANY_NAME)

    def check_for_create_project(self, locator_for_click, locator_for_check, spinner):
        try:
            if self.driver.current_url.startswith(urls.URL_CAMPANING):
                self.click(locator_for_click)
            if spinner:
                self.wait_spinner()
            self.wait(timeout=3).until(EC.element_to_be_clickable(locator_for_check))
            return True
        except:
            return False

    def check_delete_company(self, name_of_company):
        company = self.find((By.XPATH, f'//*[@title= "{name_of_company}"]/parent::div/parent::div'))
        number = company.get_attribute("data-test").split(' ')[0]
        self.click((By.XPATH, f'//*[contains(@data-test, "{number}")]//*[@type="checkbox"]'))
        self.click(target_locators.CampaignPageLocators.MENU_LOCATOR)
        self.click(target_locators.CampaignPageLocators.MENU_DELETE_LOCATOR)
        self.driver.refresh()
        self.wait_spinner()
        try:
            self.wait().until(EC.element_to_be_clickable(target_locators.CampaignPageLocators.EMPTY_NAME_OF_COMPANY_LOCATOR))
            if name_of_company not in self.driver.page_source:
                return True
            else:
                return False
        except:
            self.wait().until(EC.element_to_be_clickable(target_locators.CampaignPageLocators.NAME_OF_COMPANY_LOCATOR))
            if name_of_company not in self.driver.page_source:
                return True
            else:
                return False