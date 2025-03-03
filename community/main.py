import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver() -> WebDriver:
    # Activate browser
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def click_element(driver: WebDriver, xpath: str, retry: int = 3):
    try:
        driver.find_element(By.XPATH, xpath).click()
    except Exception as e:
        print(f"Error: {e}")
        print("Retry after 3 seconds")
        time.sleep(retry)
        click_element(driver, xpath)

def start_automatic_testing(driver: WebDriver):
    # Open the website
    driver.get("https://devdms.deltaww.com/communityweb/en-us/Community/")
    click_element(driver, "//button[@class='ant-btn ant-btn-primary']")
    time.sleep(60)
    driver.quit()

if __name__ == "__main__":
    start_automatic_testing(get_chrome_driver())