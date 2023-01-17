import pyperclip
import time
from pywinauto.keyboard import send_keys

f = open('<file>', 'r', encoding='utf-8')
time.sleep(5)  

for words in f:
    print(words)
    pyperclip.copy(words)
    send_keys("^v")
    send_keys("{ENTER}")
    time.sleep(3)
