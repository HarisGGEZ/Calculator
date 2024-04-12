import PySimpleGUI as sg


currentNum = []
full = []
buttonSize = (8, 3)
sg.theme("black")



layout = [
    [sg.Text("Output", key="TEXT")],
    [sg.Button("Clear", expand_x=True, size=buttonSize), sg.Button("Enter", expand_x=True, size=buttonSize)],
    [sg.Button(7, size=buttonSize),sg.Button(8, size=buttonSize),sg.Button(9, size=buttonSize),sg.Button("*", size=buttonSize)],
    [sg.Button(4, size=buttonSize),sg.Button(5, size=buttonSize),sg.Button(6, size=buttonSize) ,sg.Button("/", size=buttonSize)],
    [sg.Button(1, size=buttonSize),sg.Button(2, size=buttonSize),sg.Button(3, size=buttonSize),sg.Button("+", size=buttonSize)],
    [sg.Button(0, expand_x=True, size=buttonSize),sg.Button(".", size=buttonSize),sg.Button("-", size=buttonSize)]]



window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event  in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        currentNum.append(event)
        num = "".join(currentNum)
        window["TEXT"].update(num)
    
    if event in ["-", "+", "*", "/"]:
        full.append("".join(currentNum))
        currentNum.clear()
        full.append(event)
        window["TEXT"].update(event)

    if event == "Enter":
        full.append("".join(currentNum))
        recent = "".join(full)
        result = eval("".join(full))
        window["TEXT"].update(result)
        full.clear()

    if event == "Clear":
        currentNum.clear()
        full.clear()
        window["TEXT"].update("0")
        

        

