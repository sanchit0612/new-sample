
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
import time, traceback

options = XCUITestOptions()
options.set_capability("platformName", "ios")

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

    # Step - 1 : Click on the 'Allow While Using App' button
    element_locators = ['//XCUIElementTypeButton[@label="Allow While Using App"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 2 : Click on the 'Allow' button
    element_locators = ['//XCUIElementTypeButton[@label="Allow"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 3 : Click on the 'Allow' button
    element_locators = ['//XCUIElementTypeButton[@label="Allow"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 4 : Scroll right by 42%
    print('Step 4: Scroll right - Scroll right by 42%')
    driver.implicitly_wait(6)

    # Step - 5 : Click on the In-Game tab in the bottom navigation bar
    print('Step 5: Click on the In-Game tab in the bottom navigation bar')
    driver.implicitly_wait(6)

    # Step - 6 : Click on the LOG IN button
    element_locators = ['//XCUIElementTypeButton[@label="LOG IN"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 7 : Click on the mobile number/email/username input field
    print('Step 7: Click on the mobile number/email/username input field')
    driver.implicitly_wait(6)

    # Step - 8 : Type 'kishan.rudrabhatla+bcnj@ballys.com'
    element_locators = ['//XCUIElementTypeTextField[@label="Mobile number, email or username"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        pass
    element.clear()
    element.send_keys('kishan.rudrabhatla+bcnj@ballys.com')
    driver.implicitly_wait(6)

    # Step - 9 : Click on the Password input field
    print('Step 9: Click on the Password input field')
    driver.implicitly_wait(6)

    # Step - 10 : Click on the Password input field
    element_locators = ['//XCUIElementTypeSecureTextField[@label="Password"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 11 : Type 'Password1'
    element_locators = ['//XCUIElementTypeSecureTextField[@label="Password"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        pass
    element.clear()
    element.send_keys('Password1')
    driver.implicitly_wait(6)

    # Step - 12 : Click on the 'LOG IN' button
    element_locators = ['//XCUIElementTypeButton[@label="LOG IN"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 13 : Click on the Sports tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="Sports"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 14 : Click on the Live tab icon
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeCell"][2]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 15 : Click on the Baseball tab in the top sports category bar
    element_locators = ['//XCUIElementTypeStaticText[@label="Baseball"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 16 : Click on the back button in top left corner
    element_locators = ['//XCUIElementTypeOther[./XCUIElementTypeStaticText[@label="Basketball"]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 17 : Click on the Back button in the top navigation bar
    element_locators = ['//XCUIElementTypeImage[@label="Back"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 18 : Scroll right by 62%
    print('Step 18: Scroll right - Scroll right by 62%')
    driver.implicitly_wait(6)

    # Step - 19 : Scroll left by 41%
    print('Step 19: Scroll left - Scroll left by 41%')
    driver.implicitly_wait(6)

    # Step - 20 : Scroll down by 12%
    print('Step 20: Scroll down - Scroll down by 12%')
    driver.implicitly_wait(6)

    # Step - 21 : Click on the MLB tab in the sports categories row
    element_locators = ['//XCUIElementTypeStaticText[@label="Featured"]/parent::*/*[@type="XCUIElementTypeImage"][2]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 22 : Click on the 'PGA Tour' tab label.
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeCell"][4]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 23 : Click on the 'EPL' tab in the sports categories row
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeCell"][4]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 24 : Click on the EPL tab in the sports tab bar
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeCell"][4]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 25 : Scroll right by 56%
    print('Step 25: Scroll right - Scroll right by 56%')
    driver.implicitly_wait(6)

    # Step - 26 : Click on the NBA category icon
    element_locators = ['//XCUIElementTypeStaticText[@label="Bally Boosts"]/parent::*/*[@type="XCUIElementTypeImage"][13]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 27 : Click on the Settings button
    print('Step 27: Click on the Settings button')
    driver.implicitly_wait(6)

    # Step - 28 : Click on the Sports tab in bottom navigation bar
    element_locators = ['//XCUIElementTypeImage[@label="Back"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 29 : Scroll left by 47%
    print('Step 29: Scroll left - Scroll left by 47%')
    driver.implicitly_wait(6)

    # Step - 30 : Click on the next page dot indicator below the matchup card
    print('Step 30: Click on the next page dot indicator below the matchup card')
    driver.implicitly_wait(6)

    # Step - 31 : Click on the 'UFC' sports tab icon
    print('Step 31: Click on the 'UFC' sports tab icon')
    driver.implicitly_wait(6)

    # Step - 32 : Click on the Tennis category icon
    print('Step 32: Click on the Tennis category icon')
    driver.implicitly_wait(6)

    # Step - 33 : Click on the down chevron next to CLEAR ALL in the QUICKBET header
    element_locators = ['//XCUIElementTypeButton[@label="chevronDown"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 34 : Click on the 'GET' promotional banner
    print('Step 34: Click on the 'GET' promotional banner')
    driver.implicitly_wait(6)

    # Step - 35 : Click on the Back button in the top navigation bar.
    element_locators = ['//XCUIElementTypeImage[@label="Back"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 36 : Scroll down by 28%
    print('Step 36: Scroll down - Scroll down by 28%')
    driver.implicitly_wait(6)

    # Step - 37 : Scroll down by 31%
    print('Step 37: Scroll down - Scroll down by 31%')
    driver.implicitly_wait(6)

    # Step - 38 : Scroll up by 24%
    print('Step 38: Scroll up - Scroll up by 24%')
    driver.implicitly_wait(6)

    # Step - 39 : Scroll up by 29%
    print('Step 39: Scroll up - Scroll up by 29%')
    driver.implicitly_wait(6)

    # Step - 40 : Scroll up by 48%
    print('Step 40: Scroll up - Scroll up by 48%')
    driver.implicitly_wait(6)

    # Step - 41 : Click on the 'View All (4)' link in Sports Bonuses
    print('Step 41: Click on the 'View All (4)' link in Sports Bonuses')
    driver.implicitly_wait(6)

    # Step - 42 : Click on the back arrow icon in the page header
    element_locators = ['//XCUIElementTypeImage[@label="Back"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 43 : Click on the My Bets tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="My Bets"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 44 : Click on the 'Cash Out' tab.
    element_locators = ['//XCUIElementTypeStaticText[@label="Cash Out"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 45 : Click on the Promotions tab in the bottom navigation bar
    print('Step 45: Click on the Promotions tab in the bottom navigation bar')
    driver.implicitly_wait(6)

    # Step - 46 : Click on the Sports tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="Sports"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 47 : Click on the Explore button
    print('Step 47: Click on the Explore button')
    driver.implicitly_wait(6)

    # Step - 48 : Click on the Back button in the top navigation bar
    element_locators = ['//XCUIElementTypeImage[@label="Back"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 49 : Click on the Live tab in the bottom navigation bar
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeCell"][2]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 50 : Click on the Back button in the top navigation bar
    print('Step 50: Click on the Back button in the top navigation bar')
    driver.implicitly_wait(6)

    # Step - 51 : Click on the game start time label 'Today 18:05'
    print('Step 51: Click on the game start time label 'Today 18:05'')
    driver.implicitly_wait(6)

    # Step - 52 : Click on the SGP tab label.
    element_locators = ['//XCUIElementTypeCollectionView/*[@type="XCUIElementTypeCell"][4]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 53 : Scroll down by 23%
    print('Step 53: Scroll down - Scroll down by 23%')
    driver.implicitly_wait(6)

    # Step - 54 : Scroll up by 15%
    print('Step 54: Scroll up - Scroll up by 15%')
    driver.implicitly_wait(6)

    # Step - 55 : Click on the 'Swift SGP' tab label
    print('Step 55: Click on the 'Swift SGP' tab label')
    driver.implicitly_wait(6)

    # Step - 56 : Click on the 'Batter Props' tab label
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeScrollView]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 57 : Click on the 'Team Props' tab.
    print('Step 57: Click on the 'Team Props' tab.')
    driver.implicitly_wait(6)

    # Step - 58 : Click on the 'Pitcher Props' tab
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeScrollView]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 59 : Click on the back arrow in the top navigation bar
    print('Step 59: Click on the back arrow in the top navigation bar')
    driver.implicitly_wait(6)

    # Step - 60 : Scroll down by 22%
    print('Step 60: Scroll down - Scroll down by 22%')
    driver.implicitly_wait(6)

    # Step - 61 : Scroll up by 49%
    print('Step 61: Scroll up - Scroll up by 49%')
    driver.implicitly_wait(6)

    # Step - 62 : Scroll up by 32%
    print('Step 62: Scroll up - Scroll up by 32%')
    driver.implicitly_wait(6)

    # Step - 63 : Click on the 'Today 18:05' label above the game odds
    print('Step 63: Click on the 'Today 18:05' label above the game odds')
    driver.implicitly_wait(6)

    # Step - 64 : Click on the 'SGP' tab label
    print('Step 64: Click on the 'SGP' tab label')
    driver.implicitly_wait(6)

    # Step - 65 : Scroll down by 12%
    print('Step 65: Scroll down - Scroll down by 12%')
    driver.implicitly_wait(6)

    # Step - 66 : Click on the 'TOR Blue Jays' row in the Moneyline table
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeButton[@label="+180"]]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 67 : Click on the 'TOR Blue Jays' row in the Moneyline section
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeButton[@label="+180"]]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 68 : Click on the 'NY Yankees' row in the Moneyline section
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeButton[@label="+180"]]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 69 : Click on the '+180' odds button in the Moneyline row for TOR Blue Jays
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeButton[@label="+180"]]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 70 : Click on the Moneyline section header with SGP label
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeOther"][2]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 71 : Scroll down by 17%
    print('Step 71: Scroll down - Scroll down by 17%')
    driver.implicitly_wait(6)

    # Step - 72 : Click on the Run Line section
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeOther"][3]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 73 : Scroll up by 31%
    print('Step 73: Scroll up - Scroll up by 31%')
    driver.implicitly_wait(6)

    # Step - 74 : Click on the 'Swift SGP' tab label
    print('Step 74: Click on the 'Swift SGP' tab label')
    driver.implicitly_wait(6)

    # Step - 75 : Scroll down by 16%
    print('Step 75: Scroll down - Scroll down by 16%')
    driver.implicitly_wait(6)

    # Step - 76 : Click on the back arrow next to Sports in the top navigation bar
    print('Step 76: Click on the back arrow next to Sports in the top navigation bar')
    driver.implicitly_wait(6)

    # Step - 77 : Scroll right by 36%
    print('Step 77: Scroll right - Scroll right by 36%')
    driver.implicitly_wait(6)

    # Step - 78 : Scroll right by 67%
    print('Step 78: Scroll right - Scroll right by 67%')
    driver.implicitly_wait(6)

    # Step - 79 : Click on the ARS team label
    print('Step 79: Click on the ARS team label')
    driver.implicitly_wait(6)

    # Step - 80 : Click on the back arrow in the top navigation bar
    print('Step 80: Click on the back arrow in the top navigation bar')
    driver.implicitly_wait(6)

    # Step - 81 : Click on the Search tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="Search"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 82 : Click on the 'My Bets' tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="My Bets"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 83 : Click on the Open tab label
    print('Step 83: Click on the Open tab label')
    driver.implicitly_wait(6)

    # Step - 84 : Click on the 'Live' tab label.
    element_locators = ['//XCUIElementTypeStaticText[@label="Live"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 85 : Click on the 'Settled' tab
    element_locators = ['//XCUIElementTypeStaticText[@label="Settled"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 86 : Click on the Search tab icon in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="Search"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 87 : Click on the Promotions tab in the bottom navigation bar
    print('Step 87: Click on the Promotions tab in the bottom navigation bar')
    driver.implicitly_wait(6)

    # Step - 88 : Click on the Rewards tab
    element_locators = ['//XCUIElementTypeButton[@label="Rewards"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 89 : Click on the Casino tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="Casino"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 90 : Click on the Sports tab in the bottom navigation bar
    element_locators = ['//XCUIElementTypeButton[@label="Sports"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 91 : Scroll down by 22%
    print('Step 91: Scroll down - Scroll down by 22%')
    driver.implicitly_wait(6)

    # Step - 92 : Click on the Rafael Devers player prop row
    element_locators = ['//XCUIElementTypeCell[./*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeOther" and ./XCUIElementTypeStaticText[@label="Today 18:10"]]]]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 93 : Click on the '+148' moneyline odds cell for SF Giants
    print('Step 93: Click on the '+148' moneyline odds cell for SF Giants')
    driver.implicitly_wait(6)

    # Step - 94 : Click on the 'SGP' tab label
    print('Step 94: Click on the 'SGP' tab label')
    driver.implicitly_wait(6)

    # Step - 95 : Scroll down by 16%
    print('Step 95: Scroll down - Scroll down by 16%')
    driver.implicitly_wait(6)

    # Step - 96 : Scroll down by 51%
    print('Step 96: Scroll down - Scroll down by 51%')
    driver.implicitly_wait(6)

    # Step - 97 : Click on the 'SHOW ALL' button
    print('Step 97: Click on the 'SHOW ALL' button')
    driver.implicitly_wait(6)

    # Step - 98 : Click on the -127 odds cell in the 7.0 row
    element_locators = ['//XCUIElementTypeButton[@label="-127"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 99 : Click on the -127 odds cell in the 7.0 Total Runs row
    element_locators = ['//XCUIElementTypeButton[@label="-127"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 100 : Scroll up by 69%
    print('Step 100: Scroll up - Scroll up by 69%')
    driver.implicitly_wait(6)

    # Step - 101 : Click on the back arrow in the top navigation bar
    print('Step 101: Click on the back arrow in the top navigation bar')
    driver.implicitly_wait(6)

    # Step - 102 : Scroll right by 28%
    print('Step 102: Scroll right - Scroll right by 28%')
    driver.implicitly_wait(6)

    # Step - 103 : Click on the Soccer category icon.
    element_locators = ['/XCUIElementTypeApplication/*[@type="XCUIElementTypeWindow"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"][1]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeOther"]/*[@type="XCUIElementTypeCollectionView"]/*[@type="XCUIElementTypeCell"][2]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 104 : Scroll down by 9%
    print('Step 104: Scroll down - Scroll down by 9%')
    driver.implicitly_wait(6)

    # Step - 105 : Click on the Premier League match row for Arsenal vs Coventry City
    print('Step 105: Click on the Premier League match row for Arsenal vs Coventry City')
    driver.implicitly_wait(6)

    # Step - 106 : Scroll down by 16%
    print('Step 106: Scroll down - Scroll down by 16%')
    driver.implicitly_wait(6)

    # Step - 107 : Click on the back arrow in the top navigation bar
    element_locators = ['//XCUIElementTypeImage[@label="Back"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)

    driver.quit()
except Exception as e:
    driver.quit()
