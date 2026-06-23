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

    driver.get("https://www.demoblaze.com/")  # Example demo site
    driver.find_element(By.ID, "login2").click()
    driver.find_element(By.ID, "loginusername").send_keys("testuser")
    driver.find_element(By.ID, "loginpassword").send_keys("password")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    driver.quit()
