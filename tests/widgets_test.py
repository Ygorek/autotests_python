import time

from pages.widgets_page import AccordianPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            third_title, third_content = accordian_page.check_accordian('third')
            second_title, second_content = accordian_page.check_accordian('second')
            first_title, first_content = accordian_page.check_accordian('first')

            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and first_content > 0
            assert third_title == 'Why do we use it?' and first_content > 0



