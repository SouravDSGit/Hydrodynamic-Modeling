# Chapter 2: Dataset

Welcome to the second chapter of our documentation! This chapter provides a comprehensive guide for input data formatting for the CULVERT Application.

Before starting the analysis, please make sure that your input dataset is in the accepted format:

## Geospatial Dataset

1. **Boundary Shapefile**

   - **Accepted format:**
     - Upload a ZIP file containing boundary polygon files: `.shp`, `.shx`, `.dbf`, and `.prj`.
     - Ensure the total ZIP file size does not exceed 25 MB.
     - The boundary must be located within the USA.
     - The maximum area allowed for the boundary is 120,000 hectares.
   - **Sample Data Download:** [here](https://github.com/SouravDSGit/CULVERT-Web-App/raw/refs/heads/main/instance/core_data/data_format_guide/santee_boundary_f.zip)

2. **LiDAR DEM Data**

   - **Accepted format:**
     - Upload a valid DEM raster file in `.tif` format with elevation values in `m`.
     - The DEM should cover an area larger than the boundary shapefile to ensure proper watershed delineation.
     - Make sure the DEM resolution is suitable for your analysis.
     - If the DEM leaves out any part of the boundary, an error will be displayed.
   - **Sample Data Download Link:** [here](https://example.com)

3. **Pour Point (Culvert) Data**

   a. **No Data Available**

   - **Accepted format:** `N/A`
   - **Sample Data Download Link:** `N/A`

   b. **Both Culvert and Gauging Station Point Data Available**

   - **Accepted format:**

     - Upload a ZIP file containing pour point files: `.shp`, `.shx`, `.dbf`, and `.prj`.
     - Points located outside the region boundary will be excluded from the analysis.
     - At least one pour point must be within the boundary, or watershed delineation will throw an error.
     - A maximum of 300 pour points can be included in the analysis at a time.
     - The point shapefile must have these headers (Note- You can have more columns like you may find in the sample dataset which was modified from the [CATT's dataset](https://research.fs.usda.gov/srs/centers/catt), but the data and columns described in the table below are mandetory) :

     | **Column Name** | **Description**                                                                                                                                                                                                                                 |
     | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `Point_ID`      | Unique `Integer` Identifier for each pour point.                                                                                                                                                                                                |
     | `Point_Name`    | Unique Name (`alpha-numeric`) Identifier for each pour point, e.g., culvert name and Gauging station name.                                                                                                                                      |
     | `Longitude`     | geographical X-coordinate in degrees.                                                                                                                                                                                                           |
     | `Latitude`      | geographical Y-coordinate in degrees.                                                                                                                                                                                                           |
     | `Pour_Sha`      | Present shape of the culverts and/or gauging stations. Currently only supports Culverts of `Pour_Sha` = `Circular`, `Box`, `Pipe arch`, and `Bridge`. Note: `Bridge`, if mentioned will be excluded form the hydrologic vulnerability analysis. |
     | `Width_ft`      | Width of the culvert in feet untis. Must be set to `NA` for gauging stations.                                                                                                                                                                   |
     | `Height_ft`     | Height of the culvert in feet untis. Must be same as the 'Width_ft' for Circular culverts. Must be set to `NA` for gauging stations.                                                                                                            |
     | `Flag_Gst`      | Must be set to `1` if the pour point is a gauging station, and must be set to `0` if its not a gauging station.                                                                                                                                 |
     | `Grp_ID`        | Identifier (`alpha-numeric`) for culverts belonging to the same group (pair, triple, or larger group). Rows indicating single drainage structure, bridge, or gauging station must be set to `NA`.                                               |
     | `Grp_Size`      | The size (`integer`) of the group (2 for paired, 3 for tripple, or a greater number for larger groups). Rows indicating single drainage structure, bridge, or gauging station must be set to `NA`.                                              |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) for the guaged watershed drained by the gauging station. Must be set to `NA` if its not a gauging station.                                                                                                  |

   - **Sample Data Download:** [here](https://github.com/SouravDSGit/CULVERT-Web-App/raw/refs/heads/main/instance/core_data/data_format_guide/culvert_guaging_st.zip)

   c. **Only Culvert Point Data Available**

   - **Accepted format:**

     - Upload a ZIP file containing pour point files: `.shp`, `.shx`, `.dbf`, and `.prj`.
     - Points located outside the region boundary will be excluded from the analysis.
     - At least one pour point must be within the boundary, or watershed delineation will throw an error.
     - A maximum of 300 pour points can be included in the analysis at a time.
     - The point shapefile must have these headers (Note- You can have more columns like you may find in the sample dataset which was modified from the [CATT's dataset](https://research.fs.usda.gov/srs/centers/catt), but the data and columns described in the table below are mandetory) :

     | **Column Name** | **Description**                                                                                                                                                                                                                                 |
     | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `Point_ID`      | Unique `Integer` Identifier for each pour point.                                                                                                                                                                                                |
     | `Point_Name`    | Unique Name (`alpha-numeric`) Identifier for each pour point, e.g., culvert name in this case.                                                                                                                                                  |
     | `Longitude`     | geographical X-coordinate in degrees.                                                                                                                                                                                                           |
     | `Latitude`      | geographical Y-coordinate in degrees.                                                                                                                                                                                                           |
     | `Pour_Sha`      | Present shape of the culverts and/or gauging stations. Currently only supports Culverts of `Pour_Sha` = `Circular`, `Box`, `Pipe arch`, and `Bridge`. Note: `Bridge`, if mentioned will be excluded form the hydrologic vulnerability analysis. |
     | `Width_ft`      | Width of the culvert in feet untis.                                                                                                                                                                                                             |
     | `Height_ft`     | Height of the culvert in feet untis, must be same as 'Width_ft' for Circular culverts.                                                                                                                                                          |
     | `Flag_Gst`      | Must be set to `NA` becuase it is not applicable in this case.                                                                                                                                                                                  |
     | `Grp_ID`        | Identifier (`alpha-numeric`) for culverts belonging to the same group (pair, triple, or larger group). Rows indicating single drainage structure, bridge, or gauging station must be set to `NA`.                                               |
     | `Grp_Size`      | The size (`integer`) of the group (2 for paired, 3 for tripple, or a greater number for larger groups). Rows indicating single drainage structure, bridge, or gauging station must be set to `NA`.                                              |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) for the guaged watershed drained by the gauging station. Must be set to `NA` if its not a gauging station.                                                                                                  |

   - **Sample Data Download:** [here](https://github.com/SouravDSGit/CULVERT-Web-App/raw/refs/heads/main/instance/core_data/data_format_guide/culvert_guaging_st.zip)

   d. **Only Gauging Station Point Data Available**

   - **Accepted format:**

     - Upload a ZIP file containing pour point files: `.shp`, `.shx`, `.dbf`, and `.prj`.
     - Gauging stations should be located inside the region boundary.
     - Gauging stations outside the region boundary will be excluded from the analysis.
     - A maximum of 300 gauging station points can be included in the analysis at a time.
     - The point shapefile must have these headers (Note- You can have more columns like you may find in the sample dataset which was modified from the [CATT's dataset](https://research.fs.usda.gov/srs/centers/catt), but the data and columns described in the table below are mandetory) :

     | **Column Name** | **Description**                                                                              |
     | --------------- | -------------------------------------------------------------------------------------------- |
     | `Point_ID`      | Unique `Integer` Identifier for each Gauging station.                                        |
     | `Point_Name`    | Unique Name (`alpha-numeric`) Identifier for each Gauging station.                           |
     | `Longitude`     | geographical X-coordinate in degrees.                                                        |
     | `Latitude`      | geographical Y-coordinate in degrees.                                                        |
     | `Pour_Sha`      | Must be set to `NA` because it is not applicable in this case.                               |
     | `Width_ft`      | Must be set to `NA` because it is not applicable in this case.                               |
     | `Height_ft`     | Must be set to `NA` because it is not applicable in this case.                               |
     | `Flag_Gst`      | Must be set to `1`.                                                                          |
     | `Grp_ID`        | Must be set to `NA` because it is not applicable in this case.                               |
     | `Grp_Size`      | Must be set to `NA` because it is not applicable in this case.                               |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) for the guaged watershed drained by the gauging station. |

   - **Sample Data Download:** [here](https://github.com/SouravDSGit/CULVERT-Web-App/raw/refs/heads/main/instance/core_data/data_format_guide/culvert_guaging_st.zip)

## Hydro-meteorological Time-series Data

1. **Instantaneous Streamflow Data**

   a. **No Data Available**

   - **Accepted format:** `N/A`
   - **Sample Data Download Link:** `N/A`

   b. **Only AMS of Instantaneous Streamflow Data Available (AMS: Annual Maxima Series)**

   - **Accepted format:**

     - Upload a valid `.csv` file for each and every gauging station declared in the pour point shapefile with these mandetory headers :

     | **Column Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                |
     | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) for the guaged watershed drained by the gauging station. Must be exactly the same ID as declared under the header `GWS_ID` in the Pour Point shapefile for the gauging station.                                                                                                                                                            |
     | `Point_Name`    | Unique identifier (`alpha-numeric`) for the gauging station draining the WS. Must be exactly the same ID as declared under the header `Point_Name` in the Pour Point shapefile for the gauging station.                                                                                                                                                                        |
     | `Year`          | Year of peak flow. Must be at least `15 years` with valid peak flow data. Missing data rows, if present, must be set to `NA`.                                                                                                                                                                                                                                                  |
     | `Month`         | Month when peak flow occurred. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                      |
     | `Day`           | Day when peak flow occurred. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                        |
     | `Flow`          | Peak flow in `m3/s` for each year. Must have valid peak flow data length of at least `15 years`. Missing data rows, if present, must be set to `NA.`                                                                                                                                                                                                                           |
     | `Covar`         | (Optional) data for chosen covariate to perform non-stationary frequency analysis. Missing data rows, if present, must be set to `NA`. Note: Users can perform non-stationary analysis even without this data-column. The covariate in that case will be set to time. But if present, then peak flows with missing `Covar`, will be excluded from the non-stationary analysis. |
     | `Area_km2`      | Drainage Area (in `square km`) of the guaged WS drainied by the gauging station.                                                                                                                                                                                                                                                                                               |

   - **Sample Data Download Link:** [here](https://example.com)

   c. **Full Series of Instantaneous Streamflow Data Available**

   - **Accepted format:**

     - Upload a valid `.csv` file for each and every gauging station declared in the pour point shapefile with these mandetory headers :

     | **Column Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                |
     | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) for the guaged watershed drained by the gauging station. Must be exactly the same ID as declared under the header `GWS_ID` in the Pour Point shapefile for the gauging station.                                                                                                                                                            |
     | `Point_Name`    | Unique identifier (`alpha-numeric`) for the gauging station draining the WS. Must be exactly the same ID as declared under the header `Point_Name` in the Pour Point shapefile for the gauging station.                                                                                                                                                                        |
     | `Year`          | Year values. Must be at least `15 years` with valid inst. streamflow data. Missing data rows, if present, must be set to `NA`.                                                                                                                                                                                                                                                 |
     | `Month`         | Month when inst. streamflow data recorded. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                          |
     | `Day`           | Day when peak flow occurred. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                        |
     | `Flow`          | inst. streamflow records in `m3/s`. Must have valid data length of at least `15 years`. Missing data rows, if present, must be set to `NA.`                                                                                                                                                                                                                                    |
     | `Covar`         | (Optional) data for chosen covariate to perform non-stationary frequency analysis. Missing data rows, if present, must be set to `NA`. Note: Users can perform non-stationary analysis even without this data-column. The covariate in that case will be set to time. But if present, then peak flows with missing `Covar`, will be excluded from the non-stationary analysis. |
     | `Area_km2`      | Drainage Area (in `square km`) of the guaged WS drainied by the gauging station.                                                                                                                                                                                                                                                                                               |

   - **Sample Data Download Link:** [here](https://example.com)

2. **Precipitation Intensity (PI) Data**

   a. **If No Data Available**

   - **Accepted format:** `N/A`
   - **Sample Data Download Link:** `N/A`

   b. **If only Annual Maxima of PI Data Available**

   - **Accepted format:**

     - Upload a valid `.csv` file for each and every gauging station declared in the pour point shapefile with these mandetory headers :

     | **Column Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                       |
     | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) of the gauged watershed associated to the rain gauge for the analysis. Must be exactly the same ID as declared under the header `GWS_ID` in the Pour Point shapefile. Note: Data from one rain gauge can be used for multiple WSs in data scarcity/limited conditions.                                                                            |
     | `Rg_ID`         | Unique identifier (`alpha-numeric`) of the rain gauge.                                                                                                                                                                                                                                                                                                                                |
     | `Year`          | Year of maximum PI. Must be at least `15 years` with valid data. Missing data rows, if present, must be set to `NA`.                                                                                                                                                                                                                                                                  |
     | `Month`         | Month when maximum PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                        |
     | `Day`           | Day when maximum PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                          |
     | `Hr`            | Day when maximum PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                          |
     | `Min`           | Day when maximum PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                          |
     | `PI`            | Maximum PI in `cm/hr` for each year. Must have valid data length of at least `15 years`. Missing data rows, if present, must be set to `NA.`                                                                                                                                                                                                                                          |
     | `Covar`         | (Optional) data for chosen covariate to perform non-stationary frequency analysis. Missing data rows, if present, must be set to `NA`. Note: Users can perform non-stationary analysis even without this data-column. The covariate in that case will be set to time. But if present, then anual maximum PIs with missing `Covar`, will be excluded from the non-stationary analysis. |

   - **Sample Data Download Link:** [here](https://example.com)

   c. **If full Series of hourly or sub-hourly PI Data Available** (Note: Culvert APP currently only supports hourly or sub-hourly PI data which is relevant for hydrologic analysis for small head-water catchments)

   - **Accepted format:**

     - Upload a valid `.csv` file for each and every gauging station declared in the pour point shapefile with these mandetory headers :

     | **Column Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                       |
     | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `GWS_ID`        | Unique identifier (`alpha-numeric`) of the gauged watershed associated to the rain gauge for the analysis. Must be exactly the same ID as declared under the header `GWS_ID` in the Pour Point shapefile. Note: Data from one rain gauge can be used for multiple WSs in data scarcity/limited conditions.                                                                            |
     | `Rg_ID`         | Unique identifier (`alpha-numeric`) of the rain gauge.                                                                                                                                                                                                                                                                                                                                |
     | `Year`          | Year values. Must be at least `15 years` with valid data. Missing data rows, if present, must be set to `NA`.                                                                                                                                                                                                                                                                         |
     | `Month`         | Month when PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                                |
     | `Day`           | Day when PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                                  |
     | `Hr`            | Day when maximum PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                          |
     | `Min`           | Day when maximum PI was observed. Must be set to `NA` for missing data rows.                                                                                                                                                                                                                                                                                                          |
     | `PI`            | PI values in `cm/hr`. Must have a valid data length of at least `15 years`. Missing data rows, if present, must be set to `NA.`                                                                                                                                                                                                                                                       |
     | `Covar`         | (Optional) data for chosen covariate to perform non-stationary frequency analysis. Missing data rows, if present, must be set to `NA`. Note: Users can perform non-stationary analysis even without this data-column. The covariate in that case will be set to time. But if present, then anual maximum PIs with missing `Covar`, will be excluded from the non-stationary analysis. |

   - **Sample Data Download Link:** [here](https://example.com)
