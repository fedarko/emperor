r"""
Emperor 3D PCoA viewer (:mod:`emperor`)
============================================

This module provides an objects and functions to interact and visualize a set
of coordinates using the Emperor interface user interface. The `Emperor` class,
and the functions present here are all intended to be compatible with the
Jupyter notebook.

.. currentmodule:: emperor

Classes
-------
.. autosummary::
    :toctree: generated/

    Emperor

Functions
---------
.. autosummary::
    :toctree: generated/

    nbinstall
    scatterplot
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2013--, emperor development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE.md, distributed with this software.
# ----------------------------------------------------------------------------
__version__ = "0.9.51-dev"  # noqa

from emperor.core import Emperor
from emperor._pandas import scatterplot
from emperor.util import nbinstall

__all__ = ['Emperor', 'scatterplot', 'biplots', 'format', 'filter', 'parse',
           'sort', 'util', 'nbinstall']
