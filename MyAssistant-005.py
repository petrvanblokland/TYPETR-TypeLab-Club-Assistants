# -*- coding: UTF-8 -*-
#
#    Assistant for RoboFont4
#    Using TYPETR-Assistant library classes.
#
#    MyAssistant-005.py
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
    INIT_MERZ_METHODS = [ # These get called on opening the Installer window.
        'initMerzOverlay',
    ]

class MyAssistantController(
        AssistantController,
        AssistantModuleOverlay, # Add library function part source as inherited class.
	):    
    W = 450
    H = 250
    
    NAME = 'My Assistant'

    # This is where our demo UFO files live. Change to default ufo/ in your project
    UFO_PATH = 'ufo-try/' 

    # This will create missing MASTERS_DATA and GLYPH_DATA sources, based on UFO files in UFO_PATH
    MAKE_MISSING_MASTERS_DATA_GLYPH_DATA = True 

    PROJECT_PATH = __file__ # Let the AssistantContoller know where this proj4ct file is.
    ADD_GLOBAL_BUTTONS = False # For now, keep it simple

    BUILD_UI_METHODS = [
        'buildOverlay',
    ]
    assistantGlyphEditorSubscriberClass = MyAssistant
    
if __name__ == '__main__':
   OpenWindow(MyAssistantController)
    