import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage
from confTest import driver





class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_from()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_resalt()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes hav not been selected'

    class TestRadioButton:

        def test_radiо_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', '"Yes" have not been selected'
            assert output_impressive == 'Impressive', '"Impressive" have not been selected'
            assert output_no == 'No', '"No" have not been selected'

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.edd_new_person()
            tablr_result = web_table_page.check_new_added_person()
            print(new_person)
            print(tablr_result)
            assert new_person in tablr_result

        def test_web_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.edd_new_person()[random.randint(0, 5)]
            web_table_page.search_som_people(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'the person was not found in the table '

        def test_web_table_person_info_firstname(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.edd_new_person()[1]
            web_table_page.search_som_people(lastname)
            firstname = web_table_page.update_peron_firstname()
            row = web_table_page.check_search_person()

            assert firstname in row, 'the person has not been changed'

        def test_web_table_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            firstname = web_table_page.edd_new_person()[0]
            web_table_page.search_som_people(firstname)
            update_info = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert update_info in row, 'the person has not been changed'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.edd_new_person()[3]
            web_table_page.search_som_people(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()

            assert text == 'No rows found', 'User data is not deleted'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'the number of rows in the table has not been changed or incorrectly'

    class TestButtonPage:

        def test_different_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            print(double)
            print(right)
            print(click)
            assert double == "You have done a double click", 'The double click button wos not pressed'
            assert right == "You have done a right click", 'The right click button wos not pressed'
            assert click == "You have done a dynamic click", 'The dynamic click button wos not pressed'

"