# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Copyright (c) 2023+ TYPETR
#     Usage by MIT License
# ..............................................................................
#
#   docTestAssistants.py
#
import sys

from fontParts.fontshell.font import RFont

from assistantLib import *
from assistantLib.assistantModules import *
from assistantLib.assistantModules.glyphsets import *

from assistantLib.assistantModules.glyphsets.anchorData import *
from assistantLib.assistantModules.glyphsets.glyphData import *
from assistantLib.assistantModules.glyphsets.glyphSet import *
from assistantLib.assistantModules.glyphsets.MS_WGL4_segoe import *
from assistantLib.assistantModules.glyphsets.TYPETR_UpgradeNeon_set import *

from assistantLib.assistantModules.data import MasterData
from assistantLib.assistantModules.spacingKerning.kerningManager import KerningManager

SEGOEUI_DISPLAY_REGULAR_ITALIC = 'Segoe_UI_Display-Regular_Italic_MA168.ufo'
ufoName = SEGOEUI_DISPLAY_REGULAR_ITALIC
ufoPath = '../TYPETR-Segoe-UI-Italic/ufo/' + ufoName
f = RFont(ufoPath)

# Test GlyphSet
from assistantLib.assistantModules.glyphsets.TYPETR_full_set import TYPETR_GlyphSet 
#glyphSet = TYPETR_GlyphSet()
glyphSet = MS_GlyphSet()
md = MasterData(name=ufoName, glyphSet=glyphSet)

gs = md.glyphSet
gd = gs['kstroke']

g = f[gd.name]
km = KerningManager(f, md)
print(km.getLeftMarginByGlyphSetReference(g))

g = f['H']
print(km.getLeftMarginByGlyphSetReference(g))
print(km.getRightMarginByGlyphSetReference(g))