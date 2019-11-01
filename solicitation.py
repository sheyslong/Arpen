# Generated by Selenium IDE
# -*- coding: UTF-8 -*- 

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from random import randint
from config import getAll

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
Linux = '/snap/bin/chromium.chromedriver'
Windows = 'C:\\Users\\Sheilla.CONTAGIL2\\Documents\\07. Chrome Driver\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(Windows)

type_file = ''

def logar():
	driver.get("https://www4.receita.pb.gov.br/atf/")
	driver.set_window_size(1296, 704)
	driver.switch_to.frame(1)
	driver.find_element(By.ID, "login").send_keys('fra13582')
	driver.find_element(By.NAME, "edtDsSenha").click()
	driver.find_element(By.NAME, "edtDsSenha").send_keys('fiscal3336*')
	time.sleep(2)

	driver.find_element(By.NAME, "btnAvancar").click()
	time.sleep(5)

def addKey(nfces):
	for nfce in nfces:
		print(nfce)
		driver.find_element(By.NAME, "edtNrChaveAcesso").send_keys(nfce)
		driver.find_element(By.NAME, "btnAdicionar").click()


def main(nfces):
	logar()
	nfce = 'https://www4.receita.pb.gov.br/atf/fis/FISf_ConsultaGenericaEmitenteNFCe.do?limparSessao=true'
	driver.get(nfce)

	addKey(nfces)

	select = Select(driver.find_element_by_name('cmbTpExibicao'))
	select.select_by_visible_text(type_file)

	driver.find_element(By.NAME, 'btnConsultar').click() 

print('Selecione o tipo de arquivo para donwload: \n1. HTML\n2. XML\n3. TXT(produtos)\n4.TXT')
#type_input = int(input('Digite a numeração: '))
type_input = 3
while type_input < 1 or type_input > 4:
	type_input = int(input('Digite a numeração: '))

if type_input == 1:
	type_file = "HTML"

if type_input == 2: 
	type_file = "XML"

if type_input == 3: 
	type_file = "TXT (produtos)"

if type_input == 4: 
	type_file = "TXT"

while True:
	nfces = getAll()
	now = datetime.now()
	print(now)
	print('Quantidade de arquivos: ',len(nfces))
	err = True
	if len(nfces) > 0:
		while err:
			try:
				main(nfces)
				err = False
			except NoSuchElementException:
				err = True
				print('err')
		now = datetime.now()
		print(now)
	else:
		seconds = ((randint(15, 21))%7)+10
		print(seconds)
		time.sleep(seconds)


