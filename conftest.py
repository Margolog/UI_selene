import os
import pytest
from dotenv import load_dotenv
from utils import attach
from selene.support import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from modal.application_manager import ApplicationManager



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 5
    browser.config.window_width, browser.config.window_height = 1920, 1024

    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function')
def app() -> ApplicationManager:
    _app = ApplicationManager()
    return _app