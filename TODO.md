# TYPETR-Assistants TODO

### Implemented modules

* overlay (show left/overlay/right glyphs in EditorWindow. Select alignment. [g] key to snap points to overlay background

### Implement existing modules in this new Assistant architecture

* anchors (automatic creation of anchors)
* components (checks on the compatible amount of components within the design space masters)
* contours (checks on the compatible amount of contours within the design space masters)
* curves (conversion between Bezier and Quadratics. Curvepalette for curvature selection)
* dimensions (show values of the GlyphAnalyzer in the EditorWindow)
* familyOverview (show top bar of current glyph for all design space masters)
* groups (group management, including Similarity support)
* guidelines (generate relevant glyph guidelines)
* interpolate (check interpolation compatibility for all design space masters)
* italicize (intelligent italicizing for different sources)
* spacer (spacing by rules, groups and Similarity. Implementing kerning editor inside the EditorWindow. AI for best kerning values)

### Implement functions from old separate sources:

* Dimensioneer002.py
* CurvePalette003.py
* Interpolator002.py
* GlyphBrowser005.py
* KerningAssistant001.py

## KerningAssistant

KerningAssistant needs PIL and torch
Install this way:

### PIL

pip install --target "/Users/petr/Library/Application Support/RoboFont/Python3.9" https://files.pythonhosted.org/packages/bd/43/b6e0f0c85fd4ab7e6dea2e2e5c531c5ff40ec7b3f9ad1607e08b8cdd5a45/Pillow-10.0.1-cp38-cp38-macosx_11_0_arm64.whl

= for the pillow version for your computer from here:
https://pypi.org/project/Pillow/#files


### torch

pip install --target "/Users/petr/Library/Application Support/RoboFont/Python3.9" torch
