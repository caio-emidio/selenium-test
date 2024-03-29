# coding: UTF-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

baseURL = "http://www.amazon.com"
baseSearch = "Nikon"
assert_element = "Nikon D3X"

#Chrome Path
chrome_path = '/usr/bin/google-chrome'


#Start Browser
browser = webdriver.Chrome(executable_path=chrome_path)
wait = WebDriverWait(browser, 10)

#Open Amazon
browser.get(baseURL)

#Search of Canon
prod = browser.find_element_by_id("twotabsearchtextbox")
prod.send_keys(baseSearch)
browser.find_element_by_xpath("//input[@value='Go']").click();

select = Select(browser.find_element_by_id('s-result-sort-select'))
select.select_by_value('price-desc-rank')

#Newest Arrivals - change to 'date-desc-rank'
#Avg. Customer Review - change to 'review-rank'
#High to low - change to 'price-desc-rank'
#Low to high - change to 'price-asc-rank'

#Select 2 product
list_of_products = browser.find_elements_by_css_selector('span.a-text-normal')
list_of_products[1].click()

#Verify Product Title
product_title = browser.find_element_by_xpath('//span[@id="productTitle"]')
print(product_title.text)
assert  assert_element in product_title.text, "FAIL: " + assert_element + " not in Search."
print("SUCCESS: " + assert_element + " in Search")
browser.close()
