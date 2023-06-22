import pytest
from selene import browser
from selene.support import webdriver
from selenium import webdriver
from selenium.webdriver.chrome import webdriver


@pytest.fixture
def brwsr():
    # options = webdriver.ChromeOptions()
    # options.headless = True
    # browser.config.driver = webdriver.Chrome(chrome_options=options)
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')