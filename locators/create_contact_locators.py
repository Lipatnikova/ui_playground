class CreateContactLocators:
    # Header
    FULL_NAME = ("xpath", '//*[@id="root"]/div/div/nav/header/div/div/div[3]/div/button/span[1]')

    # Body
    FIRST_NAME = ('css selector', '#first_name')
    LAST_NAME = ('css selector', '#last_name')
    TITLE = ('css selector', '#title')
    EMAIL = ('css selector', '#email')
    ACCOUNT_MANAGER = ('xpath', '//*[@id="sales_id"]')
    MANAGER_NAME = ('xpath', '//li[normalize-space()="Jane Doe"]')
    BTN_SAVE = ('xpath', '//*[@id="main-content"]/div/div/form/div/div[2]/div/button')
