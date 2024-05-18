import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from username_password import user1,pass_word

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")


def login():
    user_name = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#user-name")
    user_name.send_keys(user1)
    password = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#password[name='password']")
    password.send_keys(pass_word)
    time.sleep(5)
    login=driver.find_element(By.CSS_SELECTOR,"div.form_group+div+div+input#login-button").click()
    time.sleep(5)

def select():
    select=driver.find_element(By.CSS_SELECTOR,"select[data-test='product-sort-container']")
    select.send_keys('p')


def select_item(item):
    item_select = driver.find_element(By.CSS_SELECTOR,item)
    item_select.click()

def cart():
    driver.find_element(By.CSS_SELECTOR,"div.primary_header>div#menu_button_container+div+div#shopping_cart_container").click()
    time.sleep(5)


def continue_shopping():
    driver.find_element(By.CSS_SELECTOR,"button[name$='-shopping']>img.back-image[alt='Go back']").click()
    time.sleep(5)

def checkout():
    driver.find_element(By.CSS_SELECTOR,"div>button#checkout").click()
    time.sleep(2)

def address():
    first_name=driver.find_element(By.CSS_SELECTOR,"input[class ='input_error form_input']#first-name").send_keys('Thushara')
    last_name=driver.find_element(By.CSS_SELECTOR, "div>div>input#last-name").send_keys("Anu")
    zip_code=driver.find_element(By.CSS_SELECTOR, "div.form_group>input#postal-code").send_keys("2345")
    continue_checkout=driver.find_element(By.CSS_SELECTOR, "div>input#continue").click()
    time.sleep(5)

def logout():
    driver.find_element(By.CSS_SELECTOR,"div>nav>a#logout_sidebar_link").click()



def add_to_cart():
    driver.find_element(By.CSS_SELECTOR,"button#add-to-cart").click()
def back_to_product():
    driver.find_element(By.CSS_SELECTOR,"div.header_secondary_container>div>button#back-to-products").click()

def click_item(selector):
    driver.find_element(By.CSS_SELECTOR,selector).click()
    add_to_cart()




login()
select()
select_item("button#add-to-cart-sauce-labs-onesie")
select_item("div>div>button[name='add-to-cart-sauce-labs-bike-light']")
cart()
continue_shopping()
click_item("div[class^='inventory_i'] a#item_1_title_link>div.inventory_item_name ")
#add_to_cart=driver.find_element(By.XPATH,"div>button#add-to-cart[name='add-to-cart'][data-test$='-cart']")
#add_to_cart()
back_to_product()
cart()

checkout()
address()


time.sleep(2)
driver.close()

