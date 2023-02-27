from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Waits2.html")
driver.maximize_window()

driver.find_element_by_id("clickOnMe").click()
time.sleep(10)
print(driver.find_element_by_tag_name("p").text)




