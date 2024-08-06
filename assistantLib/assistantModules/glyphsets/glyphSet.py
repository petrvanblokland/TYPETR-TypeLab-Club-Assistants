# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Copyright (c) 2023+ TYPETR
#     Usage by MIT License
# ..............................................................................
#
#   glyphSet.py
#
from copy import deepcopy
import codecs
import os

if __name__ == '__main__': # Used for doc tests to find assistantLib
    import os, sys
    PATH = '/'.join(__file__.split('/')[:-4]) # Relative path to this respository that holds AssistantLib
    if not PATH in sys.path:
        sys.path.append(PATH)

from assistantLib.assistantModules.glyphsets.glyphData import *
from assistantLib.assistantModules.glyphsets.anchorData import AD 
from assistantLib.assistantModules.glyphsets.Latin_S_set import LATIN_S_SET, LATIN_S_SET_NAME
from assistantLib.assistantModules.glyphsets.Latin_M_set import LATIN_M_SET, LATIN_M_SET_NAME
from assistantLib.assistantModules.glyphsets.Latin_L_set import LATIN_L_SET, LATIN_L_SET_NAME
from assistantLib.assistantModules.glyphsets.Latin_XL_set import LATIN_XL_SET, LATIN_XL_SET_NAME
from assistantLib.assistantModules.glyphsets.TYPETR_full_set import TYPETR_FULL_SET, TYPETR_FULL_SET_NAME
from assistantLib.assistantModules.glyphsets.TYPETR_UpgradeNeon_set import TYPETR_UPGRADENEON_SET, TYPETR_UPGRADENEON_SET_NAME
from assistantLib.assistantModules.glyphsets.MS_WGL4_Segoe_set import MS_WGL4_SEGOE_SET, MS_WGL4_SEGOE_SET_NAME

GLYPH_DATA_SETS = { # Allow them to be retrieved by name
    LATIN_S_SET_NAME: LATIN_S_SET,
    LATIN_M_SET_NAME: LATIN_M_SET,
    LATIN_L_SET_NAME: LATIN_L_SET,
    LATIN_XL_SET_NAME: LATIN_XL_SET,
    TYPETR_FULL_SET_NAME: TYPETR_FULL_SET,
    TYPETR_UPGRADENEON_SET_NAME: TYPETR_UPGRADENEON_SET,
    MS_WGL4_SEGOE_SET_NAME: MS_WGL4_SEGOE_SET,
}

class GlyphSet:
    """GlyphSet behaves like a dictionary of GlyphData instances.
    GlyphData instances are records that keep information about each individual glyph, that cannot be stored
    (and easily altered manually) in the UFO glyph file. Technically, this information could be in the glyph.lib,
    but this way it's more visible together and it can be searched on for the whole font in an editor.

    The name of the glyphset needs to be defined in GLYPH_SETS, otherwise an error is raised.

    >>> from glyphData import *
    >>> from anchorData import AD
    >>> gs = GlyphSet()
    >>> gs
    <GlyphSet 354 glyphs>
    >>> gd = gs['A']
    >>> gd
    <GlyphData A l2r=A>
    >>> gd.anchors
    ['bottom', 'middle', 'ogonek', 'tonos', 'top']
    >>> gs['doestNotExist']
    >>> gd = gs['Aacute']
    >>> gd.c
    'Á'
    >>> gd.base
    'A'
    >>> gd.accents
    ['acutecomb']
    >>> gd.components
    ['A', 'acutecomb']
    >>> gd.comment
    'Á A WITH ACUTE, LATIN CAPITAL LETTER'

    >>> gs = GlyphSet(TYPETR_FULL_SET_NAME)
    >>> gs
    <GlyphSet 711 glyphs>

    >>> gs = GlyphSet(TYPETR_UPGRADENEON_SET_NAME)
    >>> gs
    <GlyphSet 948 glyphs>

    >>> gs = GlyphSet(MS_WGL4_SEGOE_SET_NAME) # Huge glyphset!
    >>> gs
    <GlyphSet 2548 glyphs>

    """

    def __init__(self, name=LATIN_S_SET_NAME, glyphDataSet=None):
        """If glyphData is omitted, then choose by name from the GLYPH_DATA_SETS. If name is omitted too, 
        then default the glyphDataSet to LATIN_S_SET"""
        if glyphDataSet is None:
            assert name in GLYPH_DATA_SETS, (f'### Unknown glyphset: {name}')
            glyphDataSet = GLYPH_DATA_SETS[name]
        self.glyphs = deepcopy(glyphDataSet) # Deep copy the data, in case it's altered by the instance.
        self.name = name

        self.unicode2GlyphName = {} # Key is unicode, value is glyph name
        self.anchor2GlyphNames = {} # Key is names of anchors. Value if a list of glyph names that implement the anchor.
        self.anchor2DiacriticNames = {} # Key is names of anchors, Value is a list of diacritics that support the anchor placement.
        self.diacritic2GlyphNames = {} # Key is name of a diacritic. Value is a list of glyph names that use the diacritic as component

        for gName, gd in sorted(self.glyphs.items()):
            if gd.uni:
                #assert gd.uni not in UNICODE2GLYPH, ("Unicode %04x already defined for /%s" % (gd.uni, gName))
                self.unicode2GlyphName[gd.uni] = gd.name
            # Make the dict of disacritics --> List of glyphs that use them
            for componentName in gd.components:
                gdc = self.glyphs.get(componentName)
                if gdc is not None and gdc.isDiacritic:
                    if not gdc.name in self.diacritic2GlyphNames:
                        self.diacritic2GlyphNames[gdc.name] = []
                    self.diacritic2GlyphNames[gdc.name].append(gd.name)

            gdBase = None
            if gd.base is not None: # If there is a base defined, take the x-ref base reference.
                gdBase = gd.base
                gd.composites.add(gName)

            if gd.anchors is not None:
                for anchorName in gd.anchors:
                    if not anchorName in self.anchor2GlyphNames:
                        self.anchor2GlyphNames[anchorName] = []
                    self.anchor2GlyphNames[anchorName].append(gName)
                    if not anchorName in self.anchor2DiacriticNames:
                        self.anchor2DiacriticNames[anchorName] = []
                    self.anchor2DiacriticNames[anchorName].append(gName)

    def __repr__(self):
        return(f'<{self.__class__.__name__} {len(self.glyphs)} glyphs>')

    def __getitem__(self, gName):
        return self.glyphs.get(gName, None)

    def getAnchorGlyphNames(self, anchorName):
        """Answer the list of glyphs that have this anchor

        >>> from glyphData import *
        >>> from anchorData import AD
        >>> glyphs = {}

        """
        return self.anchor2GlyphNames.get(anchorName)

    def getAnchorDiacriticNames(self, anchorName):
        """Answer the list of diacritic glyph names that have this anchor"""
        return self.anchor2DiacriticNames.get(anchorName)

    def checkFixFromFont(self, f):
        """Check the validity of unicode, components, achors, etc."""
        for gName in sorted(f.keys()):
            g = f[gName]
            if not g.name in self.glyphs:
                print(f'### Missing glyph /{g.name}')
                self.glyphs[g.name] = GlyphData(name=g.name)
            gs = self.glyphs[g.name]
            for cIndex, component in enumerate(g.components):
                if cIndex == 0:
                    if gs.base != component.baseGlyph:
                        print(f'### /{g.name} has wrong base glyph /{component.baseGlyph} in component {cIndex}, should be /{gs.base}?')

                elif not component.baseGlyph in gs.accents:
                    print(f'### /{g.name} has wrong accent glyph /{component.baseGlyph} in component {cIndex}, should one of /{gs.accents}?')
            anchors = []
            if g.name in TOP_ANCHORS:
                anchors.append(AD.TOP_)                   
            if g.name in MIDDLE_ANCHORS:
                anchors.append(AD.MIDDLE_)                   
            if g.name in BOTTOM_ANCHORS:
                anchors.append(AD.BOTTOM_)                   
            if g.name in OGONEK_ANCHORS:
                anchors.append(AD.OGONEK_)                   
            if g.name in DOT_ANCHORS:
                anchors.append(AD.DOT_)                   
            if g.name in TONOS_ANCHORS:
                anchors.append(AD.TONOS_)                   
            if g.name in VERT_ANCHORS:
                anchors.append(AD.VERT_)                   
        
            if g.name in _TOP_ANCHORS:
                anchors.append(AD._TOP)                   
            if g.name in _MIDDLE_ANCHORS:
                anchors.append(AD._MIDDLE)                   
            if g.name in _BOTTOM_ANCHORS:
                anchors.append(AD._BOTTOM)                   
            if g.name in _OGONEK_ANCHORS:
                anchors.append(AD._OGONEK)                   
            if g.name in _DOT_ANCHORS:
                anchors.append(AD._DOT)                   
            if g.name in _TONOS_ANCHORS:
                anchors.append(AD._TONOS)                   
            if g.name in _VERT_ANCHORS:
                anchors.append(AD._VERT)                   
        
            gs.anchors = anchors

    def get(self, gName, default=None):
        return self.glyphs.get(gName, default) 

    def keys(self):
        return self.glyphs.keys()

    def fromFont(self, f):
        """If a new project starts, and there is no standard glyph set available, this method
        creates the glyphData records based on the contents of @f"""
        for gName in sorted(f.keys()):
            g = f[gName]
            base = None
            accents = []
            if g.components:
                base = g.components[0].baseGlyph
                if len(g.components) > 1:
                    for component in g.components[1:]:
                        accents.append(component.baseGlyph)
            anchors = []
            for a in g.anchors:
                anchors.append(a.name)
            self.glyphs[gName] = GlyphData(name=gName, uni=g.unicode, base=base, accents=accents,
                anchors=anchors,
            )
        
    def saveGlyphSetSource(self, filePath=None):
        """Write Python code source for the current self.GLYPH_DATA table."""
        if filePath is None:
            fileName = f'Exported_{self.__class__.__name__}.py'
            dirPath = '/'.join(__file__.split('/')[:-1]) + '/_export/' # Get the directory path that this script is in.
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
            filePath = dirPath + fileName

        print(f'... Exported glyphs {filePath}')
        out = codecs.open(filePath, 'w', encoding='utf8')
        out.write("""# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Copyright (c) 2023+ TYPETR
#     Usage by MIT License
# ..............................................................................
#
#     Auto-generated by TYPETR Assistant GlyphSet.saveGlyphSetSource
#     
#
try:
    from assistantLib.assistantModules.glyphsets.glyphData import *
except ModuleNotFoundError:
    from glyphData import *

MY_GLYPH_SET_NAME = 'MyGlyphSet'

MY_GLYPH_SET = {
""" % (self.__class__.__name__, filePath))
        initial = None
        for gName, gd in sorted(self.glyphs.items()):
            if initial != gName[0]:
                initial = gName[0]
                out.write(f'\n        #   {initial}\n')
            out.write(gd.asSourceLine())
        out.write('}\n')
        out.close()


if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])


