from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/")

driver.find_element_by_id("accept-choices").click()

# #99. Najechanie na element - hover
tutorials_element = driver.find_element_by_id("navbtn_tutorials")
#
# webdriver.ActionChains(driver).move_to_element(tutorials_element)

#101. Łańcuchy akcji - najechanie na element i kliknięcie
webdriver.ActionChains(driver).move_to_element(tutorials_element).click(tutorials_element).perform()



