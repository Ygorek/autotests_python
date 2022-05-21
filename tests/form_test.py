import time

from pages.form_page import FormPage, zoomPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            # form_page = FormPage(driver, "chrome://settings/")
            # form_page.open()
            # driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            p = form_page.fill_form_fields()
            time.sleep(1)
            result = form_page.form_result()
            person_form = p.firstname + ' ' + p.lastname , p.email
            result_form = result[0], result[1]
            print(p)
            print(result)
            print(person_form)
            print(result_form)
            assert person_form == result_form, "Разные данные"