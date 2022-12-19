import pytest
from selene.support.shared import browser

from modal.application_manager import ApplicationManager
from modal.pages.payment_page import SearchThings


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width, browser.config.window_height = 1920, 1024

    yield


@pytest.fixture(scope='function')
def app() -> ApplicationManager:
    _app = ApplicationManager()
    return _app
