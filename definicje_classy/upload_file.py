from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/FileUpload.html")


#102. Upload pliku

upload_input = driver.find_element_by_id("myFile")
path = os.path.abspath("upload.txt")
driver.save_screenshot(("screenshots/befour_screenshot.png"))

upload_input.send_keys(path)

#103. Tworzenie screenshota - zrzutu okna przeglądarki

driver.save_screenshot(("screenshots/after_screenshot.png"))


