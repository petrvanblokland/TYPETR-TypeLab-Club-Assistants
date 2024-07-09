# -*- coding: UTF-8 -*-
#
#    Assistant for RoboFont4
#    Using TYPETR-Assistant library classes.
#
#    MyAssistant-004.py
#
import sys, os

# Add paths to libs in sibling repositories. The assistantLib module contains generic code for Asistanta.s
PATHS = ['../TYPETR-TypeLab-Club-Assistants/']
for path in PATHS:
    if not os.path.exists(path):
        print(f'@@@ Locate this file on the top of the project repository and make sure that {path} exists.')
    if not path in sys.path:
        print(f'@@@ Append {path} to sys.path')
        sys.path.append(path)

from assistantLib.baseAssistant import (
	Assistant, AssistantController)
from assistantLib.assistantModules.overlay import AssistantModuleOverlay

class MyAssistant(
        Assistant, 
        AssistantModuleOverlay, # Add library function part source as inherited class.
	):
    pass	
class MyAssistantController(
        AssistantController,
        AssistantModuleOverlay, # Add library function part source as inherited class.
	):    
    W = 450
    H = 250
    
    NAME = 'My Assistant'

    MASTER_DATA = {} # This will contain all meta information about the masters as MasterData instances.
    PROJECT_PATH = __file__ # Let the AssistantContoller know where this proj4ct file is.
    ADD_GLOBAL_BUTTONS = False # For now, keep it simple

    BUILD_UI_METHODS = [
        'buildOverlay',
    ]
    
if __name__ == '__main__':
   OpenWindow(MyAssistantController)
    