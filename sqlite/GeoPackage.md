# Creating GeoPackages and layer tables in GeoPandas

## Mapscaping Article - Reading And Writing Geopackage In Python

Excellent article on using GeoPackage database in Python

APRIL 11, 2023 DANIEL ODONOHUE


- [Mapscaping.com: Reading And Writing Geopackage In Python](https://mapscaping.com/reading-and-writing-geopackage-in-python/)

## answer from Perplexity.ai

how can I create a geopackage from a geopandas geodataframe?

```
Answer
To create a GeoPackage from a GeoPandas GeoDataFrame in Python, you can use the to_file() method with the driver parameter set to 'GPKG'. Here's a simple example:
python
import geopandas as gpd

# Assuming 'gdf' is your GeoDataFrame
output_file = "path/to/output/geopackage.gpkg"
gdf.to_file(output_file, driver='GPKG')

This will save your GeoDataFrame gdf to a GeoPackage file at the specified output_file path
1
.
If you want to specify a layer name within the GeoPackage, you can also include the layer parameter:
python
gdf.to_file(output_file, layer='my_layer', driver='GPKG')

Remember that GeoPackage does not support all data types. For example, if your GeoDataFrame contains columns with numpy arrays, you will need to convert these to a supported format (like strings) before saving to a GeoPackage
5

```

### Sources

- [PyPi.org: geopackage-python 2.2.0.2](https://pypi.org/project/geopackage-python/)
- [pypi: fudgeo project](https://pypi.org/project/fudgeo/)  
  fudgeo removes the fear uncertainty doubt from using GeoPackages with Python. fudgeo is a lightweight package for creating OGC GeoPackages, Feature Classes, and Tables. Easily read and write geometries and attributes to Feature Classes and Tables using regular Python objects and SQLite syntax.

## GeoPackage layer support explanation on StackOverflow

[Multi-Layer .gdb files in Python?](https://stackoverflow.com/questions/54562069/multi-layer-gdb-files-in-python/54563846#54563846)

```
Yes, GeoPandas support layers. As names of your layers are terribly long, I recommend using the order of layers.

mallard_0 = gpd.read_file('./bird-species/E00039600_mallard.gdb/', layer=0)
mallard_1 = gpd.read_file('./bird-species/E00039600_mallard.gdb/', layer=1)

# geopandas included map, filtered to just this hemisphere
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
westhem = world[(world['continent'] == 'North America') |
                (world['continent'] == 'South America')]

# making sure the coordinates line up:
mallard_0 = mallard_0.to_crs(world.crs)
mallard_1 = mallard_1.to_crs(world.crs)

# establishing figure axes
base = westhem.plot(color='white', edgecolor='black', figsize=(11, 11))

# cmap because I'd LIKE the multiple layers to exist
mallard_0.plot(ax=base, color='red', alpha=.5)
mallard_1.plot(ax=base, color='blue', alpha=.5)
If you have more of them you can then make a loop to go plot them all at once easily. result of the script above

Edit: Geopandas is using Fiona under the hood for file handling, so if you want to see the list of your layers use

import fiona
fiona.listlayers('./bird-species/E00039600_mallard.gdb')
Edit2: Loop over all layers will then look like this:

import fiona

# geopandas included map, filtered to just this hemisphere
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
westhem = world[(world['continent'] == 'North America') |
                (world['continent'] == 'South America')]
base = westhem.plot(color='white', edgecolor='black', figsize=(11, 11))

layers = fiona.listlayers('./bird-species/E00039600_mallard.gdb')

for l in layers:
    mallard = gpd.read_file('./bird-species/E00039600_mallard.gdb', layer=l)
    mallard = mallard.to_crs(world.crs)
    mallard.plot(ax=base, color='red', alpha=.1)
second example using loop

Share
Improve this answer
Follow
edited Feb 6, 2019 at 23:06

```
