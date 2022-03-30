import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.amazon.com/")
time.sleep(1)
driver.find_element_by_id("twotabsearchtextbox").send_keys("Samsung S22")
time.sleep(5)
driver.find_element_by_id("nav-search-submit-text").click()
time.sleep(10)
driver.close()
print("Test case has successfully completed")

