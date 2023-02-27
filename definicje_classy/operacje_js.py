from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()

#95. Klikanie na element i ustawianie wartości pola tekstowego przy pomocy JavaScript
driver.execute_script("arguments[0].click();",driver.find_element_by_id("newPage"))

#ustawianie wartości atrybutu
wartosc = "Adela"
driver.execute_script("arguments[0].setAttribute ('value', '" + wartosc +"')",driver.find_element_by_id("fname"))



driver.switch_to.alert.dismiss()

