import pyautogui
import pyperclip
import pandas
import time #-> permite personalizar o tempo por linha

#time.sleep(5) (pausa de 5 segundas após aquela linha)
#pyautogui.cick
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa 
pyautogui.press('win')
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

# Passo 2: Navegar até o local do relatório 
time.sleep(5)
pyautogui.click(x=472, y=391, clicks=2) #x e y podem ser adpatados para determinada resolução

# Passo 3: Exportar o relatório (download)
time.sleep(2)
pyautogui.rightClick(x=472, y=391)
time.sleep(5)
pyautogui.click(x=574, y=908)
time.sleep(2)

# Passo 4: Calcular os indicadores(faturamento e quantidade de produtos)
tabela = pandas.read_excel(r"C:\Users\moniq\Downloads\Vendas - Dez.xlsx")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)

# Passo 5: Eviar o e-mail para a diretoria 

#Abrir aba e entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(5)

#Clicar no botão escrever
#print(pyautogui.position())
pyautogui.click(x=150, y=271)
#Preencher as informações
pyautogui.write("moniquebseixas@hotmail.com")
pyautogui.press('tab') #seleciona o email
pyautogui.press('tab') #pula para o campo assunto
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey("ctrl", "v")
pyautogui.press('tab')
texto = f"""Prezados, bom dia
O faturamento do dia foi de: {faturamento:,.2f}
A quantidade de produtos foi de:{quantidade:,}

Att
Monique """
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
#Enviar
pyautogui.hotkey("ctrl","enter")



