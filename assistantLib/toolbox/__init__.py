# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Copyright (c) 2023+ TYPETR
#     Usage by MIT License
# ..............................................................................
#
#    TYPETR assistantLib/toolbox
#
#
import os

def path2Dir(path):
	"""Answer the director that this path is in.

	>>> path2Dir('/dir1/dir2/aFile')
	'/dir1/dir2/'
	>>> path2Dir('dir1/dir2/aFile')
	'dir1/dir2/'
	>>> path2Dir(__file__).endswith('/TYPETR-TypeLab-Club-Assistants/assistantLib/toolbox/')
	True
	"""
	return '/'.join(path.split('/')[:-1]) + '/'

def path2UfoPaths(path):
    """Answer a list of all UFO files in the path directory.

	>>> path2UfoPaths(path2Dir(__file__))
	[]
	>>> tryUfoPaths = path2UfoPaths(path2Dir(__file__) + '../../ufo-try/')	
	>>> tryUfoPaths[0].endswith('Upgrade_Try-UltraBlack_Italic.ufo')
	True
    """
    ufoPaths = []
    for fileName in os.listdir(path):
        if fileName.startswith('.'):
            continue
        if fileName.endswith('.ufo'):
            ufoPaths.append(path + fileName)
    return ufoPaths

def path2FileName(path):
	"""Answer the file name (or current directory nane) of path:

	>>> path2FileName('/dir1/dir2/myFont.ufo')
	'myFont.ufo'
	"""
	return path.split('/')[-1]

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

