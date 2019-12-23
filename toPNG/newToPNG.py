from PIL import Image
import os
import numpy
Image.MAX_IMAGE_PIXELS = None

try:
    work_dir = os.environ['DS_WORKSPACE']
except:
    work_dir = os.path.expanduser("~")
    print(work_dir)

for root, dirs, file in os.walk("."):
    for filename in file:
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            imageExtract = os.path.join(root, filename)
            outfile = os.path.splitext(os.path.join(root, filename))[0] + ".png"
            im = Image.open(imageExtract)
            im.thumbnail(im.size)
            out = im.convert("RGB")
            out.save(outfile, "PNG", quality=100)
