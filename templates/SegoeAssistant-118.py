# -*- coding: UTF-8 -*-
#
#    FullAssistant-000.py, use as reference.
#
#    Assistant for RoboFont4
#    Belongs to Segoe UI project
#
#    Hairlåine tube: ]
import sys
from vanilla import *

import importlib
    
# Add paths to libs in sibling reposi]ries
PATHS = ('../TYPETR-TypeLab-Club-Assistants/',)
for path in PATHS:
    if not path in sys.path:
        print('@@@ Append to sys.path', path)
        sys.path.append(path)

import assistantLib.baseAssistant
import assistantLib.assistantModules.data
import assistantLib.assistantModules.builder
import assistantLib.assistantModules.overlay
import assistantLib.assistantModules.italicize
import assistantLib.assistantModules.curves
import assistantLib.assistantModules.contours
import assistantLib.assistantModules.components
import assistantLib.assistantModules.dimensions
import assistantLib.assistantModules.interpolate
import assistantLib.assistantModules.familyOverview
import assistantLib.assistantModules.anchors
import assistantLib.assistantModules.groups
import assistantLib.assistantModules.spacer
import assistantLib.assistantModules.guidelines
import assistantLib.assistantModules.glyphsets.anchorData
import assistantLib.assistantModules.glyphsets.groupBaseGlyphs
import assistantLib.assistantModules.glyphsets.glyphSet
import assistantLib.assistantModules.glyphsets.glyphData
import assistantLib.assistantModules.glyphsets.MS_WGL4_segoe
import assistantLib.assistantModules.spacingKerning.kerningManager

#    To implement
#
#    Interpolate part --> Interpolating live update of empty glyph, in case m1/m2 are defined. Compatibility check
#    Similar spacing part --> Find similars, create groups
#    Kerning part
#    Preview part --> Show a sample line of text in the current EditWindow. Select samples, guess for the language of the current glyph
#    Anchors part --> Also does diacritics positioning and checking on floating positions
#    Copy part --> Copy from source in case empty glyph

importlib.reload(assistantLib.assistantModules.spacingKerning.kerningManager)

importlib.reload(assistantLib.baseAssistant)
from assistantLib.baseAssistant import Assistant, AssistantController

# Auto generator for GD glyphset
importlib.reload(assistantLib.assistantModules.data)
from assistantLib.assistantModules.data import MasterData

importlib.reload(assistantLib.assistantModules.glyphsets.anchorData)
importlib.reload(assistantLib.assistantModules.glyphsets.groupBaseGlyphs)
importlib.reload(assistantLib.assistantModules.glyphsets.glyphSet)
importlib.reload(assistantLib.assistantModules.glyphsets.MS_WGL4_segoe)
importlib.reload(assistantLib.assistantModules.glyphsets.glyphData)

from assistantLib.assistantModules.glyphsets.MS_WGL4_segoe import MS_GlyphSet

# Add to overlay part: [B] and [Q] for curve conversion, and smoothing conversion to circle
# Add [x] Regular to show md.m0 on right side instead
importlib.reload(assistantLib.assistantModules.builder)
from assistantLib.assistantModules.builder import AssistantModuleBuilder

importlib.reload(assistantLib.assistantModules.overlay)
from assistantLib.assistantModules.overlay import AssistantModuleOverlay

importlib.reload(assistantLib.assistantModules.italicize)
from assistantLib.assistantModules.italicize import AssistantModuleItalicize

importlib.reload(assistantLib.assistantModules.curves)
from assistantLib.assistantModules.curves import AssistantModuleCurves

importlib.reload(assistantLib.assistantModules.contours)
from assistantLib.assistantModules.contours import AssistantModuleContours

importlib.reload(assistantLib.assistantModules.components)
from assistantLib.assistantModules.components import AssistantModuleComponents

importlib.reload(assistantLib.assistantModules.dimensions)
from assistantLib.assistantModules.dimensions import AssistantModuleDimensions

importlib.reload(assistantLib.assistantModules.interpolate)
from assistantLib.assistantModules.interpolate import AssistantModuleInterpolate

importlib.reload(assistantLib.assistantModules.familyOverview)
from assistantLib.assistantModules.familyOverview import AssistantModuleFamilyOverview

importlib.reload(assistantLib.assistantModules.anchors)
from assistantLib.assistantModules.anchors import AssistantModuleAnchors

importlib.reload(assistantLib.assistantModules.groups)
from assistantLib.assistantModules.groups import AssistantModuleGroups

importlib.reload(assistantLib.assistantModules.spacer)
from assistantLib.assistantModules.spacer import AssistantModuleSpacer

importlib.reload(assistantLib.assistantModules.guidelines)
from assistantLib.assistantModules.guidelines import AssistantModuleGuidelines

class MS_MasterData(MasterData):
    DEFAULT_TAB_WIDTH = 2222

# Tab widths of /zero.tnum
#    Weight    Roman        Italic

#    Display
#    Black     1465
#    Bold      1178        1240
#    Regular   1104        1240 (1104)
#    Light     1055        1240 (1055)
#    Hairline  1027        1240 (1027)

#    Text
#    Black     1336
#    Bold      1178        1260 (1178)
#    Regular   1104        1260 (1104)
#    Light     1055        1260 (1055)
#    Hairline  1039        1260 (1039)

#    Small
#    Black     1364
#    Bold      1211        1280
#    Regular   1163        1280
#    Light     1142        1280
#    Hairline  1085        1280
  
MD = MS_MasterData

OVERSHOOT = 24
XHEIGHT = 1024
XHEIGHT_SMALL = 1080
CAPHEIGHT = 1434
SUPSHEIGHT = 768
ASCENDER = 1516
DESCENDER = -471
MODBASELINE = 666
DIACRITICS_TOP = 1216
DIACRITICS_TEXT_TOP = 1216
DIACRITICS_SMALL_TOP = 1260
CAP_DIACRITICS_TOP = 1560 # Bottom of captical diacritics guideline
CAP_DIACRITICS_TEXT_TOP = 1570 # Bottom of captical diacritics guideline
CAP_DIACRITICS_SMALL_TOP = 1570 # Bottom of captical diacritics guideline
      
class SegoeUIItalicAssistant(Assistant, 
        AssistantModuleOverlay, 
        AssistantModuleFamilyOverview, 
        AssistantModuleItalicize,
        AssistantModuleInterpolate,
        AssistantModuleCurves,
        AssistantModuleContours,
        AssistantModuleComponents,
        AssistantModuleDimensions,
        AssistantModuleGroups,
        AssistantModuleSpacer,
        AssistantModuleAnchors,
        AssistantModuleGuidelines,
        AssistantModuleBuilder,
        ):
            
    PROJECT_PATH = __file__

    ITALIC_ANGLE = -12
       
    # Overlay colors
    OVERLAY_FILL_SRC_COLOR = 0, 0.3, 0.8, 0.3
    OVERLAY_FILL_COLOR = 0, 0, 0, 0.3
    
    UFO_PATH = 'ufo/'
   
    SEGOEUI_DISPLAY_HAIRLINE_ITALIC = 'Segoe_UI_Display-Hairline_Italic_MA32.ufo'
    SEGOEUI_DISPLAY_LIGHT_ITALIC = 'Segoe_UI_Display-Light_Italic_MA98.ufo'
    SEGOEUI_DISPLAY_REGULAR_ITALIC = 'Segoe_UI_Display-Regular_Italic_MA168.ufo'
    SEGOEUI_DISPLAY_BOLD_ITALIC = 'Segoe_UI_Display-Bold_Italic_MA323.ufo'

    SEGOEUI_TEXT_HAIRLINE_ITALIC = 'Segoe_UI_Text-Hairline_Italic_MA62.ufo'
    SEGOEUI_TEXT_LIGHT_ITALIC = 'Segoe_UI_Text-Light_Italic_MA98.ufo'
    SEGOEUI_TEXT_REGULAR_ITALIC = 'Segoe_UI_Text-Regular_Italic_MA168.ufo'
    SEGOEUI_TEXT_BOLD_ITALIC = 'Segoe_UI_Text-Bold_Italic_MA323.ufo'

    SEGOEUI_SMALL_HAIRLINE_ITALIC = 'Segoe_UI_Small-Hairline_Italic_MA97.ufo'
    SEGOEUI_SMALL_LIGHT_ITALIC = 'Segoe_UI_Small-Light_Italic_MA160.ufo'
    SEGOEUI_SMALL_REGULAR_ITALIC = 'Segoe_UI_Small-Regular_Italic_MA200.ufo'
    SEGOEUI_SMALL_BOLD_ITALIC = 'Segoe_UI_Small-Bold_Italic_MA300.ufo'

    UFO_PROTO_PATH = 'ufo-proto/'

    SEGOEUI_PROTO_DISPLAY_HAIRLINE_ITALIC = 'Segoe_UI_Display-Hairline_Italic_MA32.ufo'
    SEGOEUI_PROTO_DISPLAY_LIGHT_ITALIC = 'Segoe_UI_Display-Light_Italic_MA98.ufo'
    SEGOEUI_PROTO_DISPLAY_REGULAR_ITALIC = 'Segoe_UI_Display-Regular_Italic_MA168.ufo'
    SEGOEUI_PROTO_DISPLAY_BOLD_ITALIC = 'Segoe_UI_Display-Bold_Italic_MA323.ufo'
    SEGOEUI_PROTO_DISPLAY_BLACK_ITALIC = 'Segoe_UI_Display-Black_Italic_MA420.ufo'

    SEGOEUI_PROTO_TEXT_HAIRLINE_ITALIC = 'Segoe_UI_Text-Hairline_Italic_MA62.ufo'
    SEGOEUI_PROTO_TEXT_LIGHT_ITALIC = 'Segoe_UI_Text-Light_Italic_MA98.ufo'
    SEGOEUI_PROTO_TEXT_REGULAR_ITALIC = 'Segoe_UI_Text-Regular_Italic_MA168.ufo'
    SEGOEUI_PROTO_TEXT_BOLD_ITALIC = 'Segoe_UI_Text-Bold_Italic_MA323.ufo'
    SEGOEUI_PROTO_TEXT_BLACK_ITALIC = 'Segoe_UI_Text-Black_Italic_MA420.ufo'

    SEGOEUI_PROTO_SMALL_HAIRLINE_ITALIC = 'Segoe_UI_Small-Hairline_Italic_MA97.ufo'
    SEGOEUI_PROTO_SMALL_LIGHT_ITALIC = 'Segoe_UI_Small-Light_Italic_MA160.ufo'
    SEGOEUI_PROTO_SMALL_REGULAR_ITALIC = 'Segoe_UI_Small-Regular_Italic_MA200.ufo'
    SEGOEUI_PROTO_SMALL_BOLD_ITALIC = 'Segoe_UI_Small-Bold_Italic_MA300.ufo'
    SEGOEUI_PROTO_SMALL_BLACK_ITALIC = 'Segoe_UI_Small-Black_Italic_MA420.ufo'
   
    UFO_ROMAN_PATH = '../TYPETR-Segoe-UI/ufo/'

    SEGOEUI_DISPLAY_HAIRLINE = 'Segoe_UI_Display-Hairline_MA32.ufo'
    SEGOEUI_DISPLAY_LIGHT = 'Segoe_UI_Display-Light_MA98.ufo'
    SEGOEUI_DISPLAY_REGULAR = 'Segoe_UI_Display-Regular_MA168.ufo'
    SEGOEUI_DISPLAY_BOLD = 'Segoe_UI_Display-Bold_MA323.ufo'
    SEGOEUI_DISPLAY_BLACK = 'Segoe_UI_Display-Black_MA420.ufo'

    SEGOEUI_TEXT_HAIRLINE = 'Segoe_UI_Text-Hairline_MA62.ufo'
    SEGOEUI_TEXT_LIGHT = 'Segoe_UI_Text-Light_MA98.ufo'
    SEGOEUI_TEXT_REGULAR = 'Segoe_UI_Text-Regular_MA168.ufo'
    SEGOEUI_TEXT_BOLD = 'Segoe_UI_Text-Bold_MA323.ufo'
    SEGOEUI_TEXT_BLACK = 'Segoe_UI_Text-Black_MA420.ufo'

    SEGOEUI_SMALL_HAIRLINE = 'Segoe_UI_Small-Hairline_MA97.ufo'
    SEGOEUI_SMALL_LIGHT = 'Segoe_UI_Small-Light_MA160.ufo'
    SEGOEUI_SMALL_REGULAR = 'Segoe_UI_Small-Regular_MA200.ufo'
    SEGOEUI_SMALL_BOLD = 'Segoe_UI_Small-Bold_MA300.ufo'
    SEGOEUI_SMALL_BLACK = 'Segoe_UI_Small-Black_MA420.ufo'
   
    # Used by familyOverview
    UFO_PATHS = [ # Define the order of display
        UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC,
        UFO_PATH + SEGOEUI_DISPLAY_LIGHT_ITALIC,
        UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
        UFO_PATH + SEGOEUI_DISPLAY_BOLD_ITALIC,

        UFO_PATH + SEGOEUI_TEXT_HAIRLINE_ITALIC,
        UFO_PATH + SEGOEUI_TEXT_LIGHT_ITALIC,
        UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
        UFO_PATH + SEGOEUI_TEXT_BOLD_ITALIC,

        UFO_PATH + SEGOEUI_SMALL_HAIRLINE_ITALIC,
        UFO_PATH + SEGOEUI_SMALL_LIGHT_ITALIC,
        UFO_PATH + SEGOEUI_SMALL_REGULAR_ITALIC,
        UFO_PATH + SEGOEUI_SMALL_BOLD_ITALIC,
    ]
    TMP_OFF = [
    ]
    # MassterData attributes
    #
    # name=None, ufoPath=UFO_PATH, 
    # srcUFOPath=None, someUFOPath=None, orgUFOPath=None, kerningSrcUFOPath=None, romanItalicUFOPath=None, 
    # italicAngle=0, rotation=0, 
    # thickness=10, distance=16, # Used for Neon tubes
    # m0=None, m1=None, m2=None, sm1=None, sm2=None, dsPosition=None,
    # tripletData1=None, tripletData2=None, featurePath=None, 
    # glyphData=None, metrics=None,
    # HStem=None, HThin=None, OStem=None, OThin=None,
    # HscStem=None, HscThin=None, OscStem=None, OscThin=None,
    # nStem=None, oStem=None, oThin=None, UThin=None, VThin=None, eThin=None,
    # ttfPath=None, platformID=None, platEncID=None, langID=None, 
    # unitsPerEm=UNITS_PER_EM, copyright=COPYRIGHT, uniqueID=None, trademark=TRADEMARK, 
    # lowestRecPPEM=LOWEST_PPEM,
    # familyName=None, styleName=None,
    # fullName=None, version=None, versionMajor=VERSION_MAJOR, versionMinor=VERSION_MINOR,
    # postscriptName=None, preferredFamily=None, preferredSubFamily=None,
    # openTypeOS2WinAscent=None, openTypeOS2WinDescent=None,
    # openTypeOS2Type=[2, 8], # fsType, TN standard
    # vendorURL=None, manufacturerURL=None, manufacturer=None,
    # designerURL=None, designer=None, 
    # eulaURL=None, eulaDescription=None,
    # underlinePosition=None, underlineThickness=None

    GS = MS_GlyphSet()
    
    MASTERS_DATA = {
        
        #    D I S P L A Y
        
        SEGOEUI_DISPLAY_HAIRLINE_ITALIC: MD(
            name=SEGOEUI_DISPLAY_HAIRLINE_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            kerningSrcUFOPath=None,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_DISPLAY_HAIRLINE_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_DISPLAY_HAIRLINE,
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=2, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=32, # Stems from roman used as diagonal stem reference.
            HThin=31,
            nStem=31,
            OStem=32,
            OThin=31,
            oStem=31,
            oThin=31,
            tabWidth=1240, # Instead of copy 1027 from Segoe UI Rmoan
            # Vertical metrics
            #ascenderAnchorOffsetY= -AD.ANCHOR_ASCENDER_OFFSET,
            #boxTopAnchorOffsetY= -AD.ANCHOR_BOXTOP_OFFSET,
            capHeightAnchorOffsetY= -56, # Optional vertical offset of cap-anhors or lower capital diacritics.
            #xHeightAnchorOffsetY= -AD.ANCHOR_OFFSET,
            #baselineAnchorOffsetY=AD.ANCHOR_OFFSET,
            #ogonekAnchorOffsetY=AD.ANCHOR_OGONEK_OFFSET,
            #boxBottomAnchorOffsetY= AD.ANCHOR_BOXBOTTOM_OFFSET,
            #descenderAnchorOffsetY=AD.ANCHOR_DESCENDER_OFFSET,
            baseDiacriticsTop=DIACRITICS_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_DISPLAY_LIGHT_ITALIC: MD(
            name=SEGOEUI_DISPLAY_LIGHT_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC,
            m2=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            kerningSrcUFOPath=None,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_DISPLAY_LIGHT_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_DISPLAY_LIGHT,
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=3, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=99, # Stems from roman used as diagonal stem reference.
            HThin=89,
            nStem=92,
            OStem=102,
            OThin=89,
            oStem=96,     
            oThin=86,       
            tabWidth=1240, # Instead of copy 1055 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_DISPLAY_REGULAR_ITALIC: MD(
            name=SEGOEUI_DISPLAY_REGULAR_ITALIC, 
            glyphSet=GS,
            # m0: Is compatible to itself
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            kerningSrcUFOPath=None,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_DISPLAY_REGULAR_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_DISPLAY_REGULAR,
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=3, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=168, # Stems from roman used as diagonal stem reference.
            HThin=151,
            nStem=164,
            OStem=176,
            OThin=151,
            oStem=168,
            oThin=140,
            tabWidth=1240, # Instead of copy 1104 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_DISPLAY_BOLD_ITALIC: MD(
            name=SEGOEUI_DISPLAY_BOLD_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            kerningSrcUFOPath=None,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_DISPLAY_BOLD_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_DISPLAY_BOLD,
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=5, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=323, # Stems from roman used as diagonal stem reference.
            HThin=286,
            nStem=316,
            OStem=340,
            OThin=282,
            oStem=320,
            oThin=242,
            tabWidth=1240, # Instead of copy 1178 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),

        #    T E X T 
        
        SEGOEUI_TEXT_HAIRLINE_ITALIC: MD(
            name=SEGOEUI_TEXT_HAIRLINE_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC,
            m2=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,   
            osm1=None, # Used by familyOverview, previous weight with same optical size.      
            osm2=UFO_PATH + SEGOEUI_TEXT_LIGHT_ITALIC, # Used by familyOverview, next weight with same optical size.
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_TEXT_HAIRLINE_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_TEXT_HAIRLINE,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=2, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=2, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=62, # Stems from roman used as diagonal stem reference.
            HThin=58,
            nStem=58,
            OStem=63,
            OThin=58,
            oStem=60,
            oThin=55,
            tabWidth=1240, # Instead of copy 1039 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_TEXT_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_TEXT_LIGHT_ITALIC: MD(
            name=SEGOEUI_TEXT_LIGHT_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_TEXT_HAIRLINE_ITALIC, # Interpolating from masters of same optical size
            m2=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            osm1=UFO_PATH + SEGOEUI_TEXT_HAIRLINE_ITALIC,         
            osm2=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,         
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_TEXT_LIGHT_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_TEXT_LIGHT,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_LIGHT_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_LIGHT_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=2, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=3, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=99, # Stems from roman used as diagonal stem reference.
            HThin=91,
            nStem=92,
            OStem=102,
            OThin=91,
            oStem=96,
            oThin=85,
            tabWidth=1240, # Instead of copy 1055 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_TEXT_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TEXT_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_TEXT_REGULAR_ITALIC: MD(
            name=SEGOEUI_TEXT_REGULAR_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC,
            m2=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            osm1=UFO_PATH + SEGOEUI_TEXT_LIGHT_ITALIC,         
            osm2=UFO_PATH + SEGOEUI_TEXT_BOLD_ITALIC,         
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_TEXT_REGULAR_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_TEXT_REGULAR,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=2, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=3, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=168, # Stems from roman used as diagonal stem reference.
            HThin=151,
            nStem=164,
            OStem=176,
            OThin=151,
            oStem=168,
            oThin=140,
            tabWidth=1240, # Instead of copy 1104 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_TEXT_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TEXT_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_TEXT_BOLD_ITALIC: MD(
            name=SEGOEUI_TEXT_BOLD_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            osm1=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,         
            osm2=None,         
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_TEXT_BOLD_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_TEXT_BOLD,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_BOLD_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_BOLD_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=2, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=5, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=323, # Stems from roman used as diagonal stem reference.
            HThin=286,
            nStem=316,
            OStem=342,
            OThin=282,
            oStem=318,
            oThin=242,
            tabWidth=1240, # Instead of copy 1178 from Segoe UI Rmoan
            # Vertical metrics
             # Vertical metrics
            #ascenderAnchorOffsetY= -AD.ANCHOR_ASCENDER_OFFSET,
            #boxTopAnchorOffsetY= -AD.ANCHOR_BOXTOP_OFFSET,
            capHeightAnchorOffsetY= -56, # Optional vertical offset of cap-anhors or lower capital diacritics.
            #xHeightAnchorOffsetY= -AD.ANCHOR_OFFSET,
            #baselineAnchorOffsetY=AD.ANCHOR_OFFSET,
            #ogonekAnchorOffsetY=AD.ANCHOR_OGONEK_OFFSET,
            #boxBottomAnchorOffsetY= AD.ANCHOR_BOXBOTTOM_OFFSET,
            #descenderAnchorOffsetY=AD.ANCHOR_DESCENDER_OFFSET,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            # Vertical metrics baselines
            baseDiacriticsTop=DIACRITICS_TEXT_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_TEXT_TOP,
            baseDiacriticsBottom=-96,
            modBaseline=MODBASELINE,
            ),

        #    S M A L L
        
        SEGOEUI_SMALL_HAIRLINE_ITALIC: MD(
            name=SEGOEUI_SMALL_HAIRLINE_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_TEXT_HAIRLINE_ITALIC,
            m2=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,            
            osm1=None, # Used by familyOverview, previous weight with same optical size.      
            osm2=UFO_PATH + SEGOEUI_SMALL_LIGHT_ITALIC, # Used by familyOverview, next weight with same optical size.
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_SMALL_HAIRLINE_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_SMALL_HAIRLINE,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_HAIRLINE_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=18, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=2, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=97, # Stems from roman used as diagonal stem reference.
            HThin=89,
            nStem=92,
            OStem=101,
            OThin=89,
            oStem=96,
            oThin=96,
            tabWidth=1240, # Instead of copy 1085 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_SMALL_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_SMALL_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT_SMALL, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_SMALL_LIGHT_ITALIC: MD(
            name=SEGOEUI_SMALL_LIGHT_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_TEXT_HAIRLINE_ITALIC,  # Interpolating from masters of same optical size
            m2=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            osm1=UFO_PATH + SEGOEUI_SMALL_HAIRLINE_ITALIC,         
            osm2=UFO_PATH + SEGOEUI_SMALL_REGULAR_ITALIC,         
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_SMALL_LIGHT_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_SMALL_LIGHT,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_LIGHT_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_LIGHT_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=18, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=3, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=160, # Stems from roman used as diagonal stem reference.
            HThin=144,
            nStem=155,
            OStem=167,
            OThin=144,
            oStem=159,
            oThin=135,
            tabWidth=1240, # Instead of copy 1142 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_SMALL_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_SMALL_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT_SMALL, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_SMALL_REGULAR_ITALIC: MD(
            name=SEGOEUI_SMALL_REGULAR_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            m2=UFO_PATH + SEGOEUI_TEXT_BOLD_ITALIC,
            osm1=UFO_PATH + SEGOEUI_TEXT_LIGHT_ITALIC,         
            osm2=UFO_PATH + SEGOEUI_TEXT_BOLD_ITALIC,         
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_SMALL_REGULAR_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_SMALL_REGULAR,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=18, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=3, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=200, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            HThin=178,
            nStem=195,
            OStem=210,
            OThin=177,
            oStem=199,
            oThin=160,
            tabWidth=1240, # Instead of copy 1163 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_SMALL_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_SMALL_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT_SMALL, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,
            ),
        SEGOEUI_SMALL_BOLD_ITALIC: MD(
            name=SEGOEUI_SMALL_BOLD_ITALIC, 
            glyphSet=GS,
            m0=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            m1=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            m2=UFO_PATH + SEGOEUI_TEXT_BOLD_ITALIC,
            osm1=UFO_PATH + SEGOEUI_SMALL_REGULAR_ITALIC,         
            osm2=None,         
            orgUFOPath=UFO_PATH + SEGOEUI_TEXT_REGULAR_ITALIC,
            groupSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_REGULAR_ITALIC,
            srcUFOPath=UFO_PROTO_PATH + SEGOEUI_PROTO_SMALL_BOLD_ITALIC, 
            romanItalicUFOPath=UFO_ROMAN_PATH + SEGOEUI_SMALL_BOLD,
            kerningSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_BOLD_ITALIC,
            spacingSrcUFOPath=UFO_PATH + SEGOEUI_DISPLAY_BOLD_ITALIC, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=18, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=ITALIC_ANGLE,
            diagonalTolerance=5, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=300, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            HThin=265,
            nStem=293,
            OStem=315,
            OThin=262,
            oStem=299,
            oThin=234,
            tabWidth=1240, # Instead of copy 1211 from Segoe UI Rmoan
            # Vertical metrics
            baseDiacriticsTop=DIACRITICS_SMALL_TOP, # Bottom position of top diacritics for lower case
            capDiacriticsTop=CAP_DIACRITICS_SMALL_TOP,
            baseDiacriticsBottom=-96,
            baseOvershoot=OVERSHOOT, xHeight=XHEIGHT_SMALL, capHeight=CAPHEIGHT, supsHeight=SUPSHEIGHT, ascender=ASCENDER, descender=DESCENDER,
            modBaseline=MODBASELINE,            
            ),
    }
    INIT_MERZ_METHODS = [ # These get called on opening the Installer window.
        'initMerzOverlay',
        'initMerzFamilyOverview',    
        'initMerzGroups',    
        'initMerzSpacer',    
        'initMerzAnchors',    
        'initMerzItalicize', 
        'initMerzInterpolate',   
        'initMerzCurves',    
        'initMerzContours',    
        'initMerzComponents',    
        'initMerzDimensions',    
        'initMerzGuidelines', 
        'initMerzBuilder',
    ]
    UPDATE_MERZ_METHODS = [ # Allow the subscribed assistant parts to update their Merz elements.
        'updateMerzOverlay',
        'updateMerzFamilyOverview',
        'updateMerzAnchors', # Updating the diacritics cloud
        'updateMerzGroups',
        'updateMerzSpacer',
        'updateMerzDimensions',
        'updateMerzBuilder',
    ]
    UPDATE_METHODS = [ # Check if there is something to do. Methods should answer a “changed” boolean
        'updateInterpolate',
        'updateCurves',
        'updateContours',
        'updateComponents',
        'updateAnchors', 
        'updateGroups', 
        'updateSpacer', # Update spacing of the current glyph.
        'updateDimensions',
        'updateGuidelines',
        'updateBuilder',
    ]
    SET_GLYPH_METHODS = [ # 
        'setGlyphAnchors', # Called when the EditorWindow selects another glyph.   
        'setGlyphInterpolation', # Setup the glyph.lib-->isLower flag, overwriting the GlyphData.isLower 
        'setGlyphDimensions', # Create new GlyphAnalyzer, if it does not already exist, and show measurements
    ]
    MOUSE_MOVE_METHODS = [
        'mouseMoveFamilyOverview',
        'mouseMoveSpacer',
        'mouseMoveAnchors',
        'mouseMoveDimensions',
    ]         
    MOUSE_DOWN_METHODS = [
        'mouseDownFamilyOverview',
        'mouseDownSpacer',
        'mouseDownAnchors',
        'mouseDownDimensions',
    ]         
class SegoeUIItalicAssistantController(
        AssistantController, 
        AssistantModuleOverlay, 
        AssistantModuleFamilyOverview, 
        AssistantModuleGroups,
        AssistantModuleSpacer,
        AssistantModuleAnchors,
        AssistantModuleItalicize,
        AssistantModuleInterpolate,
        AssistantModuleCurves,
        AssistantModuleContours,
        AssistantModuleComponents,
        AssistantModuleDimensions,
        AssistantModuleGuidelines,
        AssistantModuleBuilder,
        ):

    # See other class variables to be redefined from BaseAssistantController
    W = 450
    H = 785

    PROJECT_PATH = __file__

    BUILD_VERSION = 27 # Build version number

    #DESIGN_SPACE_VF = 'SegoeUI-Italic-wght4-opsz3-vf.designspace'
    DESIGN_SPACE_VF = 'SegoeUI-Italic-wght4-vf.designspace'
                    
    NAME = 'Segoe UI Italic Assistant'
    WINDOW_CLASS = FloatingWindow

    # For Proofing
    MAX_PAGES = 1
    PROOF_FONT_PATH = '_ttf/SegUIVar.ttf'
    PROOF_FONT_ITALIC_PATH = '_ttf/SegoeUI-Italic-wght3-opsz3-vf-VF.ttf' 
    PROOF_PDF_NAME = 'SegoeUI-Italic.pdf' 
    INSTANCE_POSITIONS = [
        (dict(wght=300, opsz=24), 'Light Display'),
        (dict(wght=350, opsz=24), 'Semilight Display'),
        (dict(wght=400, opsz=24), 'Regular Display'),
        (dict(wght=550, opsz=24), 'Semibold Display'),
        (dict(wght=700, opsz=24), 'Bold Display'),

        (dict(wght=300, opsz=11), 'Light Text'),
        (dict(wght=350, opsz=11), 'Semilight Text'),
        (dict(wght=400, opsz=11), 'Regular Text'),
        (dict(wght=550, opsz=11), 'Semibold Text'),
        (dict(wght=700, opsz=11), 'Bold Text'),

        (dict(wght=300, opsz=5), 'Light Small'),
        (dict(wght=350, opsz=5), 'Semilight Small'),
        (dict(wght=400, opsz=5), 'Regular Small'),
        (dict(wght=550, opsz=5), 'Semibold Small'),
        (dict(wght=700, opsz=5), 'Bold Small'),

    ]

    assistantGlyphEditorSubscriberClass = SegoeUIItalicAssistant

    BUILD_UI_METHODS = [
        'buildOverlay',
        'buildFamilyOverview',
        'buildGroups',
        'buildSpacer',
        'buildAnchors',
        'buildItalicize',
        'buildInterpolate',
        'buildCurves',
        'buildContours',
        'buildComponents',
        'buildDimensions',
        'buildGuidelines',
        'buildBuilder',
    ]
    CLOSING_UI_METHODS = [
        'closeAnchors', # Notify parts that the main assistant window is about to close. Close the anchors window    
    ]  
if __name__ == '__main__':
    OpenWindow(SegoeUIItalicAssistantController)

