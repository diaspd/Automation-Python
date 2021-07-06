import pyautogui
import time
import pyperclip
#import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(6) 

link = "Link google drive"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")


time.sleep(4) 
pyautogui.click(271, 287, clicks=1)

time.sleep(3) 
pyautogui.click(281, 364)
pyautogui.click(1114, 179)
pyautogui.click(968, 475)
time.sleep(10)

#tabela = pd.read_excel(r"C:\Users\along\Downloads\vendas-dez.xlsx")
#faturamento = tabela["valor final"].sum()
#quantidade = tabela["quantidade"].sum()
#display(tabela)

pyautogui.hotkey("ctrl", "t")
link = "e-mail"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(10) 
pyautogui.click(61, 186)

time.sleep(5) 
pyautogui.write("exemplo@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

assunto = "Assunto"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

texto_email = """

---------------------------------

===============================
(faturamento)
===============================
(quantidade)

---------------------------------

"""

pyautogui.write(texto_email)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")