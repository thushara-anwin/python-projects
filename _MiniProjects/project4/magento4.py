import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from locators import top_size,bottom_size,colors,options,address
def select_browser(browser):
    if browser.lower()=='chrome':
        driver1=webdriver.Chrome()
    elif browser.lower()=='firefox':
        driver1=webdriver.Firefox()
    elif browser.lower()=='edge':
        driver1=webdriver.Edge()
    return driver1

driver =select_browser('chrome')

#driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
actions= ActionChains(driver)

driver.get("https://magento.softwaretestingboard.com/")


def sign_in(email_id,pass_word):
    driver.find_element(By.LINK_TEXT,"Sign In").click()
    driver.find_element(By.CSS_SELECTOR,"input[name='login[username]'").send_keys(email_id)
    driver.find_element(By.CSS_SELECTOR,"input[name='login[password]']").send_keys(pass_word)
    driver.find_element(By.CSS_SELECTOR,"div.primary>button#send2>span").click()

women = driver.find_element(By.XPATH,options['women'])

tops = driver.find_element(By.CSS_SELECTOR,"a#ui-id-9")
bottoms = driver.find_element(By.CSS_SELECTOR,"a#ui-id-10")
#pants= driver.find_element(By.CSS_SELECTOR,"a#ui-id-15")
actions.move_to_element(women).move_to_element(tops).move_to_element(bottoms).click().perform()

driver.find_element(By.XPATH,"//span[@class='product-image-wrapper']/img[@alt='Erika Running Short']").click()#selecting item
driver.find_element(By.XPATH,bottom_size['28']).click()#size
driver.find_element(By.XPATH,colors['green']).click()#color
driver.find_element(By.CSS_SELECTOR,"button#product-addtocart-button").click()#add to cart
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a.action.showcart").click()#click cart
driver.find_element(By.CSS_SELECTOR,"button#top-cart-btn-checkout").click()#proceed to checkout
def mailing_address(address):
    email = driver.find_element(By.XPATH,"//fieldset[@id='customer-email-fieldset']//input[@class='input-text'and @id='customer-email']")
    email.send_keys(address[0])


    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name.send_keys(address[1])

    last_name = driver.find_element(By.XPATH,"//input[@name='lastname']")
    last_name.send_keys(address[2])

    company = driver.find_element(By.XPATH,"//input[@name='company']")
    company.send_keys(address[3])

    address1 = driver.find_element(By.XPATH,"//input[@name='street[0]']")
    address1.send_keys(address[4])

    address2 = driver.find_element(By.XPATH,"//input[@name='street[1]']")
    address2.send_keys(address[5])

    address3 = driver.find_element(By.XPATH,"//input[@name='street[2]']")
    address3.send_keys(address[6])

    city = driver.find_element(By.XPATH,"//input[@name='city']")
    city.send_keys(address[7])

    select_province = driver.find_element(By.XPATH,"//select[@name='region_id']")
    drp=Select(select_province)
    drp.select_by_visible_text('Louisiana')
    #select_province.click()
    #select_province.send_keys("l")
    #select_province.click()

    zip=driver.find_element(By.XPATH,"//input[@name='postcode']")
    zip.send_keys(address[8])
    """
    country = driver.find_element(By.XPATH,"//select[@name='country_id']")
    country.click()
    country.send_keys("U")
    country.click()
    """
    phone = driver.find_element(By.XPATH, "//input[@name='telephone']")
    phone.send_keys(address[9])


mailing_address(address)











#sign_in('thushara@gmail.com','south_middle_123')
time.sleep(3)
driver.close()


