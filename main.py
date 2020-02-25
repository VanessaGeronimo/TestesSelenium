from selenium import webdriver

navegador = webdriver.Firefox(executable_path='./geckodriver')

navegador.get( 'https://demodirectory.com/profile/login.php')
link = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/a')
link.click()

name =  navegador.find_element_by_id('first_name')
name.send_keys('Melissa')

lastname = navegador.find_element_by_id('last_name')
lastname.send_keys('Barbosa')

email = navegador.find_element_by_id('username')
email.send_keys('melissamariahbarbosa@inpa.gov.br')

password = navegador.find_element_by_id('password') 
password.send_keys("123789")

register = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[5]/button')
register.click()



