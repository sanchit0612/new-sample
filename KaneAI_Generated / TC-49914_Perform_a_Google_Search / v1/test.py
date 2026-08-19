
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

    # Step - 1 : Open https://google.com
    driver.get("https://google.com")
    driver.implicitly_wait(6)

    # Step - 2 : Type 'dsad' in input field
    element_locators = ["//textarea[@name='q' and @title='Search']", "//textarea[@title='Search' and @role='combobox']", '[name="q"][title="Search"]', '[title="Search"][aria-label="Search"]', '[title="Search"][role="combobox"]', '[title="Search"]', "//textarea[@title='Search' and @aria-label='Search']", "//textarea[starts-with(@title,'Searc')]", "//textarea[contains(@title,'Search')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'dsad':
            element.send_keys(char)
    else:
        element.send_keys('dsad')
    driver.implicitly_wait(6)

    # Step - 3 : Click search button
    element_locators = ['[role="search"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(5) > div:nth-child(14) > center:nth-child(2) > input:nth-child(1)', '//body/div[2]/div[6]/form[1]/div[1]/div[1]/div[3]/div[4]/div[5]/center[1]/input[1]']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
