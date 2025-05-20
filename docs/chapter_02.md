---
myst:
  html_meta:
    title: Chapter 2 - Fundamentals of Hydrodynamic Modeling
    description: Core concepts and equations in hydrodynamic modeling
---

(chapter_02)=

# Chapter 2: Fundamentals of Hydrodynamic Modeling

```{contents}
:depth: 2
:local:
```

```{mermaid}
graph LR
    A[Hydrodynamic Modeling] --> B[Physical Principles]
    A --> C[Mathematical Formulations]
    A --> D[Numerical Methods]

    B --> B1[Conservation of Mass]
    B --> B2[Conservation of Momentum]
    B --> B3[Energy Conservation]

    C --> C1[Shallow Water Equations]
    C --> C2[Saint-Venant Equations]
    C --> C3[Navier-Stokes Equations]

    D --> D1[Finite Difference]
    D --> D2[Finite Element]
    D --> D3[Finite Volume]
```

## Introduction to Hydraulics and Hydrology

Before delving into the complexities of hydrodynamic modeling, it is essential to understand the fundamental distinction between hydraulics and hydrology, as both disciplines form the foundation of floodplain analysis.

**Hydrology** concerns the study of water movement through the Earth's natural cycle—precipitation, infiltration, runoff, and evaporation. It addresses questions like:

- How much rainfall occurs in a watershed?
- What portion of that rainfall becomes runoff?
- How quickly does water move through a basin?

**Hydraulics**, in contrast, focuses on the mechanics of fluid motion—how water moves through channels, structures, and across landscapes. It addresses questions like:

- How deep will water be at a specific location?
- What velocity will water achieve in a channel?
- How will water interact with structures and topography?

Hydrodynamic modeling primarily operates in the domain of hydraulics but requires hydrological inputs to function properly. This interdisciplinary connection is crucial for accurate flood simulation.

## Physical Principles of Water Flow

### Conservation of Mass

At the heart of hydrodynamic modeling lies the principle of mass conservation, often expressed as the continuity equation. For an incompressible fluid like water, this principle states that the mass flowing into a control volume must equal the mass flowing out, plus any change in storage.

For a one-dimensional channel section, the continuity equation can be expressed as:

```{math}
\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_l
```

Where:

- `A` is the cross-sectional area of flow
- `t` is time
- `Q` is discharge
- `x` is distance along the channel
- `q_l` is lateral inflow or outflow per unit length

This elegantly simple principle ensures that water is neither created nor destroyed within our model domain.

### Conservation of Momentum

The second fundamental principle is the conservation of momentum, which is an application of Newton's second law of motion to fluid flow. The momentum equation accounts for the forces affecting flow velocity and direction:

```{math}
\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} + gAS_f = 0
```

Where:

- `g` is gravitational acceleration
- `h` is water surface elevation
- `S_f` is the friction slope

This equation balances four terms:

1. Local acceleration (change in velocity over time)
2. Convective acceleration (change in velocity over distance)
3. Pressure gradient force (from water surface slope)
4. Friction force (from boundary resistance)

```{mermaid}
graph LR
    A[Forces in Momentum Equation] --> B[Local Acceleration]
    A --> C[Convective Acceleration]
    A --> D[Pressure Gradient Force]
    A --> E[Friction Force]

    B -->|"Temporal velocity changes"| B1["dQ/dt"]
    C -->|"Spatial velocity changes"| C1["d(Q^2/A)/dx"]
    D -->|"Water surface slope"| D1["gA dh/dx"]
    E -->|"Boundary resistance"| E1["gA Sf"]

```

Understanding these forces is crucial for interpreting model outputs and recognizing when different terms dominate under various flow conditions.

### Energy Conservation

While not always explicitly solved in hydrodynamic models, the principle of energy conservation provides valuable insights into flow behavior. The energy equation, derived from Bernoulli's principle, states that the total energy at any point in a fluid system remains constant in the absence of work done by or on the fluid:

```{math}
z + \frac{p}{\rho g} + \frac{v^2}{2g} = \text{constant}
```

Where:

- `z` is elevation head
- `p/(ρg)` is pressure head
- `v²/(2g)` is velocity head

This principle helps us understand transitions between subcritical and supercritical flow regimes, energy losses at hydraulic structures, and the formation of hydraulic jumps—all critical phenomena in flood modeling.

## Mathematical Formulations: The Shallow Water Equations

### Full Shallow Water Equations

The shallow water equations (SWEs) represent the most common mathematical framework for hydrodynamic modeling of floods. They are derived from the Navier-Stokes equations by assuming that:

1. The fluid is incompressible
2. Vertical accelerations are negligible compared to gravity (hydrostatic pressure distribution)
3. The horizontal scale of flow is much greater than the vertical scale

For two-dimensional flow, the shallow water equations consist of one continuity equation and two momentum equations:

**Continuity:**

```{math}
\frac{\partial h}{\partial t} + \frac{\partial (uh)}{\partial x} + \frac{\partial (vh)}{\partial y} = 0
```

**Momentum in x-direction:**

```{math}
\frac{\partial (uh)}{\partial t} + \frac{\partial}{\partial x}\left(u^2h + \frac{1}{2}gh^2\right) + \frac{\partial (uvh)}{\partial y} = gh(S_{0x} - S_{fx})
```

**Momentum in y-direction:**

```{math}
\frac{\partial (vh)}{\partial t} + \frac{\partial (uvh)}{\partial x} + \frac{\partial}{\partial y}\left(v^2h + \frac{1}{2}gh^2\right) = gh(S_{0y} - S_{fy})
```

Where:

- `h` is water depth
- `u` and `v` are velocity components in x and y directions
- `S_{0x}` and `S_{0y}` are bed slopes
- `S_{fx}` and `S_{fy}` are friction slopes

These equations capture the essential physics of flood wave propagation across a floodplain.

### Simplified Forms: The Diffusive Wave Approximation

For many practical applications, the full shallow water equations can be simplified by neglecting certain terms in the momentum equations. The diffusive wave approximation omits the local and convective acceleration terms, resulting in:

```{math}
gh\frac{\partial h}{\partial x} = gh(S_0 - S_f)
```

This approximation is valid when:

- Flow is gradually varied
- Local and convective accelerations are small compared to gravity and friction
- Subcritical flow conditions prevail

The diffusive model significantly reduces computational demands while maintaining accuracy for many floodplain applications where flow dynamics are relatively slow.

### The Kinematic Wave Approximation

An even simpler formulation is the kinematic wave approximation, which assumes that the friction slope equals the bed slope:

```{math}
S_f = S_0
```

This leads to a direct relationship between discharge and depth, often expressed using Manning's equation:

```{math}
Q = \frac{1}{n}AR^{2/3}S_0^{1/2}
```

Where:

- `n` is Manning's roughness coefficient
- `R` is hydraulic radius

The kinematic wave model is appropriate for steep slopes where gravity and friction dominate the flow dynamics, but it cannot capture backwater effects or flow reversal—key phenomena in flat floodplains.

```{mermaid}
graph LR
    A["Shallow Water Equation Simplifications"] --> B["Full Dynamic Wave"]
    A --> C["Diffusive Wave"]
    A --> D["Kinematic Wave"]

    B -->|"Includes all terms"| B1["Local Acceleration"]
    B -->|"Includes all terms"| B2["Convective Acceleration"]
    B -->|"Includes all terms"| B3["Pressure Gradient"]
    B -->|"Includes all terms"| B4["Friction"]

    C -->|"Neglects"| C1["Local Acceleration"]
    C -->|"Neglects"| C2["Convective Acceleration"]
    C -->|"Includes"| C3["Pressure Gradient"]
    C -->|"Includes"| C4["Friction"]

    D -->|"Neglects"| D1["Local Acceleration"]
    D -->|"Neglects"| D2["Convective Acceleration"]
    D -->|"Neglects"| D3["Pressure Gradient"]
    D -->|"Includes"| D4["Friction = Bed Slope"]
```

## Dimensionality in Hydrodynamic Models

### One-Dimensional (1D) Approach

One-dimensional models represent the river or channel as a sequence of cross-sections, solving the 1D Saint-Venant equations:

```{math}
\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_l
```

```{math}
\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} + gAS_f = 0
```

Advantages of 1D models include:

- Computational efficiency
- Simplified data requirements
- Well-established theoretical foundation
- Effective for channel networks with well-defined flow paths

Limitations include:

- Poor representation of lateral flow across floodplains
- Inability to capture two-dimensional flow patterns
- Simplified representation of complex topography

### Two-Dimensional (2D) Approach

Two-dimensional models discretize the floodplain into a grid or mesh of cells, solving the 2D shallow water equations to simulate flow in both x and y directions.

Advantages of 2D models include:

- Explicit representation of flow patterns across floodplains
- Accurate simulation of hydraulic structures
- Better representation of complex topography
- Visualization of spatial flood characteristics

Limitations include:

- Increased computational requirements
- More extensive data needs
- Greater complexity in model setup and calibration

### Coupled 1D-2D Models

Coupled models leverage the strengths of both approaches by using:

- 1D components for efficient modeling of channel flow
- 2D components for accurate representation of floodplain inundation

This hybrid approach optimizes computational resources while maintaining physical realism where it matters most.

```{mermaid}
graph LR
    A["Model Dimensionality"] --> B["1D Models"]
    A --> C["2D Models"]
    A --> D["Coupled 1D-2D Models"]

    B --> B1["River Channel Focus"]
    B --> B2["Cross-section Based"]
    B --> B3["Computationally Efficient"]
    B --> B4["Limited Floodplain Physics"]

    C --> C1["Floodplain Focus"]
    C --> C2["Grid or Mesh Based"]
    C --> C3["Computationally Intensive"]
    C --> C4["Detailed Flow Patterns"]

    D --> D1["Channel: 1D"]
    D --> D2["Floodplain: 2D"]
    D --> D3["Optimized Approach"]
    D --> D4["Lateral Exchange Links"]
```

## Numerical Methods for Solving the Equations

The differential equations governing flow cannot be solved analytically for real-world scenarios. Instead, we employ numerical methods that discretize the continuous equations into algebraic approximations.

### Finite Difference Method

The finite difference method approximates derivatives using differences between values at discrete points:

```{math}
\frac{\partial h}{\partial x} \approx \frac{h_{i+1} - h_i}{\Delta x}
```

This method is:

- Conceptually straightforward
- Easily implemented
- Well-suited for regular grid structures
- The foundation of models like LISFLOOD-FP

### Finite Volume Method

The finite volume method divides the domain into control volumes and enforces conservation principles directly:

```{math}
\frac{\partial}{\partial t}\int_V U dV + \oint_S F \cdot n dS = \int_V S dV
```

Where:

- $U$ represents conserved variables
- $F$ is the flux vector
- $S$ is the source term vector

This method:

- Guarantees conservation at the discrete level
- Handles irregular boundaries effectively
- Forms the basis for models like HEC-RAS 2D

### Finite Element Method

The finite element method approximates the solution using piecewise functions on a mesh of elements:

```{math}
u(x,y) \approx \sum_{i=1}^n N_i(x,y)u_i
```

Where:

- $N_i$ are shape functions
- $u_i$ are nodal values

This method:

- Adapts well to complex geometries
- Provides flexible spatial resolution
- Is employed in models like TELEMAC-2D

## Flow Resistance and Manning's Equation

In hydrodynamic modeling, flow resistance represents the energy loss due to friction between water and boundaries. The most common formulation is Manning's equation:

```{math}
V = \frac{1}{n}R^{2/3}S^{1/2}
```

Where:

- $V$ is flow velocity
- $n$ is Manning's roughness coefficient
- $R$ is hydraulic radius
- $S$ is energy slope

The Manning's roughness coefficient ($n$) is a critical parameter that accounts for:

- Bed material (sand, gravel, cobbles)
- Channel irregularity
- Variation in cross-section
- Obstruction effects
- Vegetation
- Channel meandering

Typical $n$ values range from:

- 0.025-0.035 for natural streams
- 0.01-0.015 for smooth concrete channels
- 0.05-0.08 for vegetated floodplains
- 0.08-0.12 for dense forests

Proper estimation of roughness values is essential for model accuracy, often requiring careful calibration against observed data.

## Critical Flow Concepts

### Froude Number and Flow Regimes

The Froude number (`Fr`) is a dimensionless parameter that characterizes flow regimes:

```{math}
Fr = \frac{V}{\sqrt{gD}}
```

Where:

- `V` is flow velocity
- `g` is gravitational acceleration
- `D` is hydraulic depth

This ratio represents the relative importance of inertial forces to gravitational forces, leading to three flow regimes:

1. **Subcritical flow** ($Fr < 1$): Tranquil, deep, slow flow controlled from downstream
2. **Critical flow** ($Fr = 1$): Transitional state often at hydraulic controls
3. **Supercritical flow** ($Fr > 1$): Rapid, shallow flow controlled from upstream

Floodplain flow is predominantly subcritical, but transitions between regimes can create complex hydraulic phenomena like hydraulic jumps, which must be properly represented in models.

```{mermaid}
graph LR
    A["Flow Regimes"] --> B["Subcritical Flow"]
    A --> C["Critical Flow"]
    A --> D["Supercritical Flow"]

    B -->|"Fr < 1"| B1["Tranquil, Deep, Slow"]
    B -->|"Fr < 1"| B2["Downstream Control"]

    C -->|"Fr = 1"| C1["Transitional State"]
    C -->|"Fr = 1"| C2["Minimum Specific Energy"]

    D -->|"Fr > 1"| D1["Rapid, Shallow, Fast"]
    D -->|"Fr > 1"| D2["Upstream Control"]
```

### Specific Energy and Critical Depth

Specific energy (`E`) is the energy per unit weight of water relative to the channel bottom:

```{math}
E = y + \frac{V^2}{2g}
```

Where:

- `y` is flow depth
- `V` is flow velocity

For a given specific energy, there exist two possible depths:

- A subcritical (deeper) depth
- A supercritical (shallower) depth

The minimum specific energy occurs at critical depth, where `Fr = 1`. This concept is fundamental for understanding flow transitions at hydraulic controls and is crucial for numerically stable models.

## Practical Implications for Modeling

The theoretical foundations discussed above have direct implications for practical flood modeling:

### Model Selection Criteria

Choose model dimensionality and complexity based on:

- Project objectives and required outputs
- Available data quality and quantity
- Computational resources
- Dominant physical processes in the study area
- Required accuracy level

### Numerical Stability Considerations

Ensure model stability by:

- Respecting the Courant-Friedrichs-Lewy (CFL) condition: `{math}C = \frac{V\Delta t}{\Delta x} \leq 1`
- Using appropriate time steps and spatial discretization
- Implementing suitable numerical schemes for your flow conditions
- Carefully handling wetting and drying processes at floodplain edges

### Parameter Sensitivity

Recognize that models are sensitive to:

- Manning's roughness values (particularly in shallow flow)
- Topographic representation (especially at hydraulic controls)
- Boundary condition specification
- Mesh or grid resolution

Systematic sensitivity analysis is essential for understanding model behavior and quantifying uncertainty.

## Emerging Approaches

While the principles outlined in this chapter remain fundamental, several emerging approaches are expanding our modeling capabilities:

### Subgrid Parameterization

Subgrid techniques allow for:

- Representation of features smaller than the grid resolution
- Efficient computation at coarser resolutions
- Improved handling of complex topography

### GPU Acceleration

Graphics Processing Unit (GPU) computing enables:

- Massive parallelization of calculations
- Significant speed improvements (10-100x)
- Higher resolution modeling within practical timeframes

### Machine Learning Integration

Machine learning approaches are being used to:

- Emulate physical models at reduced computational cost
- Improve parameter estimation
- Enhance real-time forecasting capabilities

## Summary

The fundamentals of hydrodynamic modeling rest on physical principles of conservation, translated into mathematical equations that can be solved numerically. Understanding these foundations—from basic hydraulic concepts to numerical methods—is essential for effective model application.

The selection of appropriate model dimensionality and complexity involves balancing physical realism against practical constraints of data availability and computational resources. As we progress through this book, these fundamental concepts will serve as the foundation for exploring specific modeling approaches and tools.

## Key Equations

1. **1D Continuity Equation**: Conservation of mass in channel flow

   ```{math}
   \frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_l
   ```

2. **2D Continuity Equation**: Conservation of mass in floodplain flow

   ```{math}
   \frac{\partial h}{\partial t} + \frac{\partial (uh)}{\partial x} + \frac{\partial (vh)}{\partial y} = 0
   ```

3. **1D Momentum Equation**: Force balance in channel flow

   ```{math}
   \frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} + gAS_f = 0
   ```

4. **Manning's Equation**: Flow resistance relationship

   ```{math}
   V = \frac{1}{n}R^{2/3}S^{1/2}
   ```

5. **Froude Number**: Flow regime classification
   ```{math}
   Fr = \frac{V}{\sqrt{gD}}
   ```

## Discussion Questions

1. How does the selection of model dimensionality (1D vs. 2D) affect the representation of different flood processes? When is the additional complexity of a 2D model justified?

2. What are the implications of using the diffusive wave approximation instead of the full shallow water equations for modeling urban floods?

3. How might climate change impact the validity of certain modeling assumptions, such as steady-state conditions and statistical stationarity?

4. Compare and contrast the roles of topographic data accuracy versus flow resistance parameterization in determining model performance. Which is more critical and why?

5. How do the theoretical foundations of hydrodynamic modeling influence the development of real-time flood forecasting systems?

## Further Reading

- Chow, V.T. (1959). Open-Channel Hydraulics. McGraw-Hill.
- Cunge, J.A., Holly, F.M., & Verwey, A. (1980). Practical Aspects of Computational River Hydraulics. Pitman.
- Hervouet, J.M. (2007). Hydrodynamics of Free Surface Flows: Modelling with the Finite Element Method. Wiley.
- Toro, E.F. (2001). Shock-Capturing Methods for Free-Surface Shallow Flows. Wiley.
- Bates, P.D., Horritt, M.S., & Fewtrell, T.J. (2010). A simple inertial formulation of the shallow water equations for efficient two-dimensional flood inundation modelling. Journal of Hydrology, 387(1-2), 33-45.
