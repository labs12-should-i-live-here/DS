# LiveSafe - Potential data sources

## Earthquake risk 1
US Geological Survey Earthquake Hazards Program, 2014 Long-term Model

Website: https://earthquake.usgs.gov/hazards/hazmaps/conterminous/index.php#2014

PDF rendering: https://earthquake.usgs.gov/static/lfs/nshm/conterminous/2014/2014pga2pct.pdf


### Dataset links: 
 [Map Data - PGA 2% in 50 yrs(3.9MB Zip)](https://earthquake.usgs.gov/static/lfs/nshm/conterminous/2014/data/2014_pga2pct50yrs.dat.zip) (single file `2014_pga2pct50yrs.dat`)
 
[GIS Shapefiles - PGA, 2% in 50yrs(5MB Zip)](https://earthquake.usgs.gov/static/lfs/nshm/conterminous/2014/data/USpga250.zip) (Folder `USpga250`, contains variety of filetypes in three sets)

This data describes the annual frequency of exceeding a set of ground motions, and represents an assessment of the best available science in earthquake hazards and incorporate new findings on earthquake ground shaking, faults, seismicity, and geodesy.  The USGS uses many definitons of earthquake risk.  The data that we chose to use in our app corresponds to the maximum peak ground acceleration (PGA) that an earquake has a 10% probability of causing over 50 years (PGA units are fraction of standard gravity).


## Earthquake risk 2
Similar to previous data, but older.  Main advantage is that it's available as a GeoJSON file, `stanford-rm034qp5477-geojson.json`

Website: https://geo.nyu.edu/catalog/stanford-rm034qp5477



This polygon shapefile represents seismic hazards in the United States. The data represent a model showing the probability that ground motion will reach a certain level. This map layer shows peak horizontal ground acceleration (the fastest measured change in speed, for a particle at ground level that is moving horizontally due to an earthquake) with a 10% probability of exceedance in 50 years. Values are given in %g, where g is acceleration due to gravity, or 9.8 meters/second^2. The lines of equal hazard, which are the lines between the polygons, were determined by interpolating from a grid of equally spaced points in latitude and longitude. Each point was weighted based on the seismic hazard at that location. 



## Storm Surge Hazards

Data: https://www.nhc.noaa.gov/nationalsurge/
Explanations: https://www.nhc.noaa.gov/gis/inundation/potential_storm_surge_flooding_downloads_guide.pdf

[Download – Texas to Maine (high tide scenario)](https://www.nhc.noaa.gov/gis/hazardmaps/US_SLOSH_MOM_Inundation.zip) (produces folder `US_SLOSH_MOM_Inundation_v2`, with GeoTIFF files for 5 different hurricane categories; seven files per category).

Storm surge hazard maps are available for Texas to Maine, Puerto Rico, USVI, Hawaii, and Hispaniola. The data are available in GeoTIFF (http://trac.osgeo.org/geotiff/) format for use in Geographic Information Systems (GIS) software. Comprehensive metadata are provided with each GIS file describing the data and its limitations. Storm surge inundation datasets are created using the high tide scenario SLOSH MOM products for all regions. Each dataset contains an ESRI World File (.tfw) and metadata .xml file. These GeoTIFFs are 8-bit unsigned integer raster datasets that correspond to 1 ft inundation bins (e.g., Class Value 1 corresponds to the 0-1 ft inundation bin, Class Value 2 corresponds to the 1-2 ft inundation bin, and so on). The maximum Class Value is 21, and inundation in excess of 20 ft is assigned a Class Value of 21. A Class Value of 99 is assigned to leveed areas. A more detailed description of the data can be found in the associated metadata.

## Wildfire Hazard
Data: https://www.fs.usda.gov/rds/archive/Product/RDS-2015-0046-2

Official name: Wildfire Hazard Potential (WHP) for the conterminous United States (270-m GRID), version 2018 classified (2nd Edition)

[Dataset](https://www.fs.usda.gov/rds/fedora/objects/RDS:RDS-2015-0046-2/datastreams/RDS-2015-0046-2/content) (produces folder `RDS-2015-0046-2`)

According to the metadata, this dataset contains:

ESRI grid, digital raster file (and associated files) containing wildfire hazard potential (WHP) in classes: 1) very low, 2) low, 3) moderate, 4) high, and 5) very high. In addition, non-burnable lands (6) and open water (7) are represented as separate classes.

## Historical flood data
From [FEMA](https://www.fema.gov/media-library/assets/documents/106308), [Historical Flood Risks and Costs](https://www.fema.gov/media-library-data/1493738649162-2ad83da9ad0395a0e31045c269333c55/DataVizFloodsFV3.22.2017.xlsx) (Produces file `DataVizFloodsFV3.22.2017.xlsx`)  