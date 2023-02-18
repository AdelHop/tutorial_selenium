from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()
driver.find_element_by_id("newPage").click()

# Zamyka wszystkie okna które zostąły otwarte przez selenium
# driver.quit()

# zamknięcie przeglądarki na którym był fokus
# driver.close()