from appium import webdriver
# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
import unittest

# Set up desired capabilities
capabilities = dict(
    platformName='Windows',
    automationName='Windows',
    deviceName='WindowsPC',
    app='Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
)

# When pointing a test at Appium you need to include 
appium_server_url = 'http://localhost:4723/wd/hub'
# appium_server_url = 'http://localhost:4723'

class TestWindowsCalculator(unittest.TestCase):
    def setUp(self) -> None:
        capabilities = dict(
            platformName='Windows',
            automationName='Windows',
            deviceName='WindowsPC',
            app='Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
        )
        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        self.
        driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)
        # self.
        driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_addition(self) -> None:
        # Find the buttons by their names and click them in sequence to perform 1 + 2
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("Two").click()
        self.driver.find_element_by_name("Equals").click()

        # Assert that the result is 3
        result = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        assert result == "Display is 3"

if __name__ == '__main__':
    unittest.main()