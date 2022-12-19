
import pytest
from selene.support.shared import browser



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width, browser.config.window_height = 1920, 1024

    yield