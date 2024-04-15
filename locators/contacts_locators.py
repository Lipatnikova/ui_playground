class ContactsLocators:
    # Menu
    SORT_BY = ('xpath', '//*[@aria-controls="simple-menu"]')
    # DATA_SORT = ('xpath', '//*[@id="simple-menu"]/div[3]/ul/li')
    SORT_BY_LAST_NAME = ('xpath', '//*[@data-sort="last_name"]')
    SORT_BY_FIRST_NAME = ('xpath', '//*[@data-sort="first_name"]')
    SORT_BY_LAST_SEEN = ('xpath', '//*[@data-sort="last_seen"]')
    DATA_SORT = [SORT_BY_FIRST_NAME]
    # DATA_SORT = [SORT_BY_LAST_NAME, SORT_BY_FIRST_NAME, SORT_BY_LAST_SEEN]
    EXPORT = ('xpath', '//*[@aria-label="Export"]')
    BTN_NEW_CONTACT = ('css selector', '.MuiToolbar-regular.css-bdvdm7 > div > a')

    # List contacts
    FULL_NAMES_CONTACTS = ('css selector', '.MuiListItemText-multiline.css-1xar93x > span')
    CONTACT = ('css selector', '.RaList-content.css-s18byi > ul > li> a')
