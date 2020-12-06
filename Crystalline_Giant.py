import random
import PySimpleGUI as sg

#set the look of the GUI
sg.theme = ("darkTeal2")

layout = [
		 [sg.Text("Crystalline Giant Counters")],
		 [sg.Text(size = (100,1), key = "-output-")],
		 [sg.Button("Counter"), sg.Button("Clear")]

		 ]

window = sg.Window("Crystalline Giant Counters", layout)

#dictionary of  abilities of the card crystalline giant
abilities = {
        1: "Flying",
        2: "First strike",
        3: "Deathtouch",
        4: "Hexproof",
        5: "Lifelink",
        6: "Menace",
        7: "Reach",
        8: "Trample",
        9: "Vigilance",
        10: "+1/+1"
        }

abilities_list = []

#function for finding an ability that hasnt been found yet and adding it to abilities_list
def ability_counters():
	
	choice = random.randint(1, 10)
	if abilities[choice] not in abilities_list:
		abilities_list.append(abilities[choice])
	return abilities_list

#main loop of the program
while True:
	event, values = window.Read()

	if event == None:
		break

	elif event == "Counter":
		window['-output-'].update(ability_counters())
	#if the card dies or is exiled clear the abilities 
	elif event == "Clear":
		abilities_list.clear()
		window["-output-"].update(" ")
#close the program
window.close()
