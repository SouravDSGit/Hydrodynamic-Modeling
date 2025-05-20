# Chapter 3: Data Requirements for Floodplain Models

```{contents}
:depth: 2
:local:
```

Floodplain models, like LISFLOOD-FP discussed in {ref}`Chapter 5: LISFLOOD-FP <chapter_05>`, rely on accurate data to predict how water flows during floods. This chapter explains the key data needed for these models, where to find it, and how to prepare it. Written for students, it uses simple language, practical examples, and visuals to make the concepts easy to understand. By the end, you’ll know how to gather and process data for a floodplain modeling project and avoid common pitfalls.

## Why Data Matters

Floodplain models simulate water movement based on the landscape, water inputs, and surface conditions. Without good data, models can produce inaccurate results, leading to poor flood predictions. This chapter covers the main data types—Digital Elevation Models (DEMs), boundary conditions, Manning’s roughness, channel geometry, and initial conditions—and explains how to prepare them for tools like LISFLOOD-FP or MIKE 21 (see {ref}`Chapter 6: Two-Dimensional (2D) Hydrodynamic Models <chapter_06>`).

```{mermaid}
graph LR
    A[Floodplain Model] --> B[Data Inputs]
    B --> C[Digital Elevation Model&#40;DEM&#41;]
    B --> D[Boundary Conditions]
    B --> E[Manning's Roughness]
    B --> F[Channel Geometry]
    B --> G[Initial Conditions]
    C --> H[Accurate Flood Predictions]
    D --> H
    E --> H
    F --> H
    G --> H
```

## Key Data Types

Below are the five main data types needed for floodplain modeling, explained in simple terms.

### Digital Elevation Model (DEM)

- **What It Is**: A DEM is a digital map showing the height (elevation) of the land at each point, usually in a grid format.
- **Why It Matters**: The terrain’s shape determines where water flows. Small errors in elevation can lead to big mistakes in flood predictions.
- **Sources**:
  - **LiDAR**: High-resolution (1–10m) data from laser scans, ideal for small areas.
  - **SRTM**: Global 30m data from NASA, good for large regions.
  - **Copernicus**: Free 25m DEMs from the European Space Agency.
- **How to Prepare**:
  - Use GIS tools like QGIS or ArcGIS to clip the DEM to your study area.
  - Check for errors (e.g., missing data, negative elevations) and fill gaps using interpolation.
  - Convert to a format like ASCII grid for models like LISFLOOD-FP.
- **Example**: For a 10 km² catchment, a 10m LiDAR DEM provides detailed elevation data for accurate flood mapping.

### Boundary Conditions

- **What It Is**: Data on water entering or leaving the model area, such as river flow (hydrograph) or water levels at the edges.
- **Why It Matters**: Tells the model how much water is coming in, driving the flood simulation.
- **Sources**:
  - **Gauging Stations**: Real river flow data from local authorities.
  - **Hydrological Models**: Simulated hydrographs from models like HEC-HMS.
  - **Design Storms**: Synthetic data for events like a 100-year flood.
- **How to Prepare**:
  - Format as a text file with time (seconds) and discharge (m³/s), e.g.:
    ```
    0 0.0
    3600 50.0
    7200 100.0
    10800 50.0
    ```
  - Ensure the time step matches the model’s requirements (e.g., hourly).
- **Example**: A hydrograph for a 100-year flood might peak at 100 m³/s after 2 hours.

### Manning’s Roughness

- **What It Is**: A number that measures how much a surface (e.g., grass, pavement) slows down water flow. Lower values mean smoother surfaces.
- **Why It Matters**: Affects how fast water moves and spreads. Incorrect values can skew flood extent and depth.
- **Sources**:
  - **Literature**: Standard values (e.g., 0.03 for pavement, 0.05 for forests, 0.1 for dense vegetation).
  - **Land Cover Maps**: Use GIS data to assign roughness based on surface type.
- **How to Prepare**:
  - Create a raster map matching the DEM’s grid, with roughness values for each cell.
  - Alternatively, use a single value for simple models.
  - Validate values during calibration (see {ref}`Chapter 8: Calibration and Validation of Flood Models <chapter_08>`).
- **Example**: A grassland floodplain might use a Manning’s value of 0.035.

| Surface Type     | Manning’s Roughness |
| ---------------- | ------------------- |
| Pavement         | 0.02–0.03           |
| Grassland        | 0.03–0.04           |
| Forest           | 0.05–0.1            |
| Dense Vegetation | 0.1–0.15            |

### Channel Geometry

- **What It Is**: Data on the shape of rivers or channels, including width, depth, and bank elevations.
- **Why It Matters**: Critical for models like LISFLOOD-FP when rivers are narrower than the grid size (see {ref}`Chapter 5 <chapter_05>`).
- **Sources**:
  - **Field Surveys**: Measure river cross-sections directly.
  - **Remote Sensing**: Estimate from satellite or aerial imagery.
  - **Topographic Maps**: Approximate from existing data.
- **How to Prepare**:
  - Create a text or raster file with width and depth for each river segment.
  - For LISFLOOD-FP, use a subgrid channel file (e.g., `channel.asc`).
- **Example**: A small river might have a width of 10m and depth of 2m.

### Initial Conditions

- **What It Is**: The starting water depth or flow in the model area before the simulation begins.
- **Why It Matters**: Sets the baseline for the flood event. Often zero for dry floodplains.
- **Sources**:
  - **Field Data**: Water levels from gauges at the start of the event.
  - **Assumptions**: Use zero depth for dry areas or small values for wet conditions.
- **How to Prepare**:
  - Specify as a raster (matching the DEM) or a single value.
  - For LISFLOOD-FP, include in the `.par` file or a separate file.
- **Example**: A dry floodplain starts with a depth of 0m across all cells.

## Data Preparation Workflow

Preparing data correctly is crucial for accurate modeling. Here’s a step-by-step guide for a small project (e.g., a 10 km² catchment).

1. **Collect Data**:

   - Download a DEM (e.g., 10m LiDAR from Copernicus).
   - Obtain a hydrograph from a gauging station or hydrological model.
   - Use land cover maps to assign Manning’s roughness.
   - Measure or estimate river channel geometry.
   - Set initial conditions (e.g., zero depth for a dry start).

2. **Process in GIS**:

   - Use QGIS or ArcGIS to:
     - Clip the DEM to your study area.
     - Create a roughness raster based on land cover.
     - Check for DEM errors (e.g., gaps, outliers) and fix them.
   - Convert data to compatible formats (e.g., ASCII for LISFLOOD-FP).

3. **Format for the Model**:

   - Save the DEM as `dem.asc`.
   - Create a boundary condition file (e.g., `inflow.bdy`) with time and discharge.
   - Save roughness as `manning.asc` or a single value in the `.par` file.
   - Define channel geometry in a file like `channel.asc`.

4. **Validate Data**:
   - Check DEM resolution (e.g., 10m is good for small areas).
   - Ensure hydrograph time steps align with the model’s time scale.
   - Verify roughness values match land cover types.

```{mermaid}
graph TD
    A[Start] --> B[Collect DEM, Hydrograph, Roughness]
    B --> C[Process in QGIS/ArcGIS]
    C --> D[Clip DEM, Create Rasters]
    D --> E[Format for Model: ASCII, Text Files]
    E --> F[Validate Data Quality]
    F --> G[Run Model &#40;e.g., LISFLOOD-FP&#41;]
```

## Common Data Challenges

Students often face these issues when preparing data:

- **Low-Quality DEMs**: Coarse resolution (e.g., 90m SRTM) misses small features. Solution: Use LiDAR or interpolate to improve resolution.
- **Missing Data**: Gaps in DEMs or hydrographs. Solution: Fill gaps with interpolation or use synthetic data (e.g., design storms).
- **Incorrect Roughness**: Wrong Manning’s values lead to inaccurate flow. Solution: Use literature values and calibrate (see {ref}`Chapter 8 <chapter_08>`).
- **Data Format Errors**: Models may reject incompatible files. Solution: Check the model’s user manual (e.g., LISFLOOD-FP requires ASCII grids).

| Challenge           | Solution                        |
| ------------------- | ------------------------------- |
| Low-Quality DEM     | Use LiDAR or interpolate data   |
| Missing Data        | Fill gaps or use synthetic data |
| Incorrect Roughness | Use standard values, calibrate  |
| Format Errors       | Check model manual for formats  |

## Tools for Data Preparation

- **QGIS**: Free GIS software for clipping DEMs, creating roughness maps, and visualizing data.
- **ArcGIS**: Professional GIS tool for advanced data processing.
- **Python**:
  - Use libraries like `rasterio` to process DEMs:
    ```python
    import rasterio
    with rasterio.open('dem.tif') as src:
        dem = src.read(1)
        # Process DEM (e.g., fill gaps)
    ```
  - Use `pandas` for hydrograph data:
    ```python
    import pandas as pd
    hydrograph = pd.DataFrame({'time': [0, 3600, 7200], 'discharge': [0.0, 50.0, 100.0]})
    hydrograph.to_csv('inflow.bdy', index=False, sep=' ')
    ```
- **Global Datasets**:
  - Copernicus DEM: Free 25m resolution data.
  - OpenStreetMap: Land cover for roughness estimates.
  - USGS EarthExplorer: Access to SRTM and other DEMs.

## Tips for Success

1. **Choose the Right Resolution**: Use 5–10m DEMs for small catchments, 30m for larger areas.
2. **Validate Data**: Cross-check DEMs with field surveys or satellite imagery.
3. **Start Simple**: Use a single roughness value for initial tests, then refine with a raster.
4. **Automate with Python**: Scripts save time for repetitive tasks like formatting hydrographs.
5. **Document Sources**: Keep track of where data comes from for reproducibility.

## Further Resources

- **QGIS Tutorials**: Free online guides for GIS data processing.
- **Copernicus Data Hub**: Access DEMs and land cover data.
- **USGS EarthExplorer**: Source for global DEMs like SRTM.
- **Research Papers**: Studies on data quality in flood modeling (e.g., Narmada River case in {ref}`Chapter 11: Case Studies in Floodplain Modeling <chapter_11>`).
- **LISFLOOD-FP Manual**: Details on data formats for LISFLOOD-FP (see {ref}`Chapter 5 <chapter_05>`).

This chapter has shown you how to gather and prepare data for floodplain modeling. With high-quality DEMs, boundary conditions, and roughness data, you can build accurate models. Practice with a small project, and refer to {ref}`Chapter 8 <chapter_08>` for calibration tips to refine your results.
