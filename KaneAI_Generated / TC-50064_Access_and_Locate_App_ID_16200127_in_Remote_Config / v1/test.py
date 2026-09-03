
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time, traceback

options = UiAutomator2Options()
options.set_capability("platformName", "android")

driver = webdriver.Remote("http://localhost:4723", options=options)
try:

    def get_element(driver, locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element("xpath", locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = "xpath"
                selector = locator.get('selector', locator) if isinstance(locator, dict) else locator
                try:
                    element = driver.find_element(by_method, selector)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None
    driver.implicitly_wait(6)

    # Step - 1 : Type acf@cloudranger.cn in username field
    element_locators = ['//android.view.ViewGroup[@content-desc="Email"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        pass
    element.clear()
    element.send_keys('acf@cloudranger.cn')
    driver.implicitly_wait(6)

    # Step - 2 : Type password Crit@1234
    element_locators = ['//android.view.ViewGroup[@content-desc="Password"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        pass
    element.clear()
    element.send_keys('Crit@1234')
    driver.implicitly_wait(6)

    # Step - 3 : Click Login button
    element_locators = ['//android.view.ViewGroup[@content-desc="Login"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 4 : Wait 10 s
    time.sleep(int(10))
    driver.implicitly_wait(6)

    # Step - 5 : Click 'Remote Config' cart under MY APPS text
    element_locators = ['//com.horcrux.svg.SvgView[@content-desc="icon remoteconfig"]/*[@class="com.horcrux.svg.GroupView"]/*[@class="com.horcrux.svg.GroupView"]/*[@class="com.horcrux.svg.PathView"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 6 : Wait 0.5 s
    time.sleep(int(0.5))
    driver.implicitly_wait(6)

    # Step - 7 : Check if 16200127 is visible → {{{{id_visible}}}}
    print('Step 7: Query - Check if 16200127 is visible → {{{{id_visible}}}}')
    driver.implicitly_wait(6)

    # Step - 8 : If 16200127 is not visible then scroll to find 16200127
    # Condition: If 16200127 is not visible then scroll to find 16200127
    if True:  # TODO: Implement condition
        pass
    else:
        pass
    driver.implicitly_wait(6)

    # Step - 9 : Click 16200127
    element_locators = ['(//android.widget.TextView[@content-desc="backyardName 16200127"])[1]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 10 : Wait 3 s
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Scroll 25% down in viewport
    print('Step 11: Scroll down - Scroll 25% down in viewport')

    driver.quit()
except Exception as e:
    driver.quit()
