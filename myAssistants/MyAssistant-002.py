# -*- coding: UTF-8 -*-
#
#    Assistant for RoboFont4
#    Using TYPETR-Assistant library classes.
#
#    MyAssistant-002.py
#
import sys

from assistantLib.baseAssistant import (
	Assistant, AssistantController)

# Add paths to libs in sibling repositories
PATHS = ('../TYPETR-Assistants/',)
for path in PATHS:
    if not path in sys.path:
        print('@@@ Append to sys.path', path)
        sys.path.append(path)
	
class MyAssistant(
		Assistant, 
	):
    pass	
class MyAssistantController(
		AssistantController, 
	):
	MASTER_DATA = {} # This will contain all meta information about the masters as MasterData instances.
	PROJECT_PATH = __file__ # Let the AssistantContoller know where this proj4ct file is.
	ADD_GLOBAL_BUTTONS = False # For now, keep it simple


if __name__ == '__main__':
   OpenWindow(MyAssistantController)
