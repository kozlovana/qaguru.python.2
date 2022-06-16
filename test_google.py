import pytest

from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope='session', autouse=True)
def config_browser():
    browser.window_width = 500
    browser.window_height = 500


def test_first():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene was the ancient Greek Titan goddess of the moon'))


def test_second():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Non-existent result'))
