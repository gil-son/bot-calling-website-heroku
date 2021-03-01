from selenium.webdriver import Chrome
import time
from datetime import datetime

url = 'https://www.google.com'

navegador = Chrome()
navegador.get(url)


botao_teclado = navegador.find_element_by_class_name('hOoLGe')
botao_teclado.click()

time.sleep(2)

botao_login = navegador.find_elements_by_tag_name('a')[0]
botao_login.click()

time.sleep(2)

navegador.quit()

