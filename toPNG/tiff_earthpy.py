import glob
import os
import os.path

import matplotlib.pyplot as plt
import rasterio as rio
import geopandas as gpd

import earthpy.plot as ep
from earthpy.spatial import bytescale


###############################################################################
# MAIN
###############################################################################
# Set up directories and file names:
try:
    work_dir = os.environ['DS_WORKSPACE']
except:
    work_dir = os.path.expanduser("~")

#variable storing list of all file ending in .tif in alphabetical order
file_paths = glob.glob(os.path.join(work_dir, "*.tif"))
modis_path = ""
modis_file = ""
if len(file_paths) > 0:
    modis_path = file_paths[0]
    modis_file = os.path.basename(modis_path)
else:
    raise IOError("No file found!")

with rio.open(modis_file) as src:
    tif_file = src.read()
    tif_file_meta = src.meta

# print("shape:",tif_file.shape)
# print("meta:",tif_file_meta)
# print("min:",tif_file.min())
# print("max:", tif_file.max())

"""may need to find a way to change 16 bit image to 8 bit image
"""

#Plot red band by telling imshow which band to plot
# fig, ax = plt.subplots()
# ax.imshow(tif_file[0], cmap="Greys_r")
# ax.set_title("SAT Image RGB Imagery Band 1 Red")
# plt.show()

#Plot red band using earthpy
# ep.plot_bands(tif_file[0],
#               title="Sat RGB Imagery - Band 1-Red",
#               cbar=False)
# plt.show()

#Plot green band using earthpy
# ep.plot_bands(tif_file[1],
#               title="Sat RGB Imagery - Band 2 - Green",
#               cbar=False)
# plt.show()

#Plot blue band using earthpy
# ep.plot_bands(tif_file[2],
#               title="Sat RGB Imagery - Band 3 - Blue",
#               cbar=False)
# plt.show()

# titles = ["Red Band", "Green Band", "Blue Band", "Near Infrared (NIR) Band"]

# Plot all bands using the earthpy function
# ep.plot_bands(tif_file, 
#               figsize=(12, 5), 
#               cols=2,
#               title=titles,
#               cbar=False)
# plt.show()

#Plot rgb bands combined into an image
# ep.plot_rgb(tif_file,
#            rgb=[0, 1, 2],
#            title="RGB Composite image - Sat")

#Plot rgb bands combined into an image, but apply stretch to increase contrast
ep.plot_rgb(bytescale(tif_file),
           rgb=[0, 1, 2],
           title="RGB Composite image - Sat")
plt.show()






