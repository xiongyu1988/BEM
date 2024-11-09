# 📝 Boundary Element Method (BEM)

## 📌 Quick Summary
- **Date**: [2024-11-03]
- **Topic**: [Boundary Element Method for 1D Laplace Equation]
- **Keywords**: #BEM, #1D, #Laplace

## 📚 Main Content

Understanding Boundary Element Method (BEM) always start with a simple 1D problem which could be 1D Laplace equation. This is a great application for both mathematical explanation and visualization. 

### 1. 1D Laplace Equation
Considering Laplace's equation in one dimension for an unknown function $f(x)$,

```math
\frac{d^{2}f}{d x^{2}} = 0
```

The general solution of this 1D Laplace equation is a linear function:

```math
f(x) = a x + b
```

where $a$ and $b$ are constant determined by boundary conditions.

### 2. Green's Identities and reciprocal relation
These identities are fundamental to the Boundary Element Method (BEM). They allow us to convert domain integrals to boundary integrals. They're crucial for proving uniqueness of solutions. 

In the context of Laplace Equation,
1. Green's first indentity represent energy conservation.
2. The boundary terms represent flux through the boundaries.
3. The integral term represents the internal energy.

** Green's First Identity ** in 1D: Multiplying the left-hand side of 1D Laplace equation by a twice-differentiable function $\phi(x)$ and rearranging, we obtain Green's first identity,

```math
\int_a^b v\frac{d^2u}{dx^2}dx = \left[v\frac{du}{dx}\right]_a^b - \int_a^b \frac{dv}{dx}\frac{du}{dx}dx
```

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


# Relationship Between Boundary Value Problems and Green's Second Identity

## 1. Green's Second Identity

Green's second identity (also known as Green's second theorem) in 1D states:

For two functions u(x) and v(x) that are twice continuously differentiable:

```math
\int_a^b (v\frac{d^2u}{dx^2} - u\frac{d^2v}{dx^2})dx = \left[v\frac{du}{dx} - u\frac{dv}{dx}\right]_a^b
```

## 2. Connection to Boundary Value Problems

### 2.1 Standard Boundary Value Problem

Consider the boundary value problem:

```math
\frac{d^2u}{dx^2} = f(x) \quad \text{in } (a,b)
```

with boundary conditions:
```math
u(a) = \alpha, \quad u(b) = \beta
```

### 2.2 Using Green's Function

Let G(x,ξ) be the Green's function satisfying:

```math
\frac{d^2G}{dx^2} = -\delta(x-\xi)
```

with homogeneous boundary conditions:
```math
G(a,\xi) = G(b,\xi) = 0
```

## 3. Deriving the Boundary Value Representation

### 3.1 Application of Green's Second Identity

1. Start with Green's second identity, using G(x,ξ) as v(x):

```math
\int_a^b (G\frac{d^2u}{dx^2} - u\frac{d^2G}{dx^2})dx = \left[G\frac{du}{dx} - u\frac{dG}{dx}\right]_a^b
```

2. Substitute the known equations:
   - d²u/dx² = f(x)
   - d²G/dx² = -δ(x-ξ)

```math
\int_a^b (Gf(x) + u\delta(x-\xi))dx = \left[G\frac{du}{dx} - u\frac{dG}{dx}\right]_a^b
```

### 3.2 Using Properties of Delta Function

The sifting property of the delta function gives:

```math
\int_a^b u\delta(x-\xi)dx = u(\xi)
```

### 3.3 Resulting Representation

This leads to the boundary value representation:

```math
u(\xi) = \int_a^b G(x,\xi)f(x)dx + \left[G(x,\xi)\frac{du}{dx} - u(x)\frac{\partial G}{\partial x}\right]_a^b
```

## 4. Key Insights

### 4.1 Physical Interpretation

- The first term represents the contribution from the source term f(x)
- The boundary terms represent the influence of boundary conditions
- Green's function G(x,ξ) acts as a weighting function

### 4.2 Mathematical Properties

1. **Symmetry**:
```math
G(x,\xi) = G(\xi,x)
```

2. **Jump Condition**:
```math
\left[\frac{\partial G}{\partial x}\right]_{x=\xi} = -1
```

3. **Continuity**:
```math
[G]_{x=\xi} = 0
```

## 5. Application Example

For the 1D Laplace equation:

```math
\frac{d^2u}{dx^2} = 0
```

The boundary value representation simplifies to:

```math
u(\xi) = \left[G(x,\xi)\frac{du}{dx} - u(x)\frac{\partial G}{\partial x}\right]_a^b
```

This shows that the solution is completely determined by boundary values and fluxes.

## 6. Practical Significance

1. **Numerical Methods**:
   - Forms the basis for boundary element method (BEM)
   - Reduces dimensional complexity of the problem

2. **Analysis**:
   - Provides insight into solution behavior
   - Helps prove existence and uniqueness

3. **Engineering Applications**:
   - Heat conduction
   - Electrostatics
   - Fluid flow
   - Structural mechanics

## 7. Conclusion

The relationship between boundary value representation and Green's second identity is fundamental in:
- Converting differential equations to integral equations
- Developing numerical solution methods
- Understanding physical systems
- Proving mathematical properties of solutions

This connection provides both theoretical insight and practical tools for solving boundary value problems.

### References and Further Reading

1. Stakgold, I., & Holst, M. J. (2011). Green's functions and boundary value problems (Vol. 99). John Wiley & Sons.
2. Kythe, P. K. (2012). Green's functions and linear differential equations: theory, applications, and computation. CRC Press.
3. Duffy, D. G. (2001). Green's functions with applications. CRC Press.