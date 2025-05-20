# Chapter 5: LISFLOOD-FP

```{contents}
:depth: 2
:local:
```

Floods can devastate communities, infrastructure, and ecosystems. To predict and manage flood risks, tools like LISFLOOD-FP simulate how water flows across floodplains and urban areas. This chapter introduces LISFLOOD-FP, a widely used hydrodynamic model, and explains its core concepts, setup, and applications. Designed for students, it uses simple language, step-by-step guides, and visuals to help you understand and apply LISFLOOD-FP confidently. By the end, you’ll know how to use it for a small project and discuss it in technical settings.

## What is LISFLOOD-FP?

LISFLOOD-FP is a two-dimensional (2D) hydrodynamic model developed by the University of Bristol. It simulates water movement over landscapes like floodplains or cities during floods, producing maps of flood extent, depth, and velocity. For more on hydrodynamic modeling basics, see {ref}`Chapter 2: Fundamentals of Hydrodynamic Modeling <chapter_02>`.

### Purpose and Applications

LISFLOOD-FP is used to:

- Predict flood extent and depth for risk assessment.
- Plan urban development in flood-prone areas.
- Reconstruct historical floods to improve preparedness.
- Support real-time flood forecasting with weather data.

### Key Features

- **Grid-Based**: Divides the landscape into a grid for efficient modeling.
- **Multiple Solvers**: Offers methods to balance speed and accuracy.
- **Open-Source**: Free for non-commercial use, with active development.
- **Scalable**: Suitable for small catchments (e.g., 10 km²) to continents.
- **Version 8.1**: Includes GPU acceleration for faster simulations.

## Core Concepts

To use LISFLOOD-FP, you need to understand its key ideas, explained simply below.

### Hydrodynamic Modeling Basics

Hydrodynamic models simulate water flow using physics, based on:

1. **Mass Conservation**: Water volume is conserved as it moves.
2. **Momentum Conservation**: Water flows due to gravity, friction, and pressure.

LISFLOOD-FP simplifies the _shallow water equations_ (see {ref}`Chapter 2 <chapter_02>`) to make calculations faster, using different solvers to suit various flood scenarios.

### Raster-Based Approach

LISFLOOD-FP uses a grid, like a checkerboard, where each cell stores:

- **Elevation**: Land height from a Digital Elevation Model (DEM).
- **Water Depth**: Height of water in the cell.
- **Velocity**: Speed and direction of water flow.
- **Roughness**: Surface friction (e.g., grass slows water more than pavement).

Water flows between cells based on elevation and depth differences. This grid approach integrates well with GIS tools like QGIS, as discussed in {ref}`Chapter 3: Data Requirements for Floodplain Models <chapter_03>`.

```{mermaid}
graph TD
    A[Landscape] --> B[Divide into Grid]
    B --> C[Each Cell: Elevation, Depth, Velocity, Roughness]
    C --> D[Calculate Water Flow Between Cells]
    D --> E[Output: Flood Maps]
```

### Numerical Solvers

LISFLOOD-FP offers solvers to calculate water flow, each with trade-offs:

- **Diffusive Solver**: Fast, assumes slow flow driven by gravity. Best for steady floods.
- **Inertial Solver**: Includes momentum, balancing speed and accuracy. Ideal for most projects.
- **Adaptive Solver**: Adjusts calculations for stability in complex terrains.
- **Full 2D Solver (Roe)**: Highly accurate but slow, for dynamic floods.

| Solver        | Speed     | Accuracy | Best For                    |
| ------------- | --------- | -------- | --------------------------- |
| Diffusive     | Very Fast | Low      | Slow, steady floods         |
| Inertial      | Fast      | Medium   | General flood modeling      |
| Adaptive      | Medium    | Medium   | Complex terrains            |
| Full 2D (Roe) | Slow      | High     | Dynamic, fast-moving floods |

### Input Data Requirements

LISFLOOD-FP needs (see {ref}`Chapter 3 <chapter_03>` for details):

- **DEM**: A map of land heights (e.g., from LiDAR).
- **Boundary Conditions**: River flow data (e.g., hydrograph) or water levels.
- **Manning’s Roughness**: Friction values (e.g., 0.03 for pavement, 0.05 for forests).
- **Channel Geometry**: Width and depth for narrow rivers.
- **Initial Conditions**: Starting water depths (often zero for dry areas).

## How LISFLOOD-FP Works

LISFLOOD-FP takes input data, calculates water flow, and produces flood maps. Here’s the process in simple steps.

### Step-by-Step Workflow

1. **Prepare Input Data**: Collect DEM, hydrograph, and roughness data.
2. **Set Up the Model**: Create a configuration file (`.par`).
3. **Run the Simulation**: Calculate water flow across the grid.
4. **Analyze Outputs**: Generate maps of flood extent, depth, and velocity.
5. **Validate Results**: Compare with real data (see {ref}`Chapter 8: Calibration and Validation of Flood Models <chapter_08>`).

### Flow Diagram of the Process

```{mermaid}
    graph TD
        A[Start] --> B[Collect DEM, Hydrograph, Roughness]
        B --> C[Create Configuration File (.par)]
        C --> D[Choose Solver: Inertial, Diffusive, etc.]
        D --> E[Run LISFLOOD-FP]
        E --> F[Generate Outputs: Depth, Velocity Maps]
        F --> G[Visualize in QGIS or Python]
        G --> H[Validate with Real Data]
        H --> I[Adjust Parameters if Needed]
        I --> E
```

## Setting Up a Small Project

Let’s set up LISFLOOD-FP for a 10 km² rural catchment, a practical example for students.

### Installing LISFLOOD-FP

1. **Download**: Get LISFLOOD-FP 8.1 from the University of Bristol’s website or GitHub (openearth/lisflood-fp-bmi).
2. **Install**:
   - Use a compiler (e.g., GCC for Linux, Visual Studio for Windows).
   - For GPU acceleration, install CUDA for NVIDIA GPUs.
   - Optionally, use Python’s `lisflood-py` for easier setup.
3. **Test**: Run a sample project from the user manual.

### Preparing Input Data

For the catchment:

- **DEM**: Use a 10m resolution DEM from LiDAR or Copernicus, clipped in QGIS.
- **Boundary Conditions**: Format a hydrograph (e.g., 100-year flood) as a text file:
  ```
  0 0.0
  3600 50.0
  7200 100.0
  10800 50.0
  ```
  (Time in seconds, discharge in m³/s.)
- **Manning’s Roughness**: Use 0.035 for grasslands, 0.05 for forests, as a raster or single value.
- **Channel Geometry**: Define river width (e.g., 10m) and depth if narrower than the grid.
- **Configuration File**: Create a `.par` file:
  ```
  demfile dem.asc
  bdyfile inflow.bdy
  manningfile manning.asc
  solver inertial
  sim_time 86400
  output_interval 3600
  ```

### Running the Model

1. **Command Line**: Run `lisflood -f project.par`.
2. **Python Option**: Automate with:
   ```python
   from lisflood import LisfloodModel
   model = LisfloodModel('project.par')
   model.run()
   ```
3. **Check Outputs**: Look for files like `depth_0001.asc` (water depth).

### Visualizing Outputs

Use QGIS for flood maps or Python for custom visuals:

```python
import rasterio
import matplotlib.pyplot as plt
with rasterio.open('depth_0001.asc') as src:
    depth = src.read(1)
plt.imshow(depth, cmap='Blues')
plt.colorbar(label='Water Depth (m)')
plt.title('Flood Depth Map')
plt.show()
```

```{mermaid}
graph TD
    A[Output Files] --> B[Load in QGIS]
    A --> C[Use Python with Rasterio]
    B --> D[Flood Extent Map]
    C --> E[Depth and Velocity Plots]
```

## Advanced Features in LISFLOOD-FP 8.1

LISFLOOD-FP 8.1 introduces features for faster and more accurate simulations.

### GPU Acceleration

- **What It Is**: Uses graphics cards to speed up calculations.
- **Why It Matters**: Enables faster simulations for large or real-time projects.
- **How to Use**: Requires NVIDIA GPU and CUDA. Enable with `gpu 1` in the `.par` file.

### Subgrid Channel Modeling

- **What It Is**: Models narrow rivers within coarse grids.
- **Why It Matters**: Improves accuracy without slowing down the model.
- **How to Use**: Define channel width and depth in a file (e.g., `channel.asc`).

## Strengths and Limitations

### Strengths

- **Efficient**: Fast for large areas due to simplified equations.
- **Flexible**: Multiple solvers for different flood types.
- **Open-Source**: Free and customizable.
- **GIS Integration**: Works well with QGIS or ArcGIS.

### Limitations

- **Simplified Physics**: Inertial solver may miss complex flow dynamics.
- **Data Dependency**: Needs high-quality DEMs (see {ref}`Chapter 3 <chapter_03>`).
- **Urban Challenges**: Coarse grids may miss small urban features.

| Feature           | Strength                     | Limitation                       |
| ----------------- | ---------------------------- | -------------------------------- |
| Speed             | Fast for large areas         | Slower for high-resolution grids |
| Accuracy          | Good with inertial solver    | Less accurate for complex flows  |
| Data Requirements | Works with standard GIS data | Needs high-quality DEMs          |
| Urban Modeling    | Handles broad urban floods   | May miss small-scale features    |

## Practical Applications

LISFLOOD-FP supports (see {ref}`Chapter 9: Applications of Floodplain Modeling <chapter_09>`):

- **Flood Risk Mapping**: Maps for 100-year floods.
- **Urban Planning**: Identifies safe areas for infrastructure.
- **Historical Analysis**: Reconstructs past floods.
- **Real-Time Forecasting**: Combines with weather models.

```{mermaid}
graph TD
    A[LISFLOOD-FP] --> B[Flood Risk Maps]
    A --> C[Urban Planning]
    A --> D[Historical Analysis]
    A --> E[Real-Time Forecasting]
```

## Tips for Success

1. **Start Small**: Use a 10 km² area with a 10m grid.
2. **Check Data Quality**: Ensure DEM accuracy (see {ref}`Chapter 3 <chapter_03>`).
3. **Use Inertial Solver**: Best balance for most projects.
4. **Validate Results**: Compare with real data (see {ref}`Chapter 8 <chapter_08>`).
5. **Learn GIS**: Use QGIS for data preparation and visualization.

## Further Resources

- **LISFLOOD-FP User Manual**: Setup guide (University of Bristol website).
- **GitHub**: Source code and examples (openearth/lisflood-fp-bmi).
- **Tutorials**: University of Bristol’s training exercises.
- **Research Papers**: Studies on LISFLOOD-FP applications (e.g., Nigeria floods).
- **GIS Tools**: QGIS or ArcGIS for data processing.

This chapter has equipped you with the knowledge to use LISFLOOD-FP for flood modeling. Practice with a small project, explore the resources, and refer to {ref}`Chapter 11: Case Studies in Floodplain Modeling <chapter_11>` for real-world examples.
