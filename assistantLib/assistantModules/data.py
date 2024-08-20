# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Copyright (c) 2023+ TYPETR
#     Usage by MIT License
# ..............................................................................
#
#   data.py
#
#   Main recent data, used by build.py
#
#   Most common anchor names
#   Anchors with an initial underscore belong in diacritics.
#   In the diacritics cloud and in engines such as Harfbuzz, the anchors are matche with their counter parts
#   on glyph to get their position on top or below.
#   Stacking diacritics can have both, to allow other diacritics floating on top.
#
import importlib
import os, sys
import codecs

if __name__ == '__main__': # Used for doc tests to find assistantLib
    PATH = '/'.join(__file__.split('/')[:-3]) # Relative path to this respository that holds AssistantLib
    if not PATH in sys.path:
        sys.path.append(PATH)

from assistantLib.toolbox import path2UfoPaths, path2Dir
from assistantLib.assistantModules.glyphsets.glyphData import * 
from assistantLib.assistantModules.glyphsets.glyphSet import GlyphSet, LATIN_S_SET_NAME
import assistantLib.assistantModules.glyphsets.anchorData
importlib.reload(assistantLib.assistantModules.glyphsets.anchorData)
from assistantLib.assistantModules.glyphsets.anchorData import AD

class MasterData:
    """Storing additional data about masters, without storing the actual RFont instance. 
    The font can be retrieved by baseAssistant.getMaster(self.path)

    >>> # Doctesting is done via more global docTestAssistants.py
    >>> name = 'MyFont.ufo'
    >>> ufoPath = 'ufo/' + name
    >>> md = MasterData(name, ufoPath)
    >>> md.name, md.ufoPath
    ('MyFont.ufo', 'ufo/MyFont.ufo')
    >>> md.glyphSet['A']
    <GlyphData A l2r=A>
    >>> md.ascenderAnchorOffsetY
    -120
    """
    # Master data default values
    UNITS_PER_EM = 1000 # Default font.info.unitPerEm, if not defined otherwise
    COPYRIGHT = ""
    TRADEMARK = ""
    LOWEST_PPEM = 5

    BASELINE = 0
    TAB_WIDTH = 650
    BASE_OVERSHOOT = 12 # Default overshoot for /o, etc. and for all overshoot if not defined separately.
    STEM_OVERSHOOT = 0 # Used for small overshoot of single stems, e.g. in rounded terminals such as Upgrade Neon
    ASCENDER = 750 # Default ascender in font.info, if not defined otherwise.
    DESCENDER = -250 # Default descender in font.info, if not defined otherwise.
    XHEIGHT = 500
    CAPHEIGHT = 750
    DEFAULT_TAB_WIDTH = 650
    
    VERSION_MAJOR = 1 # Default version numnber. Should be altered as MasterData creation parameter.
    VERSION_MINOR = 0

    UFO_PATH = 'ufo/' # Default relative directory for UFO files in a project. Can be altered in the MasterData creation.

    def __init__(self, name, ufoPath, 
            srcUFOPath=None, someUFOPath=None, orgUFOPath=None, 
            groupSrcUFOPath=None, # Optioncal copy groups from here, otherwise use orgUFOPath
            kerningSrcUFOPath=None, # Optional copy kerning from here, otherwise use orgUFOPath
            romanItalicUFOPath=None, # Path of corresponding master for roman <--> italic
            spacingSrcUFOPath=None, # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
            spacingOffset=0, # Value to add to margins of self.spacingSrcUFOPath (if defined)
            italicAngle=0, italicSkew=None, italicRotation=None, isItalic=False,
            dsPosition=None,
            m0=None, # Origin of the design space
            m1=None, m2=None, # Used for interpolating spacing, outlines, anchor positions, component positions
            sm1=None, sm2=None, # Scalerpolate masters for condensed and extended making
            osm1=None, osm2=None, # Previous and next master on the same optical size level
            tripletData1=None, tripletData2=None, featurePath=None, 
            # GlyphSet instance, describing the glyph set and GlyphData characteristics. 
            # This attribute must be defined, or else the Latin_S_set (Small) will be used.
            glyphSet=None, 
            glyphSetName=None,
            # Vertical metrics
            baseline=0, stemOvershoot=STEM_OVERSHOOT, baseOvershoot=None, capOvershoot=None, scOvershoot=None, supsOvershoot=None,
            ascender=None, descender=None,
            xHeight=None, capHeight=None, scHeight=None, supsHeight=None,
            numrBaseline=None, supsBaseline=None, sinfBaseline=None, dnomBaseline=None, modBaseline=None,
            middlexHeight=None, middleCapHeight=None,
            # Vertical anchor offsets to avoid collission with baseline, guidlines, etc. in mouse selection
            baseDiacriticsTop=None, capDiacriticsTop=None, scDiacriticsTop=None, # Baseline of top diacritics
            baseDiacriticsBottom=None, # Top of bottom diacritis
            ascenderAnchorOffsetY= -AD.ANCHOR_ASCENDER_OFFSET,
            boxTopAnchorOffsetY= -AD.ANCHOR_BOXTOP_OFFSET,
            capHeightAnchorOffsetY= -AD.ANCHOR_CAP_OFFSET, # Optional vertical offset of cap-anhors or lower capital diacritics.
            xHeightAnchorOffsetY= -AD.ANCHOR_OFFSET,
            baselineAnchorOffsetY=AD.ANCHOR_OFFSET,
            ogonekAnchorOffsetY=AD.ANCHOR_OGONEK_OFFSET,
            boxBottomAnchorOffsetY= AD.ANCHOR_BOXBOTTOM_OFFSET,
            descenderAnchorOffsetY=AD.ANCHOR_DESCENDER_OFFSET,
            # Horizontal metrics
            diagonalTolerance=0, # ± Tolerance for italic diagonals to be marked as off-limit
            HStem=None, HThin=None, OStem=None, OThin=None,
            HscStem=None, HscThin=None, OscStem=None, OscThin=None,
            nStem=None, oStem=None, oThin=None, UThin=None, VThin=None, eThin=None,
            thickness=10, distance=16, # Used for Neon tubes, can be overwritten from GlyphData.thickness
            tabWidth=None,
            # Table stuff
            ttfPath=None, platformID=None, platEncID=None, langID=None, 
            unitsPerEm=UNITS_PER_EM, copyright=COPYRIGHT, uniqueID=None, trademark=TRADEMARK, 
            lowestRecPPEM=LOWEST_PPEM,
            familyName=None, styleName=None,
            fullName=None, version=None, versionMajor=VERSION_MAJOR, versionMinor=VERSION_MINOR,
            postscriptName=None, preferredFamily=None, preferredSubFamily=None,
            openTypeOS2WinAscent=None, openTypeOS2WinDescent=None,
            openTypeOS2Type=[2, 8], # fsType, TN standard
            vendorURL=None, manufacturerURL=None, manufacturer=None,
            designerURL=None, designer=None, 
            eulaURL=None, eulaDescription=None,
            underlinePosition=None, underlineThickness=None

        ):
        if name is None:
            name = 'Untitled'
        self.name = name
        self.ufoPath = ufoPath or self.UFO_PATH # Ufo file path = self.ufoPath + self.name
        self.familyName = familyName
        self.styleName = styleName

        # Angle, italic skew and rotation
        self.italicAngle = italicAngle or 0
        if italicSkew is None:
            italicSkew = italicAngle * 0.5 # Default, can be overwritten if needed.
        self.italicSkew = italicSkew # In case italicize is partical skew and rotation
        if italicRotation is None:
            italicRotation = italicAngle * 0.5
        self.italicRotation = italicRotation 
        self.isItalic = bool(italicAngle) or isItalic or 'Italic' in name

        # Used by Neon for tube thickness and minimal tube distance. Overwritten if GlyphData.thickness is not None
        self.thickness = thickness
        self.distance = distance
        
        # Referencing related masters by relative path, handled by the overlay assistant part
        self.srcUFOPath = srcUFOPath # "Original" master of this font, copy from here
        self.someUFOPath = someUFOPath # Show this outline on the background
        self.orgUFOPath = orgUFOPath # "Original" master of this font for overlay reference
        self.romanItalicUFOPath = romanItalicUFOPath # Roman <---> Italic master reference
        self.groupSrcUFOPath = groupSrcUFOPath or orgUFOPath # Used as groups reference to copy from
        self.kerningSrcUFOPath = kerningSrcUFOPath or orgUFOPath # Used as kerning reference.
        self.spacingSrcUFOPath = spacingSrcUFOPath # If defined, used as spacing reference, overwriting all spacing rules. Goes with spacingOffset
        self.spacingOffset = spacingOffset # Value to add to margins of self.spacingSrcUFOPath (if defined)

        # Interpolation & design space
        self.interpolationFactor = 0.5
        self.m0 = m0 # Regular origin
        self.m1 = m1 # Direct interpolation master in "min" side
        self.m2 = m2 # Direct interpolation master on "max" side
        self.sm1 = sm1 # Scalerpolate masters for condensed and extended making.
        self.sm2 = sm2
        self.osm1 = osm1 # If defined, lighter master on same optical size level
        self.osm2 = osm2 # If defined, bolder master on same optical size level
        
        # Design space position (matching .designspace) to calculate triplet kerning.
        # This can be different from HStem (with m1, m2) interpolation.
        self.dsPosition = dsPosition 
        self.tripletData1 = tripletData1
        self.tripletData2 = tripletData2, # Compatible triplet sets of (name1, name2, name3, kerning) tuples for interpolation.
        self.featurePath = featurePath
        
        if tabWidth is None:
            tabWidth = self.DEFAULT_TAB_WIDTH
        self.tabWidth = tabWidth

        # Glyphs
        if glyphSet is None:
            # Make a default GlyphSet instance, if not defined.
            glyphSet = GlyphSet()
        self.glyphSet = glyphSet
        
        # Vertical metrics. Do some guessing for missing values. 
        # This may not be matching the current font, as we don't have it available as open RFont here.

        if baseOvershoot is None: # Generic overshoot value, specifically for lower case
            baseOvershoot = self.BASE_OVERSHOOT
        self.baseOvershoot = baseOvershoot
        if stemOvershoot is None:
            stemOvershoot = self.STEM_OVERSHOOT
        self.stemOvershoot = stemOvershoot
        if capOvershoot is None: # Overshoot value for capitals
            capOvershoot = baseOvershoot
        self.capOvershoot = capOvershoot
        if scOvershoot is None: # Overshoot value for smallcaps, mod, etc.
            scOvershoot = baseOvershoot
        self.scOvershoot = scOvershoot
        if supsOvershoot is None: # Overshoot value for sups, numr, sinf and dnom
            supsOvershoot = int(round(baseOvershoot * 0.75)) # Default scale from base overshoot
        self.supsOvershoot = supsOvershoot
        
        self.cat2Overshoot = { # Category --> overshoot
            GD.CAT_OVERSHOOT: baseOvershoot,
            GD.CAT_CAP_OVERSHOOT: capOvershoot,
            GD.CAT_SUPS_OVERSHOOT: supsOvershoot,
            GD.CAT_SC_OVERSHOOT: scOvershoot,
        }

        # Vertical anchor offsets
        self.ascenderAnchorOffsetY = ascenderAnchorOffsetY
        self.boxTopAnchorOffsetY = boxTopAnchorOffsetY
        self.capHeightAnchorOffsetY = capHeightAnchorOffsetY # Optional vertical offset of cap-anhors or lower capital diacritics.
        self.xHeightAnchorOffsetY = xHeightAnchorOffsetY
        self.baselineAnchorOffsetY = baselineAnchorOffsetY
        self.ogonekAnchorOffsetY = ogonekAnchorOffsetY
        self.boxBottomAnchorOffsetY = boxBottomAnchorOffsetY
        self.descenderAnchorOffsetY = descenderAnchorOffsetY
        
        if unitsPerEm is None:
            unitsPerEm = self.UNITS_PER_EM
        self.unitsPerEm = unitsPerEm

        if ascender is None:
            ascender = self.ASCENDER
        self.ascender = ascender
        if descender is None:
            descender = self.DESCENDER
        self.descender = descender

        if xHeight is None:
            xHeight = self.XHEIGHT
        self.xHeight = xHeight
        if capHeight is None:
            capHeight = self.CAPHEIGHT
        self.capHeight = capHeight
        if scHeight is None:
            scHeight = xHeight
        self.scHeight = scHeight
        if supsHeight is None:
            supsHeight = xHeight * 2/3
        self.supsHeight = supsHeight

        if middlexHeight is None:
            middlexHeight = xHeight/2,
        self.middlexHeight = middlexHeight        
        if middleCapHeight is None:
            middleCapHeight = capHeight/2
        self.middleCapHeight = middleCapHeight

        self.cat2Height = { # Category --> height
            GD.CAT_XHEIGHT: xHeight,
            GD.CAT_CAP_HEIGHT: capHeight,
            GD.CAT_SC_HEIGHT: scHeight,
            GD.CAT_SUPS_HEIGHT: supsHeight, # Height of .sups, .sinf, .numr, .dnom and mod
        }

        if baseDiacriticsTop is None: # Baseline of top diacritics
            baseDiacriticsTop = int(round(xHeight * 1.2))
        self.baseDiacriticsTop = baseDiacriticsTop
        if capDiacriticsTop is None:
            capDiacriticsTop = int(round(capHeight * 1.1))
        self.capDiacriticsTop = capDiacriticsTop
        if baseDiacriticsBottom is None: # Top of bottom diacritis
            baseDiacriticsBottom = int(round(-4 * baseOvershoot))
        self.baseDiacriticsBottom = baseDiacriticsBottom

        if baseline is None:
            baseline = self.BASELINE
        self.baseline = baseline
        if modBaseline is None:
            modBaseline = xHeight
        self.modBaseline = modBaseline
        if supsBaseline is None:
            supsBaseline = xHeight
        self.supsBaseline = supsBaseline
        if numrBaseline is None: 
            numrBaseline = ascender - supsHeight  
        self.numrBaseline = numrBaseline
        if dnomBaseline is None: 
            dnomBaseline = baseline  
        self.dnomBaseline = dnomBaseline
        if sinfBaseline is None: 
            sinfBaseline = descender  
        self.sinfBaseline = sinfBaseline

        self.cat2Baseline = {
            GD.CAT_BASELINE: baseline,
            GD.CAT_MOD_BASELINE: modBaseline,
            GD.CAT_NUMR_BASELINE: numrBaseline,
            GD.CAT_SINF_BASELINE: sinfBaseline,
            GD.CAT_SUPS_BASELINE: supsBaseline,
            GD.CAT_DNOM_BASELINE: dnomBaseline ,
        }

        # Horizontal metrics
        self.diagonalTolerance = diagonalTolerance # ± Tolerance for italic diagonals to be marked as off-limit
        self.HStem = HStem # Used for m1->m2 interpolation
        self.HThin = HThin
        self.OStem = OStem
        self.OThin = OThin
        self.HscStem = HscStem
        self.HscThin = HscStem
        self.OscStem = OscStem
        self.OscThin = OscThin
        self.nStem = nStem
        self.oStem = oStem
        self.oThin = oThin
        self.UThin = UThin
        self.VThin = VThin
        self.eThin = eThin

        # Info
        self.ttfPath = ttfPath
        self.platformID = platformID
        self.platEncID = platEncID
        self.langID = platEncID, 
        self.unitsPerEm = unitsPerEm
        self.copyright = copyright
        self.uniqueID = uniqueID 
        self.trademark = trademark
        self.lowestRecPPEM = lowestRecPPEM

        self.fullName = fullName

        #version=None, versionMajor=VERSION_MAJOR, versionMinor=VERSION_MINOR,
        #postscriptName=None, preferredFamily=None, preferredSubFamily=None,
        #openTypeOS2WinAscent=OS2_WIN_ASCENT, openTypeOS2WinDescent=OS2_WIN_DESCENT,
        #openTypeOS2Type=[2, 8], # fsType, TN standard
        #vendorURL=VENDOR_URL, manufacturerURL=MANUFACTURER_URL, manufacturer=MANUFACTURER,
        #designerURL=DESIGNER_URL, designer=DESIGNER, 
        #eulaURL=EULA_URL, eulaDescription=EULA_DESCRIPTION,
        #underlinePosition=None, underlineThickness=UNDERLINE_THICKNESS

    @classmethod
    def fromUfoPath(cls, ufoPath):
        """Try to create all values from the existing UFO font"""
        from fontParts.fontshell.font import RFont
        from assistantLib.toolbox.glyphAnalyzer import GlyphAnalyzer

        name = ufoPath.split('/')[-1].replace('.ufo', '')
        assert os.path.exists(ufoPath) # Make sure the UFO exists

        # Not trying to match the glyphset of ufoPath with the ones that are defined.
        # It's up to the designer/developer of the masterData.py to decide which one it should be.
        glyphSetName = LATIN_S_SET_NAME

        f = RFont(ufoPath) # Open to UFO to harvest and guess parameters
        
        # We cannot use self.getOverhoot(glyphName) here, since we're in classMethod mode.
        # And it would be a circle reference, we need to extract the values from the real glyphs
        baseOvershoot = capOvershoot = scOvershoot = supsOvershoot = None
        if 'O' in f: # Use for guessing capital overshoots
            ga = GlyphAnalyzer(f['O'])
            capOvershoot = ga.overshoot
        if 'o' in f: # Use for guessing capital overshoots
            ga = GlyphAnalyzer(f['o'])
            baseOvershoot = ga.overshoot
        if 'O.sc' in f: # Use for guessing capital overshoots
            ga = GlyphAnalyzer(f['O.sc'])
            scOvershoot = ga.overshoot

        md = cls(name, ufoPath=ufoPath, 
            romanItalicUFOPath=cls.guessRomanItalicPath(ufoPath), # Guess the roman <--> italic compantion master
            # Glyphs
            glyphSetName=glyphSetName,
            # Angles
            italicAngle=f.info.italicAngle,
            # Vertical metrics
            ascender=f.info.ascender,
            descender=f.info.descender,
            xHeight=f.info.xHeight,
            capHeight=f.info.capHeight,
            baseOvershoot=baseOvershoot,
            capOvershoot=capOvershoot,
            scOvershoot=scOvershoot,
            # supsOvershoot

            # Info
            copyright=f.info.copyright or f'Copyright for {f.info.familyName}',
        ) 
        return md

    @classmethod
    def guessRomanItalicPath(cls, ufoPath):
        ufoDirPath = '/'.join(ufoPath.split('/')[:-1]) + '/'
        fileName = ufoPath.split('/')[-1]
        if 'Italic' in fileName:
            return ufoDirPath + fileName.replace('_Italic', '')
        return ufoDirPath + fileName.replace('.ufo', '_Italic.ufo')

    def __repr__(self):
        return f'<{self.__class__.__name__} name={self.name}>'

    def isNumber(self, v):
        return isinstance(v, (int, float))

    def getOvershoot(self, gName):
        """Answer the overshoot for this glyph based on the settings of the related GlyphData and otherwise guessing on its name."""
        gd = self.glyphSet.get(gName)
        if gd is None:
            print(f'### getOvershoot: Unknown glyph /{gName} in glyphSet of {self.name}')
            return self.baseOvershoot
        if gd.overshoot is None: # Nothing defined in the glyph, use the default
            return self.baseOvershoot
        if isinstance(gd.overshoot, (int, float)): 
            return gd.overshoot
        # If there is a category defined in the glyphData for this glyph, then answer the referenced category value.
        if gd.overshoot in self.cat2Overshoot:
            return self.cat2Overshoot[gd.overshoot]
        # Not defined in the GlyphSet/GlyphData for this glyph. We need to do some quessing, based on the name.
        if gd.isUpper: # All glyph that start with initial cap
            return self.cat2Overshoot[GD.CAT_CAP_OVERSHOOT]
        if gd.isMod: # One of sups, sinf, dnom, numr, mod in the name
            return self.cat2Overshoot[GD.CAT_SUPS_OVERSHOOT]
        if gd.isSc: # One of .sc, small in the name
            return self.cat2Overshoot[GD.CAT_SC_OVERSHOOT]
        # Otherwise answer the default overshoot. 
        return self.baseOvershoot

    def getBaseline(self, gName):
        """Answer the baseline position for this glyph based on the settings of the related GlyphData and otherwise guessing on its name."""
        gd = self.glyphSet.get(gName)
        if gd is None:
            print(f'### getBaseline: Unknown glyph /{gName} in glyphSet of {self.name}')
            return self.BASELINE
        if gd.baseline is None: # Nothing defined in the glyph, use the default
            return self.BASELINE
        if isinstance(gd.baseline, (int, float)): 
            return gd.baseline
        # If there is a category defined in the glyphData for this glyph, then answer the referenced category value.
        if gd.baseline in self.cat2Baseline:
            return self.cat2Baseline[gd.baseline]
        # Not defined in the GlyphSet/GlyphData for this glyph. We need to do some quessing, based on the type of glyph or its name.
        if gd.isMod:
            return self.modBaseline
        if gd.isSups:
            return self.supsBaseline
        if gd.isNumr:
            return self.numrBaseline
        if gd.isSinf:
            return self.sinfBaseline
        if gd.isDnom:
            return self.dnomBaseline
        return self.BASELINE

    def getHeight(self, gName):
        """Answer the height for this glyph based on the settings of the related GlyphData and otherwise guessing on its name."""
        gd = self.glyphSet.get(gName)
        if gd is None:
            print(f'### getHeight: Unknown glyph /{gName} in glyphSet of {self.name}')
            return self.capHeight
        if gd.height is None: # Nothing defined in the glyph, use the default
            if gd.isLower:
                return self.xHeight
            return self.capHeight
        if isinstance(gd.height, (int, float)): 
            return gd.height
        # If there is a category defined in the glyphData for this glyph, then answer the referenced category value.
        # Smallcaps
        if gd.isSc:
            return self.scHeight
        # Not defined in the GlyphSet/GlyphData for this glyph. We need to do some quessing, based on the type of glyph or its name.
        if gd.isMod or gd.isSups or gd.isNumr or gd.isSinf or gd.isDnom:
            return self.supsHeight
        if gd.isLower:
            return self.xHeight
        return self.capHeight

    def getHeight2(self, gName):
        """Answer the rounded half of height."""
        return int(round(self.getHeight(gName)/2))
    
    def getAnchorOvershoot(self, gName):
        """Answer the standard overshoot of anchors (to make sure theu don't overlap with outline points)"""
        return 16 # for now

    def _get_localUfoPath(self):
        """Answer the self.ufoPath as local ufo/MyFont.ufo path."""
        return '/'.join(self.ufoPath.split('/')[-2:])
    localUfoPath = property(_get_localUfoPath)

    def asSource(self):
        """Answer the source of this instance that 100% regenerates. This is used by the MasterDataManager
        to write the source for local masterData.py"""
        s = ['MD(']
        s.append(f"""name='{self.name}',""")
        s.append(f"""ufoPath='{self.localUfoPath}',""")
        if self.ttfPath is not None:
            s.append(f"""ttfPath='{self.ttfPath}',""")
        s.append('#\tAngles')
        s.append(f"""italicAngle={self.italicAngle},""")
        s.append('#\tVertical metrics')
        s.append(f"""ascender={self.ascender},""")
        s.append(f"""capHeight={self.capHeight},""")
        s.append(f"""xHeight={self.xHeight},""")
        s.append(f"""descender={self.descender},""")
        s.append(f"""baseOvershoot={self.baseOvershoot},""")
        s.append(f"""capOvershoot={self.capOvershoot},""")
        s.append(f"""scOvershoot={self.scOvershoot},""")
        s.append(f"""supsOvershoot={self.supsOvershoot},""")
        s.append('#\tInfo')
        if self.copyright is not None:
            s.append(f"""copyright='{self.copyright}',""")
        """
        self.platformID = platformID
        self.platEncID = platEncID
        self.langID = platEncID, 
        self.unitsPerEm = unitsPerEm
        self.copyright = copyright
        self.uniqueID = uniqueID 
        self.trademark = trademark
        self.lowestRecPPEM = lowestRecPPEM

        self.fullName = fullName
        """
        return '\n\t\t'.join(s) + '\n\t),\n\n'

MD = MasterData

class MasterDataManager:
    """The MasterDataManager handles the connection between the MasterData instances and the directory 
    that contains UFO files. It is assumed that a project has a local masterData.py file that describes 
    all master data that does not fit in font.info. If the file does not exist or if it is empty, 
    the MasterDataInstance tries to create it, with best guesses of values that it derives from the UFO files. 
    Note that this only happens if the file does not exist. Otherwise it just reads the dictionary.
    This way a new project can start from a bunch of existing UFO files, without the need to initialize 
    the masterData.py manually. After that, the designer will alter/add values manually.
    However, there is also a self.save(path) method available, in case the user project wants to save 
    a source for the current masterData. 

    >>> # Construct the absolute path where theh type-try UDOs are located.
    >>> ufoDirPath = '/'.join(__file__.split('/')[:-3]) + '/ufo-try/' 
    >>> masterData = {} # We start with uninitialized master data
    >>> mdm = MasterDataManager(masterData, ufoDirPath, glyphSet=None) # Examine the directory content
    >>> len(mdm.keys()) # It generated a MasterData instance for each of the demo UFO files.
    10

    >>> # ---------- Select the masterData from a specific UFO
    >>> ufoName = 'Upgrade_Try-Regular' # Let's use this one for testing
    >>> md = mdm[ufoName]
    >>> md
    <MasterData name=Upgrade_Try-Regular>
    >>> md.romanItalicUFOPath.split('/')[-1] # Italic companion of this italic
    'Upgrade_Try-Regular_Italic.ufo'
    >>> md.italicAngle, md.isItalic 
    (0, False)
    >>> md.ascender, md.capHeight, md.xHeight, md.descender
    (748, 658, 466, -252)
    >>> md.baseOvershoot, md.capOvershoot
    (11, 15)

    >>> # ---------- Select the masterData from the companion italic
    >>> mdi = mdm.findPath2MasterData(md.romanItalicUFOPath)
    >>> mdi
    <MasterData name=Upgrade_Try-Regular_Italic>
    >>> mdi.romanItalicUFOPath.split('/')[-1] # Roman companion of this italic
    'Upgrade_Try-Regular.ufo'
    >>> mdi.italicAngle, mdi.isItalic
    (-8, True)
    >>> mdi.ascender, mdi.capHeight, mdi.xHeight, mdi.descender
    (748, 658, 466, -252)
    >>> mdi.baseOvershoot, mdi.capOvershoot
    (11, 15)

    >>> # ---------- Let's test another roman with different proportions
    >>> ufoName = 'Upgrade_Try-UltraBlack' # Let's use this one for testing
    >>> mdb = mdm[ufoName]
    >>> mdb
    <MasterData name=Upgrade_Try-UltraBlack>
    >>> mdb.baseOvershoot, mdb.capOvershoot # UltraBlack had more overshoot than Regular
    (24, 18)

    >>> mdm.save()
    """
    def __init__(self, mastersData, ufoDirPath, glyphSet=None):
        # If masterData is None or empty, then try to create it by filling guessed data
        self.ufoDirPath = ufoDirPath # Absolute path reference to the ufo/ directory
        self.path = None # Will be initialized as parent of ufoPath
        self.ufoPath = None # Use the first UFO that we find as reference.
        if mastersData is None or len(mastersData) == 0:
            mastersData = {}
        self.mastersData = mastersData
        ufoPaths = path2UfoPaths(ufoDirPath)
        for ufoPath in ufoPaths:
            md = self.findPath2MasterData(ufoPath) # Find the masterData that fits this ufoPath, if it exists.
            if md is None: # If it does not exist, try to create a MasterData for this ufo
                md = MasterData.fromUfoPath(ufoPath)
                self.mastersData[md.name] = md

    def findPath2MasterData(self, ufoPath):
        for name, md in self.mastersData.items():
            if ufoPath == md.ufoPath:
                return md
        return None

    def keys(self):
        return self.mastersData.keys()

    def __getitem__(self, key):
        return self.mastersData[key]

    def __setitem__(self, key, md):
        assert isinstance(md, MasterData)
        self.mastersData[key] = md

    def save(self, fileName=None):
        """Save the Python source of the current dict of MasterData"""
        s = """# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Generated by TYPETR-Assistant MasterDataManager
# ..............................................................................
#
#   masterData.py
#
from assistantLib.assistantModules.data import MasterData as MD

MASTERS_DATA = {
"""
    
        for name, md in sorted(self.mastersData.items()):
            s += f"""\t'{name}': {md.asSource()}"""

        s += '}\n\n'

        if fileName is None:
            fileName = 'myMasterData000.py'
        path = path2Dir(self.ufoDirPath) + fileName
        f = codecs.open(path, 'w', encoding='utf-8') # Open file, for unicode/UTF-8
        f.write(s) 
        f.close()

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])




