"""
===============
Custom contours
===============

These two examples highlight displaying (and not displaying) contour lines 
using 'ContourSet'.
"""

import matplotlib.pyplot as plt
from matplotlib.contour import ContourSet
import matplotlib.cm as cm

# Contour lines for each level are a list/tuple of polygons.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Note two lines.

# Filled contours between two levels are also a list/tuple of polygons.
# Points can be ordered clockwise or anticlockwise.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Note two polygons.
            [[1, 4], [3, 4], [3, 3]]]

"""
User-specifications
-------------------

The example illustrates how to to:
* fill a contour
* outline a contour
* display filled and outlined contours in a colorbar.
"""

plt.figure()

# Filled contours using filled=True.
cs = ContourSet(plt.gca(), [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)

# create the colorbar according to filled contours.
cbar = plt.colorbar(cs)

# Contour lines (non-filled).
lines = ContourSet(plt.gca(), [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool,
                   linewidths=3)

# Add contour lines are in the colorbar
cbar.add_lines(lines)

plt.axis([-0.5, 3.5, -0.5, 4.5])
plt.title('User-specified contours')

"""
Filling contours with holes
---------------------------

Multiple filled contour lines can be specified in a single list of polygon
vertices `filled01` along with a list of vertex kinds `kinds01` as described
in the `Path` class. This is particularly useful for polygons with holes.
"""

plt.figure()

filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
kinds01 = [[1, 2, 2, 2, 1, 2, 2, 2]]

cs = ContourSet(plt.gca(), [0, 1], [filled01], [kinds01], filled=True)
cbar = plt.colorbar(cs)

plt.axis([-0.5, 3.5, -0.5, 3.5])
plt.title('User specified filled contours with holes')

plt.show()

