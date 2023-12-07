from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    # Set your access credentials
    "browserstack.user" : “YOUR_BROWSERSTACK_USERNAME”,
    "browserstack.key" : “YOUR_BROWSERSTACK_ACCESS_KEY”,
    # Use the unique URL to specify the app to be downloaded
    "app" : "bs://ca0b82b855ca2c5157b2b3d36fad5b392b723fbd",
    # Provide device specifications
    "device" : "Xiaomi Redmi Note 8",
    "os_version" : "9.0",
    # grant permissions automatically and accept any pop up alerts
    "autoGrantPermissions":"true",
    "autoAcceptAlerts":"true",
    #Specify the project, build, and name
    "project" : "Test Python project", 
    "build" : "BrowserStack-build-1",
    "name" : "notes_app_test"
}
desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Identify calculator buttons using accessibility id
number_7_button = driver.find_element_by_accessibility_id('num7Button')
number_7_button.click()

add_button = driver.find_element_by_accessibility_id('plusButton')
add_button.click()

number_3_button = driver.find_element_by_accessibility_id('num3Button')
number_3_button.click()

equals_button = driver.find_element_by_accessibility_id('equalButton')
equals_button.click()

driver.quit()
