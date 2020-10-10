from selenium import webdriver
ChromeDriver = "D:\\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriver)
def return_driver():
    return driver

def open_base_url(url):
    driver.get(url)

def find_id(element_id):
    return driver.find_element_by_id(id)

def find_name(element_name):
    return driver.find_element_by_name(element_name)

def find_CSS(element_CSS):
    return driver.find_element_by_css_selector(element_CSS)

def find_Xpath(element_Xpath):
    return driver.find_element_by_xpath(element_Xpath)

def js(element_js):
    return driver.execute_script()

