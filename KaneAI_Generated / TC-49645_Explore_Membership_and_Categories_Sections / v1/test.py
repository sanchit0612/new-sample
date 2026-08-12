
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

    # Step - 1 : Open https://uat.marinabaysands.com/museum/artscience-friends-order.html
    driver.get("https://uat.marinabaysands.com/museum/artscience-friends-order.html")
    driver.implicitly_wait(6)

    # Step - 2 : Scroll in document
    driver.execute_script("window.scrollBy(0, 374)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 3 : Scroll in document
    driver.execute_script("window.scrollBy(0, 480)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 4 : Right click on Membership description paragraph
    element_locators = ["//i[text()='ArtScience Friends']/ancestor::p[1]", "//i[text()='ArtScience Friends']/ancestor::p[1]", 'body > div:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(1)', '//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/p[1]']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Scroll in document
    driver.execute_script("window.scrollBy(0, 364)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 6 : Scroll in document
    driver.execute_script("window.scrollBy(0, 0)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 7 : Click and drag Categories section
    element_locators = ["//h3[text()='Categories']/ancestor::div[2]", "//h3[text()='Categories']/ancestor::div[2]", "//h3[contains(text(),'Categories')]/ancestor::div[2]", 'body > div:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6)', '//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[6]']
    element = get_element(driver,element_locators)

    element_locators = ["//h3[text()='Categories']/ancestor::div[2]", "//h3[text()='Categories']/ancestor::div[2]", "//h3[contains(text(),'Categories')]/ancestor::div[2]", 'body > div:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6)', '//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[6]']
    element = get_element(driver,element_locators)
    driver.implicitly_wait(6)

    # Step - 8 : Scroll in document
    driver.execute_script("window.scrollBy(0, 224)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 9 : Scroll in document
    driver.execute_script("window.scrollBy(0, 1012)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 10 : Scroll in document
    driver.execute_script("window.scrollBy(0, 480)")
    time.sleep(1)

    driver.quit()
except Exception as e:
    driver.quit()
