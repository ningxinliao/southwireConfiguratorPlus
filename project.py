from selenium import webdriver
from uiautomation_pkg_common_webdriver import *


def main():
    driver = webdriver.Edge()
    global app
    global UIType
    app = Device(driver)
    UIType = Type(driver)

    app.driver.get('https://southwire-configurator-test.firebaseapp.com/')

main()
