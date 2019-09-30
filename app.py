from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

#Access amazon.com
driver.get("http://www.amazon.com")

#Search of Nikon
search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys('Nikon')
search.send_keys(Keys.RETURN)

driver.implicitly_wait(20)
#Select High to Low
botton = driver.find_element_by_css_selector('span.a-button-text.a-declarative')
botton.click()
#botton.sendKeys(Keys.DOWN)


#Select 2 product
list_of_products = driver.find_elements_by_css_selector('span.a-text-normal')
list_of_products[1].click()

#Verify Product Title
product_title = driver.find_element_by_xpath('//span[@id="productTitle"]')
print(product_title.text)
assert "Nikon D3X" in product_title.text

driver.close()
