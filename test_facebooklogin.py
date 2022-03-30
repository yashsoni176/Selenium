import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

username = input("Enter username : ")
password = input("Enter password : ")

driver = webdriver.Chrome(ChromeDriverManager().install())

print("Test case Started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.find_element_by_name("email").send_keys(username)
time.sleep(5)
driver.find_element_by_name("pass").click(password)
time.sleep(5)
driver.find_element_by_name("login").click()
driver.close()
print("Test Case completed")