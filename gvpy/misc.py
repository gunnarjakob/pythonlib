#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Module gvpy.misc with miscellaneous functions

'''

from __future__ import print_function, division
import scipy.io as spio
import numpy as np



def near(A, target):
    '''
    Find index of value in A closest to target
    '''
    # A must be sorted
    idx = A.searchsorted(target)
    idx = np.clip(idx, 1, len(A)-1)
    left = A[idx-1]
    right = A[idx]
    idx -= target - left < right - target
    return idx


def getshape(d):
    '''
    Get dict with info on dict d
    '''
    if isinstance(d, dict):
        return {k: np.shape(d[k]) for k in d}
    else:
        # Replace all non-dict values with None.
        return None


def cmap_div(numcolors=11, name='custom_div_cmap',
             mincol='blue', midcol='white', maxcol='red'):
    """ Create a custom diverging colormap with three colors

    Default is blue to white to red with 11 colors.  Colors can be specified
    in any way understandable by matplotlib.colors.ColorConverter.to_rgb()
    Adapted from http://pyhogs.github.io/colormap-examples.html
    """

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(name=name,
                                             colors=[mincol, midcol, maxcol],
                                             N=numcwolors)
    return cmap


def jupaexit():
    '''
    jupaexit()
    Exit attached console without killing kernel
    '''
    exit(keep_kernel=True)
