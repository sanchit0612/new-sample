
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

    # Step - 1 : Open https://mahametric.com/property/calculators/home-loan-emi
    driver.get("https://mahametric.com/property/calculators/home-loan-emi")
    driver.implicitly_wait(6)

    # Step - 2 : Scroll until 'Home Loan EMI & Affordability Calculator' is visible
    element_locators = ["//h2[text()='Home Loan EMI & Affordability Calculator']", "//h2[contains(text(),'Home Loan EMI & Affordability Calculator')]", '[aria-labelledby="emi-calculator-title"] > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1)', '[aria-labelledby="emi-calculator-title"] > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1)', '//body/div[3]/main[1]/div[1]/section[1]/div[1]/div[1]/h2[1]']
    element = get_element(driver,element_locators)

    element_locators = ["//h2[text()='Home Loan EMI & Affordability Calculator']", "//h2[contains(text(),'Home Loan EMI & Affordability Calculator')]", '[aria-labelledby="emi-calculator-title"] > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1)', '[aria-labelledby="emi-calculator-title"] > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1)', '//body/div[3]/main[1]/div[1]/section[1]/div[1]/div[1]/h2[1]']
    element = get_element(driver,element_locators)
    driver.implicitly_wait(6)

    # Step - 3 : Scroll until 'loan tenure' is visible
    element_locators = ['[aria-labelledby="emi-calculator-title"] > div:nth-child(3) > label:nth-child(4) > input:nth-child(2)', '[aria-labelledby="emi-calculator-title"] > div:nth-child(3) > label:nth-child(4) > input:nth-child(2)', '//body/div[3]/main[1]/div[1]/section[1]/div[3]/label[3]/input[1]']
    element = get_element(driver,element_locators)

    element_locators = ['[aria-labelledby="emi-calculator-title"] > div:nth-child(3) > label:nth-child(4) > input:nth-child(2)', '[aria-labelledby="emi-calculator-title"] > div:nth-child(3) > label:nth-child(4) > input:nth-child(2)', '//body/div[3]/main[1]/div[1]/section[1]/div[3]/label[3]/input[1]']
    element = get_element(driver,element_locators)
    driver.implicitly_wait(6)

    # Step - 4 : Get loan tenure value → 20
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        global_loan_tenure_value = result
    
    print("global_loan_tenure_value:", global_loan_tenure_value)
    driver.implicitly_wait(6)

    # Step - 5 : Type 20 in property price field
    element_locators = ['[aria-labelledby="emi-calculator-title"] > div:nth-child(3) > label:nth-child(1) > input:nth-child(2)', '[aria-labelledby="emi-calculator-title"] > div:nth-child(3) > label:nth-child(1) > input:nth-child(2)', '//body/div[3]/main[1]/div[1]/section[1]/div[3]/label[1]/input[1]']
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in '20':
            element.send_keys(char)
    else:
        element.send_keys('20')

    driver.quit()
except Exception as e:
    driver.quit()
