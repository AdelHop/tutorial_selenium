# W Pythonie możemy zdefiniować jednolinijkowe mini funkcje za pomocą tzw. wyrażenia lambda.
#
# Zamiast zapisywać funkcje w znanej nam postaci:
#
# def funkcja(x)
# 	return x*2
# Możemy skorzystać z zapisu:
#
# double_number = lambda x: x*2
#
# Wynik dla poniższych wywołań będzie taki sam i będzie wynosił 4.
#
# funkcja(2)
# double_number(2)
# W kolejnej lekcji skorzystamy z wyrażenia lambda, aby zapisać nasz własny warunek dla WebDriverWaita


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Waits2.html")
driver.find_element_by_id("clickOnMe").click()
wait.until(lambda wd: len(driver.find_elements_by_tag_name("p")) == 1)
print(driver.find_element_by_tag_name("p").text)