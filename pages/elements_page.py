import random
import time

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLokarors, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLokarors()

    def fill_all_fields(self):
        person_info = next(generated_person())

        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visibale(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visibale(self.locators.EMAIL).send_keys(email)
        self.element_is_visibale(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visibale(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visibale(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_from(self):
        full_name = self.element_is_visibale(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visibale(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visibale(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visibale(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visibale(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visibale(self.locators.ITEM_LIST)
        count = 25
        while count > 0:
            item = item_list[random.randint(1, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_resalt(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visibale(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def edd_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visibale(self.locators.ADD_BUTTON).click()
            self.element_is_visibale(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visibale(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visibale(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visibale(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visibale(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visibale(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visibale(self.locators.SUBMIT_BUTTON).click()
            count -= 1
        return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_som_people(self, key_word):
        self.element_is_visibale(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_peron_firstname(self):
        person_info = next(generated_person())
        firstname = person_info.firstname
        self.element_is_visibale(self.locators.UPDATE_BUTTON).click()
        self.element_is_visibale(self.locators.FIRSTNAME_INPUT).clear()
        self.element_is_visibale(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
        self.element_is_visibale(self.locators.SUBMIT_BUTTON).click()
        return firstname

    def update_person_info(self):
        person_info = next(generated_person())
        update_info = {'email': person_info.email, 'salary': person_info.salary,
                       'lastname': person_info.lastname, 'firstname': person_info.firstname,
                       'department': person_info.department, 'age': person_info.age}
        update_locator = {'email': self.locators.EMAIL_INPUT,
                          'salary': self.locators.SALARY_INPUT,
                          'lastname': self.locators.LASTNAME_INPUT, 'firstname': self.locators.FIRSTNAME_INPUT,
                          'department': self.locators.UPDATE_BUTTON, 'age': self.locators.AGE_INPUT, }
        update = random.choice(list(update_info.keys()))
        self.element_is_visibale(self.locators.UPDATE_BUTTON).click()
        self.element_is_visibale(update_locator[update]).clear()
        self.element_is_visibale(update_locator[update]).send_keys(update_info[update])
        self.element_is_visibale(self.locators.SUBMIT_BUTTON).click()
        return str(update_info[update])

    def delete_person(self):
        self.element_is_visibale(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visibale(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()

            self.element_is_visibale((By.CSS_SELECTOR, f'option[value="{x}"]'))
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == 'double':
            self.action_double_click(self.element_is_visibale(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == 'right':
            self.action_right_click(self.element_is_visibale(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == 'click':
            self.element_is_visibale(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text

    def click_on_double(self):
        self.action_double_click(self.element_is_visibale(self.locators.DOUBLE_BUTTON))
        return self.element_is_present(self.locators.SUCCESS_DOUBLE).text

    def click_on_right(self):
        self.action_right_click(self.element_is_visibale(self.locators.RIGHT_CLICK_BUTTON))
        return self.element_is_present(self.locators.SUCCESS_RIGHT).text

    def click_on(self):
        self.element_is_visibale(self.locators.CLICK_ME_BUTTON).click()
        return self.element_is_present(self.locators.SUCCESS_CLICK_ME).text
