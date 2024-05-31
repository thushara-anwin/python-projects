from selenium.webdriver.common.by import By

create_account_locator=(By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']")

first_name_locator=(By.CSS_SELECTOR, "input#firstname")
last_name_locator= (By.CSS_SELECTOR, "input#lastname")
email_locator= (By.CSS_SELECTOR, "input#email_address")
password_locator= (By.CSS_SELECTOR, "input#password")
confirmation_password_locator= (By.CSS_SELECTOR, "input#password-confirmation")
create_account_submit_button_locator=(By.CSS_SELECTOR, "button.action.submit.primary")

success_message_locator =(By.CSS_SELECTOR, "div[data-ui-id='message-success']")
error_message_duplicate_email_locator =(By.CSS_SELECTOR, "div[data-ui-id='message-error']")
error_confirm_password_locator= (By.CSS_SELECTOR, "div#password-confirmation-error")
firstname_error_locator= (By.CSS_SELECTOR, "div#firstname-error")
lastname_error_locator= (By.CSS_SELECTOR, "div#lastname-error")
email_error_locator= (By.CSS_SELECTOR, "input#email_address+div")
password_error_locator= (By.CSS_SELECTOR, "div#password-error")
confirm_password_error_locator= (By.CSS_SELECTOR, "input#password-confirmation+div")