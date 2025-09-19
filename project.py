import pyautogui
import pandas as pd


produtos = pd.read_csv("produtos.csv")

print(produtos)

pyautogui.PAUSE = 5

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
    if produtos["obs"][linha] == "nan":
        pyautogui.press("tab")
    else:
        pyautogui.write(produtos["obs"][linha])
        pyautogui.press("enter")
    pyautogui.scroll(1000)

