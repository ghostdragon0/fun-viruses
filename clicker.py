import random, pyautogui as pyauto
for x in range(15):
    h = random.randint(0,1080)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration = 0.3)
    pyauto.hotkey('winleft', 'm')
