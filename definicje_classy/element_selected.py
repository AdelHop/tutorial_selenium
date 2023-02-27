from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()

# 107. Sprawdzenie czy element jest wybrany/zaznaczony

checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")


if checkbox.is_selected():
    print("Wartość zaznaczona!, Odznaczam")
    checkbox.click()
else:
    print("Zaznaczam")
    checkbox.click()