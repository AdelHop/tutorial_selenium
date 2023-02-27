from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/iFrameTest.html")
driver.maximize_window()

#94. Obsługa iframe - strona wewnątrz strony

print(driver.find_element_by_tag_name("h1").text)

"""Przejscie do strony testowej"""
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
print(driver.find_element_by_tag_name("h1").text)

"""Powrót do iframe"""
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h1").text)


driver.quit()