from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://www.google.com')
pesquisa = driver.find_element_by_name('q')
pesquisa.send_keys('borboletas')
pesquisa.send_keys(Keys.RETURN)
resultados = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mBMHK"))
    )
print(resultados.text)