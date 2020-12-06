import random
import PySimpleGUI as sg

#theme = [darkTeal2]

layout = [
		 [sg.Text("Crystalline Giant Counters")],
		 [sg.Text(size = (100,1), key = "-output-")],
		 [sg.Button("Counter"), sg.Button("Clear")]

		 ]
window = sg.Window("Crystalline Giant Counters", layout)

abilities = {1: "Flying", 2: "First strike", 3: "Deathtouch", 4: "Hexproof", 5: "Lifelink", 6: "Menace", 7: "Reach", 8: "Trample", 9: "Vigilance", 10: "+1/+1"}
abilities_list = []
def ability_counters():
	
	choice = random.randint(1, 10)
	if abilities[choice] not in abilities_list:
		abilities_list.append(abilities[choice])
	return abilities_list

while True:
	event, values = window.Read()

	if event == None:
		break

	if event == "Counter":
		window['-output-'].update(ability_counters())
	elif event == "Clear":
		abilities_list.clear()
		window["-output-"].update(" ")
window.close()