import wolframalpha
client = wolframalpha.Client("XLAUKL-HQWPPX64R3")
import wikipedia

import PySimpleGUI as sg
# Define the window's contents
layout = [[sg.Text("Enter Something, Anything, No, Really Anything"), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]
# Create the window
window = sg.Window('Jarvis', layout)

import pyttsx3
engine = pyttsx3.init()

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event in (None, 'Cancel'):
        break
    try:
        wiki_result = wikipedia.summary(values[0], sentences=2)
        wolfram_result = next(client.query(values[0]).results).text
        engine.say(wolfram_result)
        sg.PopupNonBlocking("Wolfram results: "+ wolfram_result, "Wikipedia Results: " + wiki_result)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_result = next(client.query(values[0]).results).text
        engine.say(wolfram_result)
        sg.PopupNonBlocking(wolfram_result)
    except wikipedia.exceptions.PageError:
        wolfram_result = next(client.query(values[0]).results).text
        engine.say(wolfram_result)
        sg.PopupNonBlocking(wolfram_result)
    except:
        wiki_result = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_result)
        sg.PopupNonBlocking(wiki_result)


    engine.runAndWait()

    print(values[0])

window.close()
