class ShowContactLocators:
    FULL_NAME = ('xpath', '//*[@class="MuiTypography-root MuiTypography-h5 css-zq6grw"]')
    TITLE = ('xpath', '//*[@id="main-content"]/div/div[1]/div/div/div/div[2]/p')
    TEXTAREA = ('tag name', "textarea")
    SELECT_STATUS = ('css selector', '.MuiTextField-root.css-o70mjd')
    SELECT_VALUE = ('xpath', '//*[@id="menu-"]/div[3]/ul/li')
    CALENDAR = ('xpath', '//*[@type="datetime-local"]')
    BTN_ADD_THIS_NOTE = ('css selector', '.css-1dqn28w > button')
    LAST_NOTE = ('css selector', '.MuiBox-root.css-1rr4qq7 > p')
