import matplotlib.pyplot as plt
import geopandas as gpd

import fun_plots as py
import fun_imports.py

file_path="/Users/morganharrison/Downloads/ev228_data/"
historic_name= 'Historic_Fire_Perimeters.geojson'
out_p= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '1_extra_envstory.png'
gdf=gpd.read_file(file_path + historic_name)
print(gdf.columns)

