from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")

# 98. Symulowanie kliknięcia prawym przyciskiem myszki

button = driver.find_element_by_id("clickOnMe")

webdriver.ActionChains(driver).context_click(button).perform()
