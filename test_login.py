from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with your BrowserStack credentials
USERNAME = "YOUR_USERNAME"
ACCESS_KEY = "YOUR_ACCESS_KEY"

browsers = [
    {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Firefox", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Safari", "browserVersion": "latest", "os": "OS X", "osVersion": "Monterey"},
    {"browserName": "Edge", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
]

for caps in browsers:
    caps["bstack:options"] = {
        "buildName": "Task-04 Build",
        "sessionName": f"Login Test on {caps['browserName']}"
    }

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=caps
    )

    driver.get("https://www.saucedemo.com/")  # Correct demo site
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.quit()

