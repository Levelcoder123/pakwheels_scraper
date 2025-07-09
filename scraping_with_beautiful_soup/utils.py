from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options


# from selenium.webdriver.chrome.options import Options


# load website using webdriver
def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")  # Recommended for Linux

    driver = webdriver.Firefox(
        options=options,
    )
    # driver.maximize_window()

    # uncomment the following lines to use Chrome instead of Firefox
    # driver = webdriver.Chrome(
    #         options=options,
    #     )

    return driver


def get_soup_by_selenium_driver(url):
    driver = get_driver()
    driver.get(url)

    # get html from driver and make it soup
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, features="html.parser")
    driver.quit()

    return soup
