# 📝 Boundary Element Method (BEM)

## 📌 Quick Summary
- **Date**: [2024-11-03]
- **Topic**: [Boundary Element Method for 1D Laplace Equation]
- **Keywords**: #BEM, #1D, #Laplace

## 📚 Main Content

Understanding Boundary Element Method (BEM) always start with a simple 1D problem which could be 1D Laplace equation. This is a great application for both mathematical explanation and visualization. 

### Green's Identities and reciprocal relation
These identities are fundamental to the Boundary Element Method (BEM). They allow us to convert domain integrals to boundary integrals. They're crucial for proving uniqueness of solutions. 

In the context of Laplace Equation,
1. Green's first indentity represent energy conservation.
2. The boundary terms represent flux through the boundaries.
3. The integral term represents the internal energy.

### Green's Function for 1D Laplace Equation

#### Introduction

The Green's function is a fundamental concept in solving differential equations, particularly for the Laplace equation. For the 1D Laplace equation, the Green's function G(x,ξ) represents the response to a unit point source at location ξ.

The governing equation for the Green's function is:

```math
\frac{d^2u}{dx^2} = -\delta(x-\xi)
```

where δ(x-ξ) is the Dirac delta function.

#### Fundamental Solution

The Green's function for the 1D Laplace equation is:

```math
G(x,\xi) = -\frac{1}{2}|x-\xi|
```

##### Key Properties

1. **Symmetry Property**
   ```math
   G(x,\xi) = G(\xi,x)
   ```
   This symmetry is fundamental to reciprocity principles.

2. **Derivative Discontinuity**
   The derivative has a jump at x = ξ:
   ```math
   \frac{\partial G}{\partial x} = \begin{cases}
   -\frac{1}{2} & \text{for } x < \xi \\
   \frac{1}{2} & \text{for } x > \xi
   \end{cases}
   ```

3. **Delta Function Property**
   ```math
   \frac{d^2G}{dx^2} = -\delta(x-\xi)
   ```

### Integral Representation

Using the Green's function, we can represent any solution u(x) to the Laplace equation as:

```math
u(x) = -\int_a^b G(x,\xi)\frac{d^2u}{d\xi^2}d\xi + \left[G(x,\xi)\frac{du}{d\xi} - u(\xi)\frac{\partial G}{\partial \xi}\right]_a^b
```

#### Boundary Element Method (BEM) Form

In the context of boundary element methods, the representation formula becomes:

```math
c(x)u(x) = \int_\Gamma \left(G(x,\xi)\frac{du}{dn}(\xi) - u(\xi)\frac{\partial G}{\partial n}(x,\xi)\right)d\Gamma(\xi)
```

where:
- c(x) is the free term coefficient
- Γ represents the boundary points
- n is the outward normal

### Physical Interpretation

1. **Source Response**
   - The Green's function represents the potential at point x due to a unit source at ξ
   - The magnitude grows linearly with distance from the source
   - The sign changes across the source point

2. **Derivative Behavior**
   - The jump in the derivative at x = ξ corresponds to the source strength
   - The constant derivative on either side reflects the linear nature of the solution

3. **Energy Considerations**
   - The linear behavior minimizes the energy integral
   - Satisfies the principle of minimum potential energy

### Applications

1. **Boundary Value Problems**
   - Solving problems with known boundary conditions
   - Converting domain integrals to boundary integrals
   - Handling point sources and distributed loads

2. **Numerical Methods**
   - Foundation for boundary element methods
   - Basis for fundamental solution methods
   - Green's function as a test function

### Important Characteristics

#### Mathematical Properties
- Linearity
- Symmetry
- Jump discontinuity in derivative
- Smoothness away from source point

#### Physical Properties
- Represents fundamental physics of the problem
- Satisfies conservation principles
- Mimics real physical responses

### Visualization Guide

The interactive visualization above demonstrates:

1. **Source Position (ξ)**
   - Adjustable using the slider
   - Shows how the solution shifts with source location

2. **Function View**
   - Shows the Green's function G(x,ξ)
   - Demonstrates the V-shaped profile
   - Highlights the continuity of the function

3. **Derivative View**
   - Shows the jump discontinuity
   - Illustrates constant derivatives on either side
   - Demonstrates the source strength

### References and Further Reading

1. Stakgold, I., & Holst, M. J. (2011). Green's functions and boundary value problems (Vol. 99). John Wiley & Sons.
2. Kythe, P. K. (2012). Green's functions and linear differential equations: theory, applications, and computation. CRC Press.
3. Duffy, D. G. (2001). Green's functions with applications. CRC Press.