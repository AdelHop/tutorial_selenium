from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.google.com")

# Określenie wielkosci okna w pixelach
# driver.set_window_size(1800,1200)

# Otwarcie przeglądarki w maksymalnych rozmiarach ekranu
# driver.maximize_window()

#zamknięcie przeglądarki
driver.close()