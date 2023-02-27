#105. Sprawdzenie czy element jest wyświetlony

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()

paragraph = driver.find_element_by_tag_name("p")

if paragraph.is_displayed():
    print("Is displayed")
    print(paragraph.text)
else:
    print("Is not displayed")
    print(paragraph.get_attribute("textContent"))

