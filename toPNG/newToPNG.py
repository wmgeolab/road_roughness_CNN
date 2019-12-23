#!/usr/bin/env python3
#
# VERSION 0.1
# LAST EDIT: 2019-11-04
#
# Use this script to read a tif spatial data file,
# convert the tif dataset to a png
#
# This script crawls in whatever directory you are
# running the script from and find what you are looking for
# and performs the conversion
#
#@Author Yaw Ofori-Addae

from PIL import Image
import os
import numpy
Image.MAX_IMAGE_PIXELS = None

"""
This works but I suggest incorporating a way where you could
directly pass in the directory as input so it looks just at that directory
cos sometimes it may end up converting files you don't want to.
Got a bit lazy here and didn't do that cos I was looking to quick results instead

"""
for root, dirs, file in os.walk("."):
    for filename in file:
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            imageExtract = os.path.join(root, filename)
            outfile = os.path.splitext(os.path.join(root, filename))[0] + ".png"
            im = Image.open(imageExtract)
            im.thumbnail(im.size)
            out = im.convert("RGB")
            out.save(outfile, "PNG", quality=100)
