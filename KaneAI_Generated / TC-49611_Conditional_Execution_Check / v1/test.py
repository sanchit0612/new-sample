
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

    # Step - 2 : Set x = 1
    x = "1"
    driver.implicitly_wait(6)

    # Step - 3 : If {{x}} < 2
    # While loop: If {{x}} < 2
    _loop_counter_XR4p = 1
    _max_iterations_XR4p = 30
    while _loop_counter_XR4p < _max_iterations_XR4p:
        user_variables["loop_counter"] = _loop_counter_XR4p
        _conditions_XR4p = [ResolvedCondition.from_string(condition) for condition in ['{{x}} < 2']]
        _connectors_XR4p = [ConcatenationOperator(connector) for connector in []]
        _condition_XR4p = Condition(_conditions_XR4p, _connectors_XR4p)
        _result_XR4p, _ = _condition_XR4p.evaluate(user_variables, get_variable_value)
        if not _result_XR4p:
            break
        driver.implicitly_wait(6)

        # Step - 4 : {{x}} + 1 → {{x}}
        _loop_counter_XR4p += 1
    if _loop_counter_XR4p >= _max_iterations_XR4p:
        raise Exception("While loop exceeded maximum iterations (30)")

    driver.quit()
except Exception as e:
    driver.quit()
