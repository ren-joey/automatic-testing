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

def get_element(driver: WebDriver, xpath: str, retry: int = 3):
    try:
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        print(f"Error: {e}")
        print("Retry after 3 seconds")
        time.sleep(retry)
        return get_element(driver, xpath)

def click_element(driver: WebDriver, xpath: str, retry: int = 3):
    try:
        driver.find_element(By.XPATH, xpath).click()
    except Exception as e:
        print(f"Error: {e}")
        print("Retry after 3 seconds")
        time.sleep(retry)
        click_element(driver, xpath)

def traverse_communities(driver: WebDriver):
    ul = get_element(driver, "//div[@class='Community_CardList']/div[@class='dui-emptyHelper']/ul")
    print("ul.text")
    print(ul.text)

    li_elements = ul.find_elements(By.XPATH, "./li")

    for li in li_elements:
        print("li.text")
        print(li.text)

def start_automatic_testing(driver: WebDriver):
    # Open the website
    driver.get("https://devdms.deltaww.com/communityweb/en-us/Community/")
    click_element(driver, "//button[@class='ant-btn ant-btn-primary']")
    traverse_communities(driver)
    time.sleep(60)
    driver.quit()

if __name__ == "__main__":
    start_automatic_testing(get_chrome_driver())