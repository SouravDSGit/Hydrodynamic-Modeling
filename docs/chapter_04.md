---
myst:
  html_meta:
    title: Chapter 4 - One-Dimensional (1D) Hydrodynamic Models
    description: Core concepts and equations in hydrodynamic modeling
---

(chapter_04)=

# Chapter 4: One-Dimensional (1D) Hydrodynamic Models

```{contents}
:depth: 2
:local:
```

```{mermaid}
graph TD
    A["1D Hydrodynamic Models"] --> B["Key Concepts"]
    A --> C["Popular Software"]
    A --> D["Applications"]
    A --> E["Limitations"]

    B --> B1["Cross-Section Based"]
    B --> B2["Saint-Venant Equations"]
    B --> B3["Simplified Network"]

    C --> C1["HEC-RAS 1D"]
    C --> C2["MIKE 11"]
    C --> C3["ISIS/Flood Modeller Pro"]

    D --> D1["River Hydraulics"]
    D --> D2["Flood Forecasting"]
    D --> D3["Structure Impact Assessment"]

    E --> E1["Limited Floodplain Representation"]
    E --> E2["Perpendicular Flow Assumption"]
    E --> E3["Complex Geometry Challenges"]
```

## Introduction to One-Dimensional Modeling

One-dimensional (1D) hydrodynamic models represent the foundation of computational river hydraulics. These models simulate water flow along a single spatial dimension—the longitudinal axis of a river channel—providing efficient solutions for many practical engineering and management problems. Despite the growing popularity of more complex 2D and 3D approaches, 1D models remain vital tools in the hydrodynamic modeling toolkit due to their computational efficiency, straightforward implementation, and proven track record in real-world applications.

This chapter explores the fundamental concepts, mathematical formulations, practical applications, and limitations of 1D hydrodynamic models, with a focus on their role in floodplain management.

## Conceptual Framework of 1D Models

### The Cross-Section Representation

1D models represent a river network as a series of cross-sections perpendicular to the main flow direction. Each cross-section captures the channel geometry at a specific location, defined by:

- Channel bed elevation
- Bank positions and elevations
- Floodplain geometry (when included)
- Roughness characteristics

```{mermaid}
graph TD
    A["River Representation in 1D Model"] --> B["River Centerline"]
    A --> C["Cross-Sections"]
    A --> D["Hydraulic Structures"]

    B --> B1["Defines Flow Path"]
    B --> B2["Distances Between Cross-Sections"]

    C --> C1["Perpendicular to Flow"]
    C --> C2["Capture Channel Geometry"]
    C --> C3["Define Conveyance Capacity"]

    D --> D1["Bridges"]
    D --> D2["Culverts"]
    D --> D3["Weirs & Dams"]
```

The spacing between cross-sections is critical for model accuracy and stability. Cross-sections should be placed:

- At significant changes in channel geometry
- At hydraulic structures (bridges, weirs, etc.)
- Where flow conditions change (tributaries, rapids)
- With sufficient density to capture longitudinal variation

### Flow Representation

1D models assume that:

1. Water flows primarily along the channel axis
2. Velocity is uniform (or follows a predefined distribution) across each cross-section
3. Water surface elevation is constant across each cross-section
4. Pressure distribution is hydrostatic

These assumptions work well for:

- Rivers with well-defined channels
- Gradual changes in flow conditions
- Subcritical flow regimes

But become problematic in conditions with significant lateral flow components or rapidly varied flow.

## Mathematical Foundation: The Saint-Venant Equations

### Derivation and Assumptions

The one-dimensional Saint-Venant equations form the mathematical foundation of 1D hydrodynamic models. These equations, derived from the principles of mass and momentum conservation, consist of:

1. **Continuity Equation** (conservation of mass):

```{math}
\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_l
```

2. **Momentum Equation** (conservation of momentum):

```{math}
\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} + gAS_f = 0
```

Where:

- `A` is the cross-sectional area of flow
- `Q` is discharge
- `t` is time
- `x` is distance along the channel
- `q_l` is lateral inflow/outflow per unit length
- `g` is gravitational acceleration
- `h` is water surface elevation
- `S_f` is the friction slope

These equations rely on several key assumptions:

- Flow is one-dimensional (primarily along the channel axis)
- Vertical accelerations are negligible (hydrostatic pressure distribution)
- Channel bed slope is small
- Friction can be represented by steady-state formulations (e.g., Manning equation)
- Fluid density is constant (incompressible flow)

### Simplified Variants

For certain applications, simplified versions of the Saint-Venant equations provide adequate results with reduced computational demands:

1. **Diffusive Wave Approximation**

   - Neglects local and convective acceleration terms
   - Valid for gradually varied flows where inertial forces are small
   - Common in flood routing applications

2. **Kinematic Wave Approximation**
   - Assumes friction slope equals bed slope
   - Valid for steep channels with predominantly supercritical flow
   - Often used in watershed runoff modeling
   - Cannot represent backwater effects

```{mermaid}
graph TD
    A["Saint-Venant Equation Variants"] --> B["Full Dynamic Wave"]
    A --> C["Diffusive Wave"]
    A --> D["Kinematic Wave"]

    B -->|"Includes all terms"| B1["Most Complete"]
    B -->|"Includes all terms"| B2["Most Computationally Demanding"]

    C -->|"Neglects acceleration"| C1["Captures Backwater Effects"]
    C -->|"Intermediate complexity"| C2["Suitable for Most Floods"]

    D -->|"Most simplified"| D1["Fastest Computation"]
    D -->|"Most restrictive"| D2["Limited to Simple Channels"]
```

## Numerical Implementation

### Discretization Approaches

To solve the Saint-Venant equations numerically, 1D models employ various discretization schemes:

1. **Finite Difference Methods**

   - Approximate derivatives using differences between discrete points
   - Can be explicit (simpler but conditional stability) or implicit (more complex but unconditionally stable)
   - Common in many established 1D models

2. **Finite Volume Methods**
   - Ensure conservation properties by integrating over control volumes
   - Handle discontinuities well (hydraulic jumps, rapid transitions)
   - Becoming increasingly common in modern implementations

### Stability Considerations

Numerical stability is crucial for reliable 1D model results. Key considerations include:

- **Courant-Friedrichs-Lewy (CFL) condition**: For explicit schemes, `C = V∆t/∆x ≤ 1`
- **Time step selection**: Balancing computational efficiency with stability
- **Spatial discretization**: Cross-section spacing and representation
- **Wetting/drying algorithms**: Handling the moving boundary between wet and dry areas

## Popular 1D Modeling Software

### HEC-RAS 1D

Developed by the U.S. Army Corps of Engineers, HEC-RAS (Hydrologic Engineering Center's River Analysis System) is one of the most widely used 1D modeling tools:

- **Capabilities**: Steady and unsteady flow simulation, sediment transport, water quality
- **Strengths**: Free, well-documented, extensive user community, powerful visualization
- **Applications**: Floodplain mapping, bridge hydraulics, regulatory studies
- **Interface with 2D**: Later versions include integrated 1D/2D capabilities

### MIKE 11

Developed by DHI, MIKE 11 is a professional software package widely used in water resources:

- **Capabilities**: Hydrodynamics, sediment transport, water quality, real-time forecasting
- **Strengths**: Robust numerical schemes, comprehensive modules, excellent technical support
- **Applications**: Flood forecasting, dam break analysis, water resource management
- **Integration**: Seamless coupling with MIKE 21 for 1D/2D modeling (MIKE FLOOD)

### ISIS/Flood Modeller Pro

Originally developed by Halcrow (now part of Jacobs) as ISIS and rebranded as Flood Modeller Pro:

- **Capabilities**: 1D river modeling, structures, real-time forecasting
- **Strengths**: User-friendly interface, specialized for UK environment, regulatory acceptance
- **Applications**: Flood risk assessment, structure design, flood forecasting
- **Integration**: Can be linked with 2D models like TUFLOW

## Practical Applications of 1D Models

### Flood Forecasting and Warning Systems

1D models excel in operational flood forecasting due to:

- Computational efficiency enabling real-time simulations
- Ability to rapidly process long river reaches
- Straightforward integration with rainfall-runoff models
- Established calibration procedures with historical events

Many national flood warning systems rely on 1D models as their hydraulic component, often coupled with data assimilation techniques to improve forecast accuracy.

### Hydraulic Structure Design and Assessment

1D models are the standard tool for:

- Bridge and culvert hydraulic analysis
- Flood defense sizing
- Weir and dam operations
- Channel modification assessment

These applications benefit from the models' ability to efficiently simulate:

- Backwater effects
- Flow transitions (subcritical to supercritical)
- Pressure flow conditions
- Structure interactions

### Floodplain Mapping and Regulation

Despite limitations in representing complex floodplain flow, 1D models remain important for:

- Regulatory floodplain delineation
- Flood insurance studies
- Preliminary flood risk assessment
- Long-term planning scenarios

Many jurisdictions accept or require 1D modeling results for regulatory purposes, often with specific guidelines for model development and application.

### Water Quality and Sediment Transport

Beyond flood modeling, 1D models serve as platforms for:

- Pollutant fate and transport simulation
- Sediment erosion and deposition studies
- Temperature modeling
- Habitat assessment

These applications leverage the computational efficiency of 1D approaches to simulate long time periods and multiple scenarios.

## Limitations and Challenges

### Geometric Representation Constraints

1D models are fundamentally limited by their simplified representation of:

- Complex channel networks
- Meandering rivers with significant lateral flow
- Braided channels
- Wide floodplains
- Urban environments with complex flow paths

```{mermaid}
graph TD
    A["1D Model Limitations"] --> B["Geometric Constraints"]
    A --> C["Flow Assumptions"]
    A --> D["Floodplain Representation"]

    B --> B1["Limited to Channel Centerline"]
    B --> B2["Cross-Section Orientation Issues"]

    C --> C1["Assumes Perpendicular Flow"]
    C --> C2["Uniform Velocity Distribution"]
    C --> C3["Horizontal Water Surface"]

    D --> D1["Storage Areas Only"]
    D --> D2["Limited Flow Paths"]
    D --> D3["No Lateral Momentum Transfer"]
```

### Floodplain Flow Limitations

The most significant limitation of 1D models appears during floodplain inundation, where they struggle to represent:

- Two-dimensional flow patterns
- Flow paths not aligned with the main channel
- Areas with significant lateral velocity components
- Multiple flow paths with different directions
- Flow around structures and obstacles

### Addressing Limitations Through Extensions

Several approaches extend 1D capabilities for floodplain modeling:

1. **Quasi-2D approaches**

   - Storage cells connected to the main channel
   - Link-node networks representing floodplain flow paths
   - Limited momentum exchange but improved volume conservation

2. **Parallel conveyance paths**

   - Multiple 1D channels representing floodplain flow
   - Connected through lateral structures
   - Improved representation of compound channels

3. **1D/2D coupling**
   - 1D model for main channel
   - 2D model for floodplains
   - Dynamic exchange at the interface
   - Combines computational efficiency with improved floodplain physics

## Model Development Best Practices

### Data Requirements

Successful 1D model development requires:

- **Topographic data**: Channel and floodplain cross-sections
- **Hydrologic inputs**: Flow hydrographs, tributary contributions
- **Roughness values**: Manning's n for channel and floodplains
- **Structure details**: Bridge, culvert, weir dimensions and properties
- **Boundary conditions**: Upstream flows, downstream stages

### Cross-Section Placement and Processing

Critical decisions in 1D modeling include:

- Strategic cross-section placement at hydraulically significant locations
- Appropriate spacing based on channel characteristics
- Consideration of expansion/contraction zones
- Proper orientation perpendicular to expected flow paths
- Extension across the full potential floodplain width

### Calibration and Validation

Model performance should be evaluated through:

- Comparison with observed water levels at gauging stations
- Verification against historical flood extents
- Sensitivity analysis of key parameters (roughness, structure coefficients)
- Uncertainty assessment for critical outputs

Typical calibration parameters include:

- Manning's roughness coefficients
- Structure loss coefficients
- Expansion/contraction coefficients
- Effective flow areas

## When to Choose a 1D Approach

1D models remain the preferred choice when:

- The study area is primarily composed of well-defined channels
- Flow is predominantly aligned with the channel axis
- Computational efficiency is a priority (large networks, long simulations)
- Limited data is available for more complex approaches
- Regulatory requirements specify 1D methods
- Quick assessment is needed for screening or preliminary studies
- The focus is on water levels rather than detailed flow patterns

## Case Studies: Successful Applications

### Flood Forecasting on the Mississippi River

The U.S. National Weather Service uses a comprehensive 1D model to:

- Forecast floods along 2,500+ km of the Mississippi River
- Provide 5-day advance warning of flood levels
- Inform emergency management decisions
- Optimize reservoir operations during flood events

The model demonstrates the capability of 1D approaches to handle large-scale river systems efficiently while providing actionable information.

### Bridge Hydraulics Assessment

A case study on the Ohio River illustrates how 1D models effectively:

- Evaluate bridge scour risk during floods
- Assess impacts of proposed bridge designs
- Determine required bridge clearances
- Analyze pressure flow conditions
- Evaluate floodplain encroachment

This application leverages the specialized hydraulic structure capabilities of 1D models.

## Integration with Other Model Types

Modern flood modeling often integrates 1D approaches with complementary models:

- **Rainfall-runoff models**: Providing inflow hydrographs
- **2D floodplain models**: Detailed inundation mapping
- **Groundwater models**: Subsurface interactions
- **Water quality models**: Environmental impacts
- **Real-time data systems**: Operational forecasting

This integration leverages the strengths of each approach while addressing limitations.

## Future Directions

Despite being among the oldest hydrodynamic modeling approaches, 1D models continue to evolve:

- Improved numerical schemes for better stability and efficiency
- Enhanced structure handling for complex hydraulic features
- Better methods for parameter estimation and uncertainty analysis
- Seamless integration with 2D and 3D approaches
- Machine learning methods for parameter optimization and real-time correction

## Summary

One-dimensional hydrodynamic models provide an efficient, well-established approach for simulating river hydraulics and flooding. While they have inherent limitations in representing complex floodplain flow, they remain essential tools for:

- River engineering
- Flood forecasting
- Hydraulic structure assessment
- Preliminary flood mapping
- Water quality studies

Their computational efficiency, straightforward implementation, and long history of successful application ensure that 1D models will remain important components of the flood modeler's toolkit, particularly when integrated with complementary modeling approaches.

## Key Equations

1. **1D Continuity Equation**:

   ```{math}
   \frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_l
   ```

2. **1D Momentum Equation**:

   ```{math}
   \frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} + gAS_f = 0
   ```

3. **Manning's Equation** (often used to calculate friction slope):

   ```{math}
   Q = \frac{1}{n}AR^{2/3}S_f^{1/2}
   ```

4. **Courant Number** (for numerical stability):
   ```{math}
   C = \frac{V\Delta t}{\Delta x} \leq 1
   ```

## Discussion Questions

1. How does the representation of floodplains differ between 1D and 2D models, and what are the implications for flood risk assessment?

2. Under what circumstances might a 1D model provide more accurate results than a 2D model, despite the more simplified physics?

3. How might climate change impact the applicability and limitations of 1D models for flood forecasting?

4. What are the key considerations when deciding between full dynamic wave, diffusive wave, and kinematic wave formulations for a particular application?

5. How might advances in data collection (LiDAR, remote sensing) and computational resources change the role of 1D models in future flood management practice?

## Further Reading

- Cunge, J.A., Holly, F.M., & Verwey, A. (1980). Practical Aspects of Computational River Hydraulics. Pitman.
- Brunner, G.W. (2016). HEC-RAS River Analysis System: Hydraulic Reference Manual. US Army Corps of Engineers.
- Knight, D.W., & Shamseldin, A.Y. (Eds.). (2005). River Basin Modelling for Flood Risk Mitigation. CRC Press.
- DHI. (2023). MIKE 11: A Modelling System for Rivers and Channels - Reference Manual. DHI Water & Environment.
- Flood Modeller. (2023). 1D River Modelling User Manual. Jacobs.
