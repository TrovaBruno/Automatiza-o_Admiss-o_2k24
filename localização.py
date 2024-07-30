import pyautogui
import time

# Função para obter as coordenadas atuais do mouse
def obter_posicao_mouse():
    x, y = pyautogui.position()
    return x, y

# Movendo o mouse para a posição obtida
def mover_mouse_para_posicao(x, y):
    pyautogui.moveTo(x, y, duration=1)  # Movimento com duração de 1 segundo

# Script principal
if __name__ == "__main__":
    print("Posicione o mouse no ponto desejado e aguarde 10 segundos...")
    time.sleep(10)  # Aguarde 5 segundos para o usuário posicionar o mouse
    x, y = obter_posicao_mouse()
    print(f"Coordenadas obtidas: X={x}, Y={y}")
    print("Movendo o mouse para a posição obtida em 3 segundos...")
    time.sleep(10)
    mover_mouse_para_posicao(x, y)
    print("Movimento concluído!")
