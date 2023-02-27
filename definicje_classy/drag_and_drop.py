from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index/")

driver.find_element_by_id("onetrust-accept-btn-handler").click()

#100. Symulowanie drag and drop

draggable = driver.find_element_by_id("draggable")
droptarget = driver.find_element_by_id("droptarget")

webdriver.ActionChains(driver).drag_and_drop(draggable, droptarget).perform()