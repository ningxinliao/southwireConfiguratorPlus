from selenium import webdriver
from common import *


def main():
    driver = webdriver.Chrome()
    global app
    global UIType
    app = Device(driver)
    UIType = Type(driver)

main()
