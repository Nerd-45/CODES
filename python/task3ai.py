import pyautogui,time
time.sleep(7)
f=open('', 'r')
for word in f:
    pyautogui.typewriter(word)
    pyautogui.press('enter')
    
