
import gc
import ROOT
from typing import Union

__all__ = ['set_figure', 'get_figure', 'clear', 'suppress_root_warnings']

from . import figures
__all__.extend( figures.__all__ )
from .figures import *

global __figure
__figure = Figure()

def suppress_root_warnings():
    ROOT.gErrorIgnoreLevel=ROOT.kFatal

def set_figure(canvas: Union[ROOT.TCanvas, Figure]):
    """
    Sets current figure

    Parameters
    ----------
    canvas : Union[ROOT.TCanvas, Figure]
        rpl.Figure object to be the current figure.
        If a ROOT.TCanvas object is passed, creates a new figure
        containing it.
    """
    global __figure
    if type(canvas) is Figure:
        __figure = canvas
    else:
        __figure = Figure(canvas)

def get_figure() -> Figure:
    """
    Returns current figure

    Returns
    -------
    Figure
        Current Figure object
    """
    global __figure
    return __figure

def clear():
    """
    Clears current figure
    """
    get_figure().clear()

from . import axis
__all__.extend( axis.__all__ )
from .axis import *

from . import canvas
__all__.extend( canvas.__all__ )
from .canvas import *

from . import plots
__all__.extend( plots.__all__ )
from .plots import *

from . import hist1d
__all__.extend( hist1d.__all__ )
from .hist1d import *

from . import hist2d
__all__.extend( hist2d.__all__ )
from .hist2d import *

from . import legends
__all__.extend( legends.__all__ )
from .legends import *

from . import styles
__all__.extend( styles.__all__ )
from .styles import *

from . import colors
__all__.extend( colors.__all__ )
from .colors import *