import webbrowser
import pyautogui
import time

# URL que você quer abrir
url = "https://lwp.service-now.com/nav_to.do?uri=%2Fhome_splash.do%3Fsysparm_direct%3Dtrue"

x, y = 3300, 272

# Caminho para o executável do Google Chrome
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# Abre a URL no Google Chrome
webbrowser.get(chrome_path).open(url)

time.sleep(20)

pyautogui.moveTo(x,y)

time.sleep(1)
pyautogui.click(duration=0.5)
