from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/DoubleClick.html")
driver.maximize_window()

#96. Symulowanie podwójnego kliknięcia myszki
button = driver.find_element_by_id("bottom")

webdriver.ActionChains(driver).double_click(button).perform()

