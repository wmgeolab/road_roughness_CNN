import numpy as np
import rasterio as rio
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
from pycrs.parse import from_epsg_code
import json
import utm
# lat long to UTM

class Cropper:
    def __init__(self, filePath):
        self.filepath = filePath

    def crop(self, lat, long, outPath):
        dimX = 224
        dimY = 224

        x, y, zN, zL = utm.from_latlon(lat, long)
        with rio.open(self.filepath, "r") as raster:
            minx, miny = x - dimX/2, y - dimY/2
            maxx, maxy = x + dimX/2, y + dimY/2
            square = box(minx, miny, maxx, maxy)
            #gdf = gpd.GeoDataFrame({'geometry': square}, index = [0], crs=from_epsg(4326))
            gdf = gpd.GeoDataFrame({'geometry': square}, index = [0], crs=raster.crs.data)
            print(raster.crs.data)
            #gdf = gdf.to_crs(crs = raster.crs.data)
            #print("no crash")
            coords = self.__getFeatures(gdf)
            
            out_img, out_transform = mask(raster, coords, crop = True)
            out_meta = raster.meta.copy()
            epsg_code = int(raster.crs.data['init'][5:])
            print(epsg_code)
            out_meta.update({"driver": "GTiff", "height": out_img.shape[1], "width": out_img.shape[2], "transform": out_transform, "crs": from_epsg_code(epsg_code).to_proj4()})
            with rio.open(outPath, "w", **out_meta) as dest:
                dest.write(out_img)
            
    def __getFeatures(self, gdf):
        return [json.loads(gdf.to_json())['features'][0]['geometry']]
    
### Small test case ###
#if __name__ == "__main__":
#      crop = Cropper(r"CNN_roads_satImages/20190710_152929_101f_3B_AnalyticMS.tif")
#      crop.crop(37.27369, -76.75234, r"Jason/testCrop/test1.tif")