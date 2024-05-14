import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome

opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)



driver =webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")


def login():
    user_name = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#password[name='password']")
    password.send_keys("secret_sauce")
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
    time.sleep(6)

def logout():
    driver.find_element(By.CSS_SELECTOR,"div>nav>a#logout_sidebar_link").click()



def add_to_cart():
    driver.find_element(By.CSS_SELECTOR,"button#add-to-cart").click()
def back_to_product():
    driver.find_element(By.CSS_SELECTOR,"div.header_secondary_container>div>button#back-to-products").click()

def click_item(selector):
    driver.find_element(By.CSS_SELECTOR,selector).click()
    add_to_cart()

def print_summary_info():
    print("Summary")
    print("___________________")
    summary=driver.find_elements(By.CSS_SELECTOR,"div[data-test^='header-']+div#checkout_summary_container>div>div+div.summary_info")
    for i in range (len(summary)):
        print(summary[i].text)

def summary_info():
    print("Summary")
    print("___________________")
    summary=driver.find_elements(By.CSS_SELECTOR,"div.summary_info")
    with open('summary_info','w') as file:
        for i in range(len(summary)):
            file.write(summary[i].text)


def finish():
    driver.find_element(By.CSS_SELECTOR,"div.summary_info>div>button#cancel+button[name='finish']").click()

def cancel_payment():
    driver.find_element(By.CSS_SELECTOR,"")

def print_cart_list():
    print("List Of Items in The Cart")
    print("________________________")
    cartlist =driver.find_elements(By.CSS_SELECTOR,"div>div[data-test^='header-']+div[data-test$='-container']>div>div.cart_list")
    for i in  range(len(cartlist)):
        print(cartlist[i].text)

def cart_list():
    print("List Of Items in The Cart")
    print("________________________")
    cartlist =driver.find_elements(By.CSS_SELECTOR,"div.cart_list")
    with open("list_of_items_in_the_cart",'w') as f:
        for i in  range(len(cartlist)):
            f.write(cartlist[i].text)







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
print_cart_list()
print_summary_info()
cart_list()
summary_info()
finish()


time.sleep(2)
#driver.close()

