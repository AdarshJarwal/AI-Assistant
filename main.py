import os
import eel
# from engine.features import *
# from engine.command import *
eel.init('www')

# playAssistantSound()
os.system('start chrome.exe --app="http://localhost:8000/www/index.html"')
eel.start('index.html', mode='edge', host='localhost', block=True)