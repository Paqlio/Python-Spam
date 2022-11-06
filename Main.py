import keyboard
import time
import sys

exitProgram = False


#Funkcja do wyjścia z programu
def quit():
    global exitProgram
    exitProgram = True

#Wyjście z programu
keyboard.add_hotkey('q', lambda: quit())

#Pętla główna
while not exitProgram:
    time.sleep(1)
    text = open('msg.txt')
    for each_line in text:
        keyboard.write(each_line)
        keyboard.press('enter')

print("Proces zakończony")
sys.exit()