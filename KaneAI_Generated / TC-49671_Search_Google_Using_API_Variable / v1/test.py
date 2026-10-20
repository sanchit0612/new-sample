
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : open https://kaneai-playground.lambdatest.io/
    driver.get("https://kaneai-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : executing api
    response = requests.post(url='https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'},data="{\r\n    \"id\": 123456,\r\n    \"category\": {\r\n      \"id\": 1,\r\n      \"name\": \"Dogs\"\r\n    },\r\n    \"name\": \"DemoDog\",\r\n    \"photoUrls\": [\r\n      \"https://example.com/dog.jpg\"\r\n    ],\r\n    \"tags\": [\r\n      {\r\n        \"id\": 1,\r\n        \"name\": \"demo\"\r\n      }\r\n    ],\r\n    \"status\": \"available\"\r\n  }", params={},timeout=10000)
    print("Content for the api is ",response.status_code)
    driver.implicitly_wait(6)

    # Step - 3 : Open https://google.com
    driver.get("https://google.com")
    driver.implicitly_wait(6)

    # Step - 4 : Type DemoDog in search box
    element_locators = ["//textarea[@name='q' and @title='Search']", "//textarea[@title='Search' and @role='combobox']", '[name="q"][title="Search"]', '[title="Search"][aria-label="Search"]', '[title="Search"][role="combobox"]', '[title="Search"]', "//textarea[@title='Search' and @aria-label='Search']", "//textarea[starts-with(@title,'Searc')]", "//textarea[contains(@title,'Search')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'DemoDog':
            element.send_keys(char)
    else:
        element.send_keys('DemoDog')

    driver.quit()
except Exception as e:
    driver.quit()
