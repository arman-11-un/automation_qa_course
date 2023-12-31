from selenium.webdriver.common.by import By


class TextBoxPageLokarors:
    # form fields

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')

    # YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    # IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    # NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    # OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
    FIRSTNAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]')
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH_INPUT = (By.XPATH, ' //input[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND = (By.XPATH, '//div[@class="rt-noData"]')
    COUNT_ROW_LIST = (By.XPATH, '//select[@aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.XPATH, '//span[@title="Edit"]')


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    # result
    SUCCESS_DOUBLE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.XPATH, '//p[@id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.XPATH, '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, '//a[@id="simpleLink"]')
    DYNAMIC_LINK = (By.XPATH, '//a[@id="dynamicLink"]')
    CREATED_LINK = (By.XPATH, '//a[@id="created"]')
    NO_CONTENT = (By.XPATH, '//a[@id="no-content"]')
    MOVED = (By.XPATH, '//a[@id="moved"]')
    BAD_REQUEST = (By.XPATH, '//a[@id="bad-request"]')
    UNAUTHORIZED = (By.XPATH, '//a[@id="unauthorized"]')
    FORBIDDEN = (By.XPATH, '//a[@id="forbidden"]')
    NOT_FOUND = (By.XPATH, '//a[@id="invalid-url"]')

