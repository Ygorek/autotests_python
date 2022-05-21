import random
import time

from selenium.webdriver.common.by import By


class FormPageLocators:
    BODY = (By.TAG_NAME, "body")
    HTML = (By.TAG_NAME, "html")
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    SELECT_STATE1 = (By.XPATH, '//*[@id="state"]/div')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    SELECT_CITY1 = (By.XPATH, '//*[@id="city"]/div/div[2]/div')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    SUBMIT1 = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[11]/div/button")

    #TABLE RESULTS
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")

class zoomPageLocators:

    topics_xpath = (By.XPATH, "//div[@class='divTopicsSection1']//span//label[text()='All Topics']")
    states_xpath = (By.XPATH, "//div[@class='divStatesSection1']//span//label[text()='All States']")
    dBase_xpath = (By.XPATH, "//h4[text()='Searchable Database']")
