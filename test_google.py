import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)
driver.find_element_by_name("q").send_keys("Harman")
time.sleep(5)
driver.find_element_by_name("btnk").click()
time.sleep(10)
driver.close()
print("Test case has successfully completed")