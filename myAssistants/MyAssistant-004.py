# -*- coding: UTF-8 -*-
#
#    Assistant for RoboFont4
#    Using TYPETR-Assistant library classes.
#
#    MyAssistant-004.py
#
import sys

from assistantLib.baseAssistant import (
	Assistant, AssistantController)
from assistantLib.assistantParts.overlay import AssistantPartOverlay

# Add paths to libs in sibling repositories
PATHS = ('../TYPETR-Assistants/',)
for path in PATHS:
    if not path in sys.path:
        print('@@@ Append to sys.path', path)
        sys.path.append(path)
	
class MyAssistant(
        Assistant, 
        AssistantPartOverlay, # Add library function part source as inherited class.
	):
    pass	
class MyAssistantController(
        AssistantController,
        AssistantPartOverlay, # Add library function part source as inherited class.
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
    