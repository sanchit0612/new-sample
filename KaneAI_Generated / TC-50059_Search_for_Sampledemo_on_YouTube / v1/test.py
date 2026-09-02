
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time, requests, re, os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = XCUITestOptions()
options.set_capability("platformName", "ios")
options.browser_name = "Safari"

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.get("https://kaneai-playground.lambdatest.io/")
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

    # Step - 1 : Open google.com
    driver.get("https://google.com")
    driver.implicitly_wait(6)

    # Step - 2 : Open https://youtube.com
    driver.get("https://youtube.com")
    driver.implicitly_wait(6)

    # Step - 3 : Open google.com
    driver.get("https://google.com")
    driver.implicitly_wait(6)

    # Step - 4 : Open https://youtube.com
    driver.get("https://youtube.com")
    driver.implicitly_wait(6)

    # Step - 5 : Type ${sampledemo} in search field
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'sanchit':
            element.send_keys(char)
    else:
        element.send_keys('sanchit')

    driver.quit()
except Exception as e:
    driver.quit()
