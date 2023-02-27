from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()

# 106. Sprawdzenie czy element istnieje na stronie

elements = driver.find_elements_by_tag_name("papa")

if len(elements) > 0:
    print("Element istnieje na stronie")

else:
    print("Brak elementu na stronie")

# Zapomocą bloków
try:
    driver.find_element_by_tag_name("papa")
    print("Element istnieje na stronie")
except NoSuchElementException:
    print("Element nie istnieje na stornie")
