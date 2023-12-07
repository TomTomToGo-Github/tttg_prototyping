# https://www.youtube.com/watch?v=x-hBpgM5je8&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=3


import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Windows',
    automationName='battery_automator',
    # deviceName='Dell',
    # app = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App',
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    language='en',
    # locale='US'
)
# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Android',
#     appPackage='com.android.settings',
#     appActivity='.Settings',
#     language='en',
#     locale='US'
# )

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()


if __name__ == '__main__':
    unittest.main()