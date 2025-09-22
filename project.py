import pyautogui
import pandas as pd
import time


produtos = pd.read_csv("produtos.csv")

print(produtos)
pyautogui.PAUSE = 3

#abrindo sistema
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#login
pyautogui.press("esc")
pyautogui.press("tab")
pyautogui.write("login")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")

#cadastrando os produtos
pyautogui.press("esc")
pyautogui.PAUSE = 1

for linha in produtos.index:
    
    pyautogui.click(x=517, y=279)
    pyautogui.write(produtos["codigo"][linha])
    pyautogui.press("tab")
    pyautogui.write(produtos["marca"][linha])
    pyautogui.press("tab")
    pyautogui.write(produtos["tipo"][linha])
    pyautogui.press("tab")
    pyautogui.write(str(produtos["categoria"][linha]))
    pyautogui.press("tab")
    pyautogui.write(str(produtos["preco_unitario"][linha]))
    pyautogui.press("tab")
    pyautogui.write(str(produtos["custo"][linha]))
    pyautogui.press("tab")
    if pd.isna(produtos["obs"][linha]):
        pyautogui.press("enter")
    else:
        pyautogui.write(str(produtos["obs"][linha]))
        pyautogui.press("enter")
    #Celular    pyautogui.click(x=632, y=603)
    #pyautogui.click(x=767, y=613)
    pyautogui.scroll(1000)

