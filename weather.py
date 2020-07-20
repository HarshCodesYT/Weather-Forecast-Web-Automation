from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

path = "C:\Program Files (x86)\chromedriver"
city = input("Enter City Name: ")
driver = webdriver.Chrome(path)
driver.get("https://www.bbc.com/weather")

try:
    search = WebDriverWait(driver , 30).until(
        ec.presence_of_all_elements_located((By.ID , "ls-c-search__input-label"))
    )
    search[0].send_keys(city)

    suggestion = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.CLASS_NAME , "ls-c-locations-list-item"))
    )
    suggestion.click()

except:
    driver.quit()