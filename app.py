# coding: iso-8859-1
from selenium.webdriver import Chrome
import time
from datetime import datetime

url = 'http://fullstackeletro-front.herokuapp.com/'

navegador = Chrome()
navegador.get(url)

'''
    - Intervalos de 30 em 30 min
    - O horário fica a seu critério, é interessante encerrar até 0h
    - Quantidade de ciclo = inicio + ciclo
    - Monitoramento
    - Horário Limite 
'''

hora_final = 20
inicio = 0
ciclo = 0

while datetime.now().hour < hora_final:
    if inicio == 0:
        print("Acordando o site. Aguarde 3 minutos")
        time.sleep(180)
        navegador.refresh()
        inicio = 1
        print('\t ------ Relatório ------')
    else:
        ciclo +=1
        print('\n Ciclo: {} \n Período: {}'.format(ciclo, datetime.now()))
        time.sleep(1790)
        navegador.refresh()
navegador.quit()
