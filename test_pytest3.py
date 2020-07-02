#Execute any particular test case
#To execute particular test case, go to terminal and type below command
#   pytest -k method name
#For this program, I am running first test only
#   pytest -k test1_valid_login

from selenium import webdriver
import pytest
driver = webdriver.Chrome(executable_path="C:/Users/Sandeep Burad/PycharmProjects/Hello/drivers/chromedriver.exe")
a=100


def test1_valid_login():
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    driver.find_element_by_id("welcome").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()


def test2_invalid_login():
    driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys("admin1234")
    driver.find_element_by_id("btnLogin").click()
    assert driver.find_elements_by_link_text("Invalid credentials") == 'Invalid credentials'
    print("Invalid login text matching")
    driver.close()
    driver.quit()


def test3_invalid_login():
    driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtUsername").send_keys("Admin1")
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    assert driver.find_elements_by_link_text("Invalid credentials") == 'Invalid credentials'
    print("Invalid login text matching")
    driver.close()
    driver.quit()

if __name__ == '__main__':
    pytest.main()