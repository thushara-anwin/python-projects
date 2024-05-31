from selenium.webdriver.common.by import By

sign_in_locator = (By.CSS_SELECTOR, "li.authorization-link>a")
email_field_locator = (By.CSS_SELECTOR, "input#email")
password_field_locator = (By.CSS_SELECTOR, "input[name='login[password]']")
sign_in_button_locator = (By.CSS_SELECTOR, "div+div>div.primary>button#send2")
sign_in_success_locator =(By.XPATH,"//span[contains(text(),'Welcome')]")
invalid_email_password_error_message_locator = (By.CSS_SELECTOR,"div[data-ui-id='message-error")
email_field_required_locator = (By.CSS_SELECTOR,"div#email-error")
password_field_required_locator=(By.CSS_SELECTOR,"div#pass-error")


