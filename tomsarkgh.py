import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


def parse(category):
    chromedriver_autoinstaller.install()

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for Render
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service()  # No need to specify path, chromedriver-autoinstaller handles it


    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url='https://www.tomsarkgh.am/')
        time.sleep(3)

        if category == "concerts":
            driver.find_element(By.CSS_SELECTOR, '#drop2').click()
            time.sleep(1)
            xpaths = [
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[1]/div[1]',
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[2]/div[1]',
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[3]/div[1]'
            ]

        elif category == "theatre":
            driver.find_element(By.CSS_SELECTOR, '#drop5').click()
            time.sleep(1)
            xpaths = [
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[1]/div[1]',
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[2]/div[1]',
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[3]/div[1]'
            ]

        elif category == "opera_ballet":
            driver.find_element(By.CSS_SELECTOR, '#drop43').click()
            time.sleep(1)
            xpaths = [
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[1]/div[1]',
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[2]/div[1]',
                '//*[@id="main_wrapper"]/div/div/div[1]/div[1]/div[3]/div[1]'
            ]

        events = []
        for xpath in xpaths:
            try:
                event = driver.find_element(By.XPATH, xpath).text
                if event.strip():
                    events.append(event)
            except:
                events.append("No event found")

        return "\n\n".join(events)

    except Exception as ex:
        return f"Error: {ex.__class__.__name__}"

    finally:
        driver.close()
        driver.quit()
