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

## FEMA disaster data
From [FEMA](https://www.fema.gov/media-library/assets/documents/106308), [Summary of Disaster Declarations and Grants](https://www.fema.gov/media-library-data/1493738442601-01db152481b5d3d747535ae0a1c441a6/DataVizDisasterSummariesFV12.19.2016.xlsx) (Produces file `DataVizDisasterSummariesFV12.19.2016.xlsx`)  
See the Federal declared disasters that have occurred in your state or territory. Then view a summary of our support for fire, preparedness, mitigation, individual assistance, and public assistance grants.

## Extreme weather events
[NOAA Website](https://www.climate.gov/maps-data/dataset/severe-storms-and-extreme-events-data-table); 
[Downloads page](https://www.ncdc.noaa.gov/stormevents/ftp.jsp);
[Column meanings](https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/Storm-Data-Export-Format.pdf);
[Data sets](https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/)

We used data for 2018, files:

`StormEvents_details-ftp_v1.0_d2018_c20190422.csv`

`StormEvents_fatalities-ftp_v1.0_d2018_c20190422.csv`

`StormEvents_locations-ftp_v1.0_d2018_c20190422.csv`

## County shapes, names, and codes
[From this ESRI forum post](https://community.esri.com/thread/24614)


The TIGER/Line shapefiles and related database files (.dbf) are an extract of selected geographic and cartographic information from the U.S. Census Bureau's Master Address File / Topologically Integrated Geographic Encoding and Referencing (MAF/TIGER) Database (MTDB). The MTDB represents a seamless national file with no overlaps or gaps between parts, however, each TIGER/Line shapefile is designed to stand alone as an independent data set, or they can be combined to cover the entire nation.

The primary legal divisions of most states are termed counties.  In Louisiana, these divisions are known as parishes.  In Alaska, which has no counties, the equivalent entities are the organized boroughs, city and boroughs, municipalities, and for the unorganized area, census areas.  The latter are delineated cooperatively for statistical purposes by the State of Alaska and the Census Bureau.  In four states (Maryland, Missouri, Nevada, and Virginia), there are one or more incorporated places that are independent of any county organization and thus constitute primary divisions of their states.  These incorporated places are known as independent cities and are treated as equivalent entities for purposes of data presentation.  The District of Columbia and Guam have no primary divisions, and each area is considered an equivalent entity for purposes of data presentation.  The Census Bureau treats the following entities as equivalents of counties for purposes of data presentation: Municipios in Puerto Rico, Districts and Islands in American Samoa, Municipalities in the Commonwealth of the Northern Mariana Islands, and Islands in the U.S. Virgin Islands.  The entire area of the United States, Puerto Rico, and the Island Areas is covered by counties or equivalent entities.

This shape file was transformed into a geoJSON file using [Mapshaper](https://mapshaper.org/).

This replaces an earlier map that we tried, which had much higher resolution and therefore was much, much heavier. 

