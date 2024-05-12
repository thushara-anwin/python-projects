import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://magento.softwaretestingboard.com/")
item_list=[]

def options(opt):
    if opt == 'new':
        driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-3' ]").click()
    elif opt=='women':
        driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-4' ]").click()
    elif opt == 'men':
        driver.find_element(By.XPATH, "//a[@class='level-top ui-corner-all' and  @id='ui-id-5' ]").click()
    elif opt=='gear':
         driver.find_element(By.XPATH, "//a[@class='level-top ui-corner-all' and  @id='ui-id-6' ]").click()
    elif opt =='training':
        driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-7' ]").click()
    else:
        print("Wrong choice")

def items(xpath):
    driver.find_element(By.XPATH,xpath).click()

def select_item(xpath):
    driver.find_element(By.XPATH,xpath).click()




def top_size(size):
    if size == 'xs':
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-166']").click()
    elif size=='s':
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-167']").click()
    elif size=='m':
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-168']").click()
    elif size=='l':
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-169']").click()
    elif size =='xl':
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-170']").click()
    else:
        print("Wrong choice")

def bottom_size(size):
    if size == 28:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-171']").click()
    elif size == 29:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-172']").click()
    elif size == 30:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-173']").click()

    elif size == 31:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-174']").click()
    elif size == 32:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-175']").click()
    elif size == 33:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-176']").click()
    elif size == 34:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-177']").click()
    elif size == 36:
        driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-178']").click()


def color(color):
    if color== 'white':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-59']").click()
    elif color == 'black':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-49']").click()
    elif color == 'grey':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-52']").click()
    elif color == 'blue':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-50']").click()
    elif color =='purple':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-57']").click()
    elif color =='yellow':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-60']").click()
    elif color =='orange':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-56']").click()
    elif color =='red':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-58']").click()
    elif color == 'brown':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-51']").click()
    elif color == 'green':
        driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-53']").click()
    else:
        print("Color not available")


def add_to_cart():
    add_to_cart = driver.find_element(By.XPATH,"//button[@type='submit' and @id='product-addtocart-button']")
    add_to_cart.click()
    time.sleep(2)



def mailing_address():
    email = driver.find_element(By.XPATH,"//fieldset[@id='customer-email-fieldset']//input[@class='input-text'and @id='customer-email']")
    email.send_keys("demo@gmail.com")


    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name.send_keys("Rickey")

    last_name = driver.find_element(By.XPATH,"//input[@name='lastname']")
    last_name.send_keys("Marten")

    company = driver.find_element(By.XPATH,"//input[@name='company']")
    company.send_keys("ABC Technologies")

    address1 = driver.find_element(By.XPATH,"//input[@name='street[0]']")
    address1.send_keys("23455")

    address2 = driver.find_element(By.XPATH,"//input[@name='street[1]']")
    address2.send_keys("Park view Ave")

    address3 = driver.find_element(By.XPATH,"//input[@name='street[2]']")
    address3.send_keys("Alice Rd")

    city = driver.find_element(By.XPATH,"//input[@name='city']")
    city.send_keys("Clive")

    select_province = driver.find_element(By.XPATH,"//select[@name='region_id']")
    select_province.click()
    select_province.send_keys("l")
    select_province.click()

    zip=driver.find_element(By.XPATH,"//input[@name='postcode']")
    zip.send_keys("70081")
    """
    country = driver.find_element(By.XPATH,"//select[@name='country_id']")
    country.click()
    country.send_keys("U")
    country.click()
    """


    phone = driver.find_element(By.XPATH,"//input[@name='telephone']")
    phone.send_keys("56_879_890")

def click_cart():
    driver.find_element(By.XPATH, "//a[@class='action showcart']").click()

def check_out():
    driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()

def shipping_method(xpath):
    shipping_method = driver.find_element(By.XPATH, xpath)
    shipping_method.click()
def place_order():
    place_order = driver.find_element(By.XPATH,"//button[@title='Place Order']")
    place_order.click()

def order_summary():
    summary = driver.find_elements(By.XPATH, "//div[@class='opc-block-summary']")
    with open("summary.txt", 'w') as f:
        for i in range(len(summary)):
            f.write(summary[i].text)




def print_order_summary():
    print("Order Summary")
    print("------------------")
    summary = driver.find_elements(By.XPATH, "//div[@class='opc-block-summary']")
    for i in range(len(summary)):
        print(summary[i].text)




def billing_address():
    address = driver.find_elements(By.XPATH, "//div[@class='billing-address-details']")
    with open("billing_address.txt", 'w') as f:
        for i in range(len(address)):
            f.write(address[i].text)


def print_billing_address():
    print("Billing Address")
    print("____________________")
    address = driver.find_elements(By.XPATH, "//div[@class='billing-address-details']")
    for i in range(len(address)):
                print(address[i].text)


options('women')
items("//a[text()='Jackets']")
select_item("//a[contains(text(), 'Juno Jacket ')]")
top_size('m')
color('blue')
add_to_cart()

options('women')
items("//a[contains(text(),'Tees')]")
select_item("//a[contains(text(),'Gwyn Endurance Tee')]")
top_size('m')
color('yellow')
add_to_cart()


options('women')
items("//a[text()='Pants']")
select_item("//strong[@class='product name product-item-name']//parent::a[@href='https://magento.softwaretestingboard.com/ida-workout-parachute-pant.html']")
bottom_size(29)
color('black')
add_to_cart()

options('men')
items("//a[text()='Hoodies & Sweatshirts']")
select_item("//*[contains(text(),'Ajax Full-Zip Sweatshirt')]")
color('blue')
top_size('xl')
add_to_cart()

options('men')
items("//a[contains(text(),'Tanks')]")
select_item("//a[contains(text(),'Sparta Gym')]")
color('green')
top_size('xl')
add_to_cart()


options('gear')
items("//div[@class='block filter']//following::a[text()='Bags'][2]")
select_item("//img[@alt='Fusion Backpack']")
add_to_cart()


options('training')
options('sale')

click_cart()


time.sleep(6)

check_out()

##################### Shipping Address #############
mailing_address()


shipping_method("//td[@id='label_method_bestway_tablerate']")

next=driver.find_element(By.XPATH,"//span[text()='Next']")
next.click()
time.sleep(10)

################ PLACING ORDER ###############
place_order()
order_summary()
print_order_summary()
billing_address()
print_billing_address()


time.sleep(6)
driver.close()