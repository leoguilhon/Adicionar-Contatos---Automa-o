import pyautogui as pat
import time

pat.click("excel.PNG") #posição Excel
time.sleep(1)

pat.PAUSE = .5

for i in range(733):
    pat.keyDown('ctrl')
    pat.press('c')
    pat.keyUp('ctrl')
    pat.click("chrome.PNG") #posição google chrome
    pat.click("app.PNG") #posição InTouchApp
    pat.click("nome.PNG") #posição Nome
    pat.hotkey('Ctrl','V')
    pat.click("excel.PNG") #posição Excel
    pat.press('right')
    pat.keyDown('ctrl')
    pat.press('c')
    pat.keyUp('ctrl')
    pat.click("chrome.PNG") #posição google chrome
    pat.click("numero.PNG") #posição Celular
    pat.hotkey('Ctrl','V')
    pat.click("salvar.PNG",clicks=2) #posição Adicionar Contato
    pat.moveTo(725, 335)
    adicionado = pat.locateOnScreen("adicionado.PNG")
    while adicionado == None:
        adicionado = pat.locateOnScreen("adicionado.PNG")
    pat.click("app2.PNG") #posição InTouchApp
    pat.click("excel.PNG") #posição Excel
    pat.press('down')
    pat.press('left')


#atualizar as posições com pyautogui.position() no Idle





