from community import main as community

if __name__ == "__main__":
    driver = community.get_chrome_driver()
    community.start_automatic_testing(driver)