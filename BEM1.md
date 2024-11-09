# Boundary Element Method (BEM)

Understanding Boundary Element Method (BEM) always start with a simple 1D problem which could be 1D Laplace equation. This is a great application for both mathematical explanation and visualization. 

## 1. 1D Laplace Equation
Considering Laplace's equation in one dimension for an unknown function $f(x)$,

```math
\frac{d^{2}f}{d x^{2}} = 0
```

The general solution of this 1D Laplace equation is a linear function:

```math
f(x) = a x + b
```

where $a$ and $b$ are constant determined by boundary conditions.

## 2. Green's Identities and reciprocal relation
These identities are fundamental to the Boundary Element Method (BEM). They allow us to convert domain integrals to boundary integrals. They're crucial for proving uniqueness of solutions. 

In the context of Laplace Equation,
1. Green's first indentity represent energy conservation.
2. The boundary terms represent flux through the boundaries.
3. The integral term represents the internal energy.

**Green's First Identity** in 1D: Multiplying the left-hand side of 1D Laplace equation by a twice-differentiable function $\phi(x)$ and rearranging, we obtain Green's first identity,

```math
\int_a^b \phi\frac{d^2f}{dx^2}dx = \left[\phi\frac{df}{dx}\right]_a^b - \int_a^b \frac{d\phi}{dx}\frac{dx}{dx}dx
```

In other form,
```math
\phi\frac{d^2f}{dx^2} = \frac{d}{dx}\left[\phi\frac{df}{dx}\right] - \frac{d\phi}{dx}\frac{dx}{dx}
```


**Green's Second Identity** in 1D: Interchanging the roles of functions $\phi$ and $f$, then subtracting from one to another, we obtain Green's second identity,

```math
\int_a^b \left(\phi\frac{d^2f}{dx^2} - f\frac{d^2\phi}{dx^2}\right)dx = \left[\phi\frac{df}{dx} - f\frac{d\phi}{dx}\right]_a^b
```

In other form,
```math
\phi\frac{d^2f}{dx^2} - f\frac{d^2\phi}{dx^2} = \frac{d}{dx}\left[\phi\frac{df}{dx} - f\frac{d\phi}{dx}\right]
```

**Reciprocal Relation**: If both $\phi$ and $f$ satisfy the Laplace equation,

```math
\frac{d^2u}{dx^2} = 0 \quad \text{and} \quad \frac{d^2v}{dx^2} = 0
```

Then the reciprocal relation becomes:

```math
\left[v\frac{du}{dx} - u\frac{dv}{dx}\right]_a^b = 0
```

## 3. Green's Function for 1D Laplace Equation

The Green's function is a fundamental concept in solving differential equations, particularly for the Laplace equation. For the 1D Laplace equation, the Green's function $G(x,\xi)$ represents the response to a unit point source at location $\xi$. The governing equation for the Green's function is:

```math
\frac{d^2 G(x,\xi)}{dx^2} + \delta(x-\xi) = 0 
```

where $\delta(x-\xi)$ is the Dirac delta function, $x$ is the variable field point, $\xi$ is the fixed location of the singular point or pole.

### 3.1 Fundamental Solution

A solution of this Green's function for the 1D Laplace equation is the piecewise linear function,

```math
G(x,\xi) = -\frac{1}{2}|x-\xi|
```

#### 3.1.1 Key Properties

1. **Symmetry Property**
   ```math
   G(x,\xi) = G(\xi,x)
   ```
   This symmetry is fundamental to reciprocity principles.

2. **Derivative Discontinuity**
   The derivative has a jump at $x = \xi$:
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

#### 3.1.2 Physical Interpretation

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


### 3.2 Boundary Value Problems and Green's Second Identity

#### 3.2.1 Standard Boundary Value Problem

Consider the boundary value problem:

```math
\frac{d^2u}{dx^2} = f(x) \quad \text{in } (a,b)
```

with boundary conditions:
```math
u(a) = \alpha, \quad u(b) = \beta
```

#### 3.2.2 Using Green's Function

Let $G(x,\xi)$ be the Green's function satisfying:

```math
\frac{d^2G}{dx^2} = -\delta(x-\xi)
```

with homogeneous boundary conditions:
```math
G(a,\xi) = G(b,\xi) = 0
```

### 3.2.3 Deriving the Boundary Value Representation

1. Start with Green's second identity:

```math
\int_a^b (G\frac{d^2f}{dx^2} - f\frac{d^2G}{dx^2})dx = \left[G\frac{df}{dx} - f\frac{dG}{dx}\right]_a^b
```

2. Substitute the known equations:
   - $\frac{d^2f}{dx^2} = F(x)$
   - $\frac{d^2G}{dx^2} = - \delta(x-\xi)$

```math
\int_a^b (GF(x) + f\delta(x-\xi))dx = \left[G\frac{df}{dx} - f\frac{dG}{dx}\right]_a^b
```

3. The sifting property of the delta function gives:

```math
\int_a^b f\delta(x-\xi)dx = f(\xi)
```

4. Resulting Representation

This leads to the boundary value representation:

```math
f(\xi) = \int_a^b G(x,\xi)F(x)dx + \left[G(x,\xi)\frac{df}{dx} - f(x)\frac{\partial G}{\partial x}\right]_a^b
```

## Application to 1D Helmholtz's Equation

## 5.References

1. Stakgold, I., & Holst, M. J. (2011). Green's functions and boundary value problems (Vol. 99). John Wiley & Sons.
2. Kythe, P. K. (2012). Green's functions and linear differential equations: theory, applications, and computation. CRC Press.
3. Duffy, D. G. (2001). Green's functions with applications. CRC Press.