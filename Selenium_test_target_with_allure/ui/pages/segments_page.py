from datetime import datetime
from random import randint

import allure
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators import target_locators
from ui import urls

class SegmentsPage(BasePage):
    url = urls.URL_SEGMENT
    locators = target_locators.SegmentsPageLocators()

    def create_new_segment(self, SEGMENT_NAME):
        self.logger.info(f'Create segment {SEGMENT_NAME}')
        with allure.step(f'Create segment {SEGMENT_NAME}'):
            self.wait_spinner()
            try:
                self.click(target_locators.SegmentsPageLocators.NEW_SEGMENT_LOCATOR_1, timeout=5)
            except:
                self.click(target_locators.SegmentsPageLocators.NEW_SEGMENT_LOCATOR_2)
            self.click(target_locators.SegmentsPageLocators.CHECKBOX_LOCATOR)
            self.click(target_locators.SegmentsPageLocators.ADD_BUTTON_LOCATOR)
            self.input_data(target_locators.SegmentsPageLocators.INPUT_SEGMENT_NAME_LOCATOR, SEGMENT_NAME)
            self.click(target_locators.SegmentsPageLocators.CREATE_BUTTON_LOCATOR)
            self.wait_spinner()
            self.wait(timeout=10).until(EC.element_to_be_clickable(target_locators.SegmentsPageLocators.NAME_OF_SEGMENT))

    def delete_segment(self, SEGMENT_NAME):
        self.logger.info('Delete segment')
        with allure.step('Delete segment'):
            segment = self.find((By.XPATH, f'//*[@title= "{SEGMENT_NAME}"]/parent::div/parent::div'))
            number = segment.get_attribute("data-test").split(' ')[1]
            self.click((By.XPATH, f'//*[contains(@data-test, "{number}")]/*[contains(@class, "cells-module-removeCell")]'))
            self.click(target_locators.SegmentsPageLocators.DELETE_BUTTON_LOCATOR)
            self.wait().until(EC.invisibility_of_element(target_locators.SegmentsPageLocators.DELETE_WINDOW_LOCATOR))

    def check_create_segment(self):
        SEGMENT_NAME = "Сегмент от " + str(datetime.now()) + ' №' + str(randint(1, 1000))
        self.create_new_segment(SEGMENT_NAME)
        self.logger.info('Assert create segment')
        with allure.step('Assert create segment'):
            assert SEGMENT_NAME in self.driver.page_source
        self.delete_segment(SEGMENT_NAME)

    def check_delete_segment(self):
        SEGMENT_NAME = "Сегмант от " + str(datetime.now()) + ' №' + str(randint(1, 1000))
        self.create_new_segment(SEGMENT_NAME)
        self.delete_segment(SEGMENT_NAME)
        self.logger.info('Assert delete segment')
        with allure.step('Assert delete segment'):
            assert SEGMENT_NAME not in self.driver.page_source