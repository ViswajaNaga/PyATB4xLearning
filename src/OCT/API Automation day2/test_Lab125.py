import pytest
import allure
import requests

def test_selenium(launch_browser,close_browser):
    launch_browser
    print("Do TC")
    close_browser

