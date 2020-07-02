from selenium import webdriver
import pytest
from Base import Start_Browser
import time
from selenium.webdriver.common.action_chains import ActionChains
from Library import Config_Reader


def test_valid_username():
    driver = Start_Browser.startbrowser()
    driver.find_element_by_id(Config_Reader.Readelements("login", "username")).send_keys("Admin")
    driver.find_element_by_id(Config_Reader.Readelements("login", "password")).send_keys("admin123")
    driver.get_screenshot_as_file("Valid_Login.png")
    driver.find_element_by_id(Config_Reader.Readelements("login", "loginbutton")).click()
    assert driver.title == "OrangeHRM"
    driver.quit()


def test_invalid_username():
    driver = Start_Browser.startbrowser()
    driver.find_element_by_id(Config_Reader.Readelements("login", "username")).send_keys("Admin")
    driver.find_element_by_id(Config_Reader.Readelements("login", "password")).send_keys("admin123")
    driver.find_element_by_id(Config_Reader.Readelements("login", "loginbutton")).click()
    driver.get_screenshot_as_file("Invalid_Login.png")
    actual_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/span')
    expected_text = "Invalid credentials"
    assert actual_text == expected_text
    driver.quit()


def test_invalid_password():
    driver = Start_Browser.startbrowser()
    driver.find_element_by_id(Config_Reader.Readelements("login", "username")).send_keys("Admin")
    driver.find_element_by_id(Config_Reader.Readelements("login", "password")).send_keys("admin123")
    driver.find_element_by_id(Config_Reader.Readelements("login", "loginbutton")).click()
    driver.get_screenshot_as_file("Invalid_password.png")
    actual_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/span')
    expected_text = "Invalid credentials"
    assert actual_text == expected_text
    driver.quit()

def test_forgotpassword():
    driver = Start_Browser.startbrowser()
    driver.find_element_by_id(Config_Reader.Readelements("login", "forgotbutton")).click()
    print(driver.title)


def test_logout():
    driver = Start_Browser.startbrowser()
    driver.find_element_by_id(Config_Reader.Readelements("login", "username")).send_keys("Admin")
    driver.find_element_by_id(Config_Reader.Readelements("login", "password")).send_keys("admin123")
    driver.find_element_by_id(Config_Reader.Readelements("login", "loginbutton")).click()
    assert driver.title == "OrangeHRM"
    mousehovering = ActionChains(driver)
    welcomebutton = driver.find_element_by_id(Config_Reader.Readelements("welcome", "welcome"))
    logoutbutton = driver.find_element_by_xpath(Config_Reader.Readelements("welcome", "logoutbutton"))
    mousehovering.move_to_element(welcomebutton).click().move_to_element(logoutbutton).click().perform()


def test_edituser():
    driver = Start_Browser.startbrowser()
    driver.find_element_by_id(Config_Reader.Readelements("login", "username")).send_keys("Admin")
    driver.find_element_by_id(Config_Reader.Readelements("login", "password")).send_keys("admin123")
    driver.find_element_by_id(Config_Reader.Readelements("login", "loginbutton")).click()

    admin = driver.find_element_by_id(Config_Reader.Readelements("edituser", "mainmenu"))
    usermanagement = driver.find_element_by_id(Config_Reader.Readelements("edituser", "usermanagement"))
    user = driver.find_element_by_id(Config_Reader.Readelements("edituser", "viewuser"))
    mouserhovering = ActionChains(driver)
    mouserhovering.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform()
    driver.find_element_by_id(Config_Reader.Readelements("edituser", "searchuser")).send_keys("Admin")
    driver.find_element_by_id(Config_Reader.Readelements("edituser", "searchbutton")).click()
    driver.quit()








