from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=6):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=15):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
            action = ActionChains(self.driver)
            action.double_click(element)
            action.perform()

    def action_right_click(self, element):
            action = ActionChains(self.driver)
            action.context_click(element)
            action.perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script(" document.getElementById('close-fixedban').remove();")
        #self.driver.execute_script("document.body.style.zoom = '0.5'")
        # self.driver.execute_script("document.body.style.zoom='zoom %67';")
        #executeScript("document.body.style.zoom = '1.5'")

    def zooming_page(self):
        self.driver.execute_script("document.body.style.zoom = '0.5'")

    def action_intercepted(self, element):
        intercepted = ActionChains(self.driver)
        intercepted.move_to_element(element)
        intercepted.click(element)
        intercepted.perform()

        # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
        #webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
    def ctrl_minus(self, element):
        ctrlm = ActionChains(self.driver)
        ctrlm.key_down(Keys.CONTROL).send_keys("-").perform()


        # "webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
        # self.driver.execute_script("arguments[0].click();", element)




