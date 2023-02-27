from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()

first_name = driver.find_element_by_name("fname")

if first_name.is_enabled():
    first_name.send_keys("Tomek")
else:
    print("Element nie jest dostępny")