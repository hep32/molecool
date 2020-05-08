"""
molecool
A Python package for analyzing and visualizing pdb and xyz files. For MolSSI May Webinar series.
"""

# Add imports here
from .functions import *
#from .functions import canvas
#can call individual functions - best practice

#import molecool.functions
#a way to call it in a different way -- molecool.functions.canvas()

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
