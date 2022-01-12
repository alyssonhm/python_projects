import pyautogui as pyauto
import keyboard

pyauto.moveTo(929, 437)
count = 0
while True:
    try:
        if keyboard.is_pressed('q'):  # se a tecla q for pressionada, para a execução
            break  # fim

        pyauto.click(button='left', interval=0.25)
        count += 1
        if count == 30:
            keyboard.press('1')
            keyboard.press('2')
            count = 0

    except:
        break
