from appium import webdriver

desired_caps = {}
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
