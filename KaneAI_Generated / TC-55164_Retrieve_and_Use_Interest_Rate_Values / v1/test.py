
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
    driver.implicitly_wait(6)

    # Step - 1 : Open URL https://www.mortgagecalculator.org
    driver.get("https://www.mortgagecalculator.org/")
    driver.implicitly_wait(6)

    # Step - 2 : Check current page URL text → {{current_url}}
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 3 : executing assertion
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 4 : Get value of interest rate → 6
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        interest_rate = result
    
    print("interest_rate:", interest_rate)
    driver.implicitly_wait(6)

    # Step - 5 : Get value of interest rate → {{global.interest_rate_float}}
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        interest_rate_float = result
    
    print("interest_rate_float:", interest_rate_float)
    driver.implicitly_wait(6)

    # Step - 6 : Open new tab
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(6)

    # Step - 7 : Type 6 in input field
    element_locators = ["//textarea[@name='q' and @role='combobox']", "//textarea[@name='q' and @aria-label='Search']", '[name="q"][role="combobox"]', '[role="combobox"][aria-label="Search"]', '[name="q"][aria-label="Search"]', '[aria-label="Search"]', "//textarea[@role='combobox' and @aria-label='Search']", "//textarea[starts-with(@aria-label,'Searc')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in '6':
            element.send_keys(char)
    else:
        element.send_keys('6')
    driver.implicitly_wait(6)

    # Step - 8 : Open new tab
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(6)

    # Step - 9 : Type 6 in input field
    element_locators = ["//textarea[@name='q' and @role='combobox']", "//textarea[@name='q' and @aria-label='Search']", '[name="q"][role="combobox"]', '[role="combobox"][aria-label="Search"]', '[name="q"][aria-label="Search"]', '[aria-label="Search"]', "//textarea[@role='combobox' and @aria-label='Search']", "//textarea[starts-with(@aria-label,'Searc')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in '6':
            element.send_keys(char)
    else:
        element.send_keys('6')

    driver.quit()
except Exception as e:
    driver.quit()
