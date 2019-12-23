#!/usr/bin/env python3
#
# VERSION 0.1
# LAST EDIT: 2019-11-04
#
# Use this script to read a tif spatial data file,
# convert the tif dataset to a png
#
# This script assumes that your tif file is located
# in a directory defined by an environment variable "DS_WORKSPACE"
# or else is in your home directory
#
#@Author Yaw Ofori-Addae
###############################################################################
# IMPORT MODULES
###############################################################################
import glob
import os
import os.path

import gdal


###############################################################################
# MAIN
###############################################################################
# Set up directories and file names:
try:
    work_dir = os.environ['DS_WORKSPACE']
except:
    work_dir = os.path.expanduser("~")

file_paths = glob.glob(os.path.join(work_dir, "*.tif"))
modis_path = ""
modis_file = ""
if len(file_paths) > 0:
    modis_path = file_paths[0]
    modis_file = os.path.basename(modis_path)
else:
    raise IOError("No file found!")

# Open ncs file
nc_data = gdal.Open(modis_path, gdal.GA_ReadOnly)


# Create an PNG output
out_file = os.path.splitext(modis_file)[0] + '_png'
out_path = os.path.join(work_dir, out_file)
gdal.GetDriverByName("PNG").CreateCopy(out_path, nc_data, 0)

# Add GeoTIFF to your map in QGIS, if you ended up running all this code bit by bit in QGIS
#iface.addRasterLayer(out_path, out_file)
