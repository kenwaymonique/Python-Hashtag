#Passo 1: Pegar as cotações (dólar, euro, ouro)
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

navegador.get("https://www.google.com.br/")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute("value")
cto = cotacao_ouro.replace(",",".")
print(cto)

#Passo 2: Base de dados
import pandas as pd
tabela = pd.read_excel("Produtos.xlsx")

#Passo 3: Atualizar os valores

tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro","Cotação"] = float(cto)
print(tabela['Cotação'])

tabela["Preço de Compra"] = tabela['Cotação']*tabela['Preço Original']
tabela['Preço de Venda'] = tabela['Preço de Compra']*tabela['Margem']
print(tabela)

#Passo 4: Exportar
tabela.to_excel("Produtos Novo.xlsx", index=False)