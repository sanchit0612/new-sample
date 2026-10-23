
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

    # Step - 1 : Open https://example.com
    driver.get("https://example.com")
    driver.implicitly_wait(6)

    # Step - 2 : Execute JavaScript snippet
    JS_Response=driver.execute_script('''return (function(){try{return (function(){
    (() => {
      if (window.__extProtoGuard) return;
      window.__extProtoGuard = true;
      window.__blockedLaunches = [];
      const isExternal = (u) => {
        try { return !/^(https?|about|blob|data|javascript):$/.test(new URL(u, location.href).protocol); }
        catch (e) { return false; }
      };
      const note = (how, u) => { window.__blockedLaunches.push({ how, url: String(u) }); };
      if (window.navigation) {
        navigation.addEventListener('navigate', (e) => {
          if (isExternal(e.destination.url) && e.cancelable) { e.preventDefault(); note('navigate', e.destination.url); }
        });
      }
      document.addEventListener('click', (e) => {
        const a = e.target.closest && e.target.closest('a[href]');
        if (a && isExternal(a.href)) { e.preventDefault(); note('link', a.href); }
      }, true);
      const open = window.open;
      window.open = function (u, ...rest) {
        if (u && isExternal(u)) { note('window.open', u); return null; }
        return open.call(this, u, ...rest);
      };
    })();
    })()}catch(e){return {error: e.stack}}})()''')
    print("Your response is => ",JS_Response)
    driver.implicitly_wait(6)

    # Step - 3 : Execute JavaScript snippet
    JS_Response=driver.execute_script('''return (function(){try{return (function(){
    setTimeout(() => { location.href = 'myapp://open?from=te-33414'; }, 100);
    })()}catch(e){return {error: e.stack}}})()''')
    print("Your response is => ",JS_Response)
    driver.implicitly_wait(6)

    # Step - 4 : Execute JavaScript snippet
    JS_Response=driver.execute_script('''return (function(){try{return (function(){
    return JSON.stringify(window.__blockedLaunches || 'guard not present');
    })()}catch(e){return {error: e.stack}}})()''')
    print("Your response is => ",JS_Response)
    driver.implicitly_wait(6)

    # Step - 5 : Click 'Learn more' link
    element_locators = ["//a[text()='Learn more']", 'body > a:nth-child(9)', 'body > a:nth-child(9)', "//a[contains(text(),'Learn more')]", '//body/a[1]', '//body/a[1]']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
