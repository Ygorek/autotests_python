import os
import time

from pytest_selenium import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators, zoomPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        #self.remove_footer()
        #self.zooming_page()

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        #self.element_is_visible(self.locators.GENDER).click()
        self.click_by_script(self.element_is_visible(self.locators.GENDER))
        #self.element_is_visible(self.locators.HOBBIES).click()
        self.click_by_script(self.element_is_visible(self.locators.HOBBIES))
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)

        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        # self.click_by_script(self.element_is_visible(self.locators.SELECT_STATE1))

        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)

        #self.click_by_script(self.element_is_visible(self.locators.SELECT_CITY1))


        # self.zooming_page()
        time.sleep(5)
        self.click_by_script(self.element_is_visible(self.locators.SUBMIT))
        #self.element_is_clickable(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data

class zoomPage(BasePage):
    locators = zoomPageLocators()

    def zooming(self):

        #WebDriverWait(self, 10).until(expected_conditions.visibility_of_element_located(self.locators.topics_xpath))
        #elem = self.element_is_present(self.locators.dBase_xpath)
        #self.execute_script("arguments[0].scrollIntoView(true);", elem)
        self.go_to_element(self.element_is_present(self.locators.topics_xpath))
        time.sleep(5)
        self.element_is_present(self.locators.topics_xpath).click()
        time.sleep(5)
        self.go_to_element(self.element_is_present(self.locators.states_xpath))
        self.element_is_visible(self.locators.states_xpath).click()
        time.sleep(10)


