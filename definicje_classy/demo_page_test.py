from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/adela/Downloads/kurs_selenium/Test.html")
driver.maximize_window()
#
# #otwieranie nowego okna
# #driver.find_element_by_id("newPage").click()
#
# # Zamyka wszystkie okna które zostąły otwarte przez selenium
# # driver.quit()
#
# # zamknięcie przeglądarki na którym był fokus
# # driver.close()
#
# # znalezienie konkretnego elementu na stronie
#
# # metoda bezpośrednia
# # driver.find_element_by_id("fname")
#
# # metoda bardziej elastyczna
# # driver.find_element(By.ID,"fname")
#
#
#
# # technika lokalizowania elementów np. przycisków za pomocą nama
# # driver.find_element_by_id("clickOnMe")
# # driver.find_element_by_name("fname")
#
# # jak lokalizować elementy na stronie znajdujące się wewnątrz tagu"A"
# driver.find_element_by_link_text("Visit W3Schools.com!")
# # lokalizowanie lementów po niepełnym tekście bardziej elastyczna
# driver.find_element_by_partial_link_text("Visit W3Schools.com")
#
# #lokalizowanie leementów na stronie za pomocą nazwy klasy
# driver.find_element_by_class_name("topSecret")
#
# #lokalizowanie elementów
# driver.find_element_by_tag_name("a")
# driver.find_element_by_tag_name("p")
# driver.find_element_by_tag_name("label")
#
# #lokalizowanie elementu za pomocą selektora CSS
# driver.find_element_by_css_selector("a")
# driver.find_element_by_css_selector("img#smileImage")
# driver.find_element_by_css_selector("p.topSecret")
# print(driver.find_element_by_css_selector("th:first-child").text)
#
# #lokalizowanie za pomocą xpatha
# driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
# driver.find_element_by_xpath("//tbody//th")
# driver.find_element_by_xpath("//th")
# driver.find_element_by_xpath("//th[text()='Month']")
# driver.find_element_by_xpath("//button[@id='clickOnMe']")
# driver.find_element_by_xpath("//input[@id='fname']/following-sibling::table")
# driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table")
#
# #znajdowani listy elementów na stronie
# list_elements = len(driver.find_elements_by_xpath("//th"))
# print(list_elements)


# Kliknij na element

#driver.find_element_by_id("clickOnMe").click()
# click_me_button = driver.find_element_by_id("clickOnMe")
# click_me_button.click()

# nie można klikac na elementy niewidoczne na stronie.
# driver.find_element_by_tag_name("p").click()

# obsługiwanie alertów na stronie
# akceptowanie alertu
# driver.switch_to.alert.accept()
# pomijanie alertu
# driver.switch_to.alert.dismiss()

# # wprowadzanie wartości do pola tekstowego
# driver.find_element_by_id("fname").send_keys("Adela")
# print(driver.find_element_by_id("fname").get_attribute("value"))

# # symulowanie naciśnięcia przycisku
# #driver.find_element_by_name("password").send_keys(Keys.ENTER)
#
# #wybieranie opcji z rozwijanej listy - klasa Select
# auto_select = Select(driver.find_element_by_tag_name("select"))
# auto_select.select_by_visible_text("Volvo")
# auto_select.select_by_value("saab")
# auto_select.select_by_index(0)

# # Zaznaczanie chceckboxa na stronie
# driver.find_element_by_xpath("//input[@type='checkbox']").click()

#
# # Zaznaczanie radio buttona
# driver.find_element_by_xpath("//input[@value='male']").click()


# # Pobieranie tekstu z elementu
# # print(driver.find_element_by_xpath(("//input[@value='male']").text)) #nie zawierał tekstu
#
# print(driver.find_element_by_tag_name("h1").text)
# print(driver.find_element_by_id("clickOnMe").text)
# print(driver.find_element_by_tag_name("p").text) #nie zadziała dla niewidocznych elementów


#91. Pobieranie tekstu z ukrytego elementu
#print(driver.find_element_by_tag_name("p").get_attribute("textContent"))

# pobieranie tekstu z uzupełnionego pola tekstowego (wartość z inputa)
#driver.find_element_by_id("fname").send_keys("Adela")
#print(driver.find_element_by_id("fname").get_attribute("value"))


#92. Sprawdzenie czy obrazek wyświetla się na stronie
# print(driver.find_element_by_id("smileImage").size.get("height"))
# print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight")) #poleca do sprawdzania czy został poprawnie załadowany na stornie


# #93. Przełączanie do nowo otwartego okna przeglądarki
# driver.find_element_by_id("newPage").click()
# print(driver.title)
#
# current_window_name = driver.current_window_handle
# window_name = driver.window_handles
#
# for window in window_name:
#     if window != current_window_name:
#         driver.switch_to.window(window)
# print(driver.title)
#
# driver.switch_to.window(current_window_name)
# print(driver.title)







# zamknięcie okna
driver.quit()