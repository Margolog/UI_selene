import pytest
from selene.support.shared import browser
from modal.application_manager import ApplicationManager



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 5
    browser.config.window_width, browser.config.window_height = 1920, 1024
    yield


@pytest.fixture(scope='function')
def app() -> ApplicationManager:
    _app = ApplicationManager()
    return _app