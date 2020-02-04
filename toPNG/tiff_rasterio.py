import rasterio
from rasterio.plot import show
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

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

raster = rasterio.open(modis_file)

red = raster.read(3)
green = raster.read(2)
blue = raster.read(1)

# Function to normalize the grid values
def normalize(array):
    """Normalizes numpy arrays into scale 0.0 - 1.0"""
    array_min, array_max = array.min(), array.max()
    return ((array - array_min)/(array_max - array_min))

# Normalize the bands
redn = normalize(red)
greenn = normalize(green)
bluen = normalize(blue)

print("Normalized bands")
print(redn.min(), '-', redn.max(), 'mean:', redn.mean())
print(greenn.min(), '-', greenn.max(), 'mean:', greenn.mean())
print(bluen.min(), '-', bluen.max(), 'mean:', bluen.mean())

# Create RGB natural color composite
rgb = np.dstack((redn, greenn, bluen))

# Let's see how our color composite looks like
plt.imshow(rgb)
plt.axis("off")
plt.savefig("test_image.png")

