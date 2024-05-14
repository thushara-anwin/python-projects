import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://magento.softwaretestingboard.com/")
item_list=[]

def options(opt):
    """" 3-new arrival 4-women 5-men 6- gear 7-training 8 sale"""
    driver.find_element(By.XPATH, f"//a[@class='level-top ui-corner-all' and  @id='ui-id-{opt}' ]").click()



def items(xpath):
    driver.find_element(By.XPATH,xpath).click()

def select_item(xpath):
    driver.find_element(By.XPATH,xpath).click()




def top_size(size_code):
    """ xs=166 s=167 m=168 l= 169 xl=170"""
    driver.find_element(By.XPATH, f"//div[@id='option-label-size-143-item-{size_code}']").click()

def bottom_size(size_no):
    #28=171,29=172,30=173,31=174,32=175,33=176,34=177,36=178:
        driver.find_element(By.XPATH, f"//div[@id='option-label-size-143-item-{size_no}']").click()

def color(color_no):
    #black=49 blue=50 brown=51 grey=52 green=53 orange = 56 purple=57 red=58 white=59 yellow=60
        driver.find_element(By.XPATH, f"//div[@id='option-label-color-93-item-{color_no}']").click()


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


options(4)
items("//a[text()='Jackets']")
select_item("//a[contains(text(), 'Juno Jacket ')]")
top_size(168)
color(50)
add_to_cart()

options(4)
items("//a[contains(text(),'Tees')]")
select_item("//a[contains(text(),'Gwyn Endurance Tee')]")
top_size(167)
color(60)
add_to_cart()


options(4)
items("//a[text()='Pants']")
select_item("//strong[@class='product name product-item-name']//parent::a[@href='https://magento.softwaretestingboard.com/ida-workout-parachute-pant.html']")
bottom_size(172)
color(49)
add_to_cart()

options(5)
items("//a[text()='Hoodies & Sweatshirts']")
select_item("//*[contains(text(),'Ajax Full-Zip Sweatshirt')]")
color(50)
top_size(169)
add_to_cart()

options(5)
items("//a[contains(text(),'Tanks')]")
select_item("//a[contains(text(),'Sparta Gym')]")
color(53)
top_size(169)
add_to_cart()


options(6)
items("//div[@class='block filter']//following::a[text()='Bags'][2]")
select_item("//img[@alt='Fusion Backpack']")
add_to_cart()


options(7)
options(8)

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