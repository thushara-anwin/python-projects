import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://money.rediff.com/")

forex=driver.find_element(By.XPATH,"//div[@id='moremoney']//a[contains(text(),'Forex')]")
forex.click()



def currency_rate():
    currency=driver.find_elements(By.XPATH,"//div[@id='leftcontainer']//div/table")
    with open("currency_rate.txt",'w') as f:
            for i in range(len(currency)):
                f.write(currency[i].text)

def print_currency_rate():
    currency = driver.find_elements(By.XPATH, "//div[@id='leftcontainer']//div/table")
    for i in range(len(currency)):
        print(currency[i].text)

def currency_converter(amt,c1,c2=1):
    """
    Enter numbers 1 -22 for c1 and c2
    """

    currency_amt= driver.find_element(By.XPATH,"//input[@id='amt']")
    currency_amt.clear()
    currency_amt.send_keys(amt)
    first_country=driver.find_element(By.XPATH,f"//select[@id='cnfrm']//option[{c1}]")
    first_country.click()
    time.sleep(10)
    second_country=driver.find_element(By.XPATH,f"//select[@id='cnto']//option[{c2}]")
    second_country.click()
    convert = driver.find_element(By.XPATH,"//input[@value='Convert']")
    convert.click()
    result = driver.find_elements(By.XPATH, "//div[@id='resdiv']")
    for i in range (len(result)):
        print(result[i].text)



currency_rate()
print_currency_rate()
currency_converter(50,13,10)


mutual_fund = driver.find_element(By.XPATH,"//div[@id='moremoney']/ul/li[5]/a")
mutual_fund.click()

driver.find_element(By.XPATH,"//input[@name='radioBtn' and @value='L']").click()

quote=driver.find_element(By.XPATH,"//input[@id='srchword']")
quote.send_keys(" Tata Motor Ltd.")
quote.send_keys(Keys.ENTER)










time.sleep(10)
driver.close()