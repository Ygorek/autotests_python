import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            third_title, third_content = accordian_page.check_accordian('third')
            second_title, second_content = accordian_page.check_accordian('second')
            first_title, first_content = accordian_page.check_accordian('first')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "Different title or no content"
            assert second_title == 'Where does it come from?' and second_content > 0, "Different title or no content"
            assert third_title == 'Why do we use it?' and third_content > 0, "Different title or no content"

        def test_accordian1(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "Different title or no content"

        def test_accordian2(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            second_title, second_content = accordian_page.check_accordian('second')
            assert second_title == 'Where does it come from?' and second_content > 0, "Different title or no content"

        def test_accordian3(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            third_title, third_content = accordian_page.check_accordian('third')
            assert third_title == 'Why do we use it?' and third_content > 0, "Different title or no content"

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            print(colors)
            print(colors_result)
            assert colors == colors_result, "colors are not the same"


        def test_remove_value_from_multi(self,driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            print(count_value_before)
            print(count_value_after)
            assert count_value_before != count_value_after, "colors are the same"

        def test_fill_single_autocomplete(self,driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            print(color)
            print(color_result)
            assert color == color_result, "colors are not the same"