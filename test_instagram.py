import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
username = input("Enter username : ")
password = input("Enter password : ")
driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element_by_name("username").send_keys(username)
time.sleep(5)
driver.find_element_by_name("password").send_keys(password)
time.sleep(5)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(4)
driver.close()
print("Test case has successfully completed")