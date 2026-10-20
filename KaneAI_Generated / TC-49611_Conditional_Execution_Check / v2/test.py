
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
    _loop_counter_tdM0 = 1
    _max_iterations_tdM0 = 30
    while _loop_counter_tdM0 < _max_iterations_tdM0:
        user_variables["loop_counter"] = _loop_counter_tdM0
        _conditions_tdM0 = [ResolvedCondition.from_string(condition) for condition in ['{{x}} < 2']]
        _connectors_tdM0 = [ConcatenationOperator(connector) for connector in []]
        _condition_tdM0 = Condition(_conditions_tdM0, _connectors_tdM0)
        _result_tdM0, _ = _condition_tdM0.evaluate(user_variables, get_variable_value)
        if not _result_tdM0:
            break
        driver.implicitly_wait(6)

        # Step - 4 : {{x}} + 1 → {{x}}
        _loop_counter_tdM0 += 1
    if _loop_counter_tdM0 >= _max_iterations_tdM0:
        raise Exception("While loop exceeded maximum iterations (30)")
    driver.implicitly_wait(6)

    # Step - 5 : Wait 1 s
    time.sleep(int(1))

    driver.quit()
except Exception as e:
    driver.quit()
