import PySimpleGUI as sg
import random
from time import sleep


# deklarerar varibaler
currentNum = []
full = []
historyList = []
result = ""
sizeList = [(400, 650), (300, 400), (900, 900), (400, 900), (100, 1000)]
numList = ["1", "2", "3", "4" ,"5" ,"6", "7", "8", "9", "0", ".", "/", "*", "+", "-"]
numList2 = ["1", "2", "3", "4" ,"5" ,"6", "7", "8", "9", "0", ".", "/", "*", "+", "-"]
random.shuffle(numList)
colorList = ["black", "green", "red", "blue"]
buttonSize = (8, 3) 
sg.theme("DarkRed2")
sg.set_options(font = ("Bodoni MT Fet", 14))



# Skapar layouten för GUI:n
layout = [
    [sg.Text("0", key = "TEXT", font=("Bodoni MT Fet", 34))], 
    [sg.Button("Clear", expand_x=True, size=buttonSize), sg.Button("Enter", expand_x=True, size=buttonSize),],     
    [sg.Button(numList[3], size=buttonSize, key=numList[3] ), sg.Button(numList[4], size=buttonSize, key=numList[4] ), sg.Button(numList[11], size=buttonSize, key=numList[11] ), sg.Button(numList[12], size=buttonSize, key=numList[12] )], 
    [sg.Button(numList[2],size=buttonSize, key=numList[2] ), sg.Button(numList[5],size=buttonSize, key=numList[5] ), sg.Button(numList[10], size=buttonSize, key=numList[10] ), sg.Button(numList[13], size=buttonSize, key=numList[13]  )], 
    [sg.Button(numList[0], size=buttonSize, key=numList[0]), sg.Button(numList[6], size=buttonSize, key=numList[6]), sg.Button(numList[9], size=buttonSize, key=numList[9] ), sg.Button(numList[14],size=buttonSize, key=numList[14])], 
    [sg.Button(numList[1], expand_x=True, size=buttonSize, key=numList[1]), sg.Button(numList[7], size=buttonSize, key=numList[7]), sg.Button(numList[8], size=buttonSize, key=numList[8])],
    [sg.Button("History", expand_x=True, size=buttonSize )]]


# Skapar fönstret
window = sg.Window("troll calcultator", layout, size=(400, 650),)


# Loop för fönstret
while True:
    
    error = False
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
   
    if window[event].get_text() in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        currentNum.append(window[event].get_text())
        num = "".join(currentNum)
        window["TEXT"].update(num)
    
    if window[event].get_text() in ["-", "+", "*", "/"]:
        full.append("".join(currentNum))
        currentNum.clear()
        full.append(window[event].get_text())
        window["TEXT"].update(window[event].get_text())
    
    if event == "Enter":
        full.append("".join(currentNum))
        recent = "".join(full)
        try:
            result = eval("".join(full))
            window["TEXT"].update(result)
            historyList.append(str(recent) + " = " +  str(result))

        except ZeroDivisionError:
            window["TEXT"].update("Cannot divide by zero")
            window["TEXT"].update(font=("Bodoni MT Fet", 15))
            error = True
        
        except:   
            window["TEXT"].update("Something went wrong")
            window["TEXT"].update(font=("Bodoni MT Fet", 15))
            error = True
      
        currentNum.clear()
        full.clear()

    if len(currentNum) > 16 or len(str(result)) > 16:
         window["TEXT"].update(font=("Bodoni MT Fet", 20))
         if len(currentNum) > 27 or len(str(result)) > 27:
             window["TEXT"].update(font=("Bodoni MT Fet", 15))

    elif error == False: 
        window["TEXT"].update(font=("Bodoni MT Fet", 34))

    if event == "Clear":
        currentNum.clear()
        full.clear()
        window["TEXT"].update("0")

    # visar historik
    if event == "History":
        sg.PopupNoButtons("\n".join(historyList), title="History", relative_location=(300, 0), font=("Bodoni MT Fet", 20), modal=False)
    
    # förflyttat och ändrar strorlek på fönstret
    window.disappear()
    window.move(random.randint(450, 1400), random.randint(50, 100))
    window.set_size(random.choice(sizeList))
    sleep(0.4)
    
    numList2 = ["1", "2", "3", "4" ,"5" ,"6", "7", "8", "9", "0", ".", "/", "*", "+", "-"]
    
    for x in numList:
        num = random.choice(numList2)
        numList2.remove(num)
        window[x].update(num)
  
    window.reappear()
