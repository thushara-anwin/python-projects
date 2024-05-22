import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains




def select_browser(browser):
    if browser.lower()=='chrome':
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option('detach', True)
        d=webdriver.Chrome(options=opts)
    elif browser.lower()=='firefox':
        d=webdriver.Firefox()
    elif browser.lower()=='edge':
        d=webdriver.Edge()
    return d

driver=select_browser('chrome')
wait=WebDriverWait(driver,10,2)
driver.maximize_window()
driver.implicitly_wait(10)
actions =ActionChains(driver)
driver.get("https://tutorialsninja.com/demo/")
wait = WebDriverWait(driver,10,2)

def select_laptops_and_notebooks():
    laptops_notebooks=driver.find_element(By.XPATH,"//a[(text()='Laptops & Notebooks')]")
    mac =driver.find_element(By.XPATH,"//a[(text()='Macs (0)')]")
    windows =driver.find_element(By.XPATH,"//a[(text()='Windows (0)')]")
    show_all= driver.find_element(By.XPATH,"//a[text()='Show AllLaptops & Notebooks']")

    actions.move_to_element(laptops_notebooks).move_to_element(mac).move_to_element(windows).move_to_element(show_all).click().perform()



#select_laptops_and_notebooks()
macbook=driver.find_element(By.XPATH,"//img[@alt='MacBook']")
macbook.click()
def click_images():
    images = driver.find_elements(By.CSS_SELECTOR,"a.thumbnail>img[title='MacBook']")
    images[0].click()
    time.sleep(2)
    for i in range(len(images)):
        if i == 3:
            driver.save_screenshot('laptop_image.png')
        try:
            next = wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")))
            next.click()
        except Exception as e:
            print(e)
        time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"button[title='Close (Esc)']").click()

#click_images()



js = "document.getElementById('button-cart').click();"
driver.execute_script(js)

desktops = driver.find_element(By.LINK_TEXT,"Desktops")

driver.execute_script("arguments[0].click();",desktops)

tablets = driver.find_element(By.LINK_TEXT,"Tablets")
driver.execute_script("arguments[0].click()",tablets)
time.sleep(5)
"""
search1=driver.find_element(By.NAME,"search")
search1.send_keys("ipad")
search1_click = driver.find_element(By.XPATH,"//div[@id='search']//button[@type='button']")
driver.execute_script("arguments[0].click();",search1_click)
"""
search ="document.getElementsByName('search').value='ipad';"
driver.execute_script(search)


#items= driver.find_elements(By.XPATH,"//div[@class='list-group']/a")
#driver.execute_script("arguments[0].click();",items)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")










time.sleep(5)
#driver.close()