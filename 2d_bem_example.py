import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hankel1
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit

# Physical constants
c = 343          # Speed of sound in air (m/s)
rho_0 = 1.225    # Density of air (kg/m^3)
f = 300         # Frequency (Hz)
omega = 2 * np.pi * f  # Angular frequency (rad/s)
k = omega / c    # Wavenumber (rad/m)
V0 = 1.0         # Amplitude of membrane velocity (m/s)
a = 0.5          # Radius of the membrane (m)
alpha = 1  # Absorption coefficient in 1/m

# Spatial domain
x_min, x_max, y_min, y_max = -1.0, 1.0, -1.0, 1.0  # Spatial boundaries (m)
num_points = 1000  # Number of points along each axis

x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2 + Y**2)

# Avoid division by zero at the source location
r[r == 0] = 1e-6



# Compute the pressure using the 2D Green's function
# Approximate outgoing wave solution in 2D
tilde_p = (1j / 4) * hankel1(0, k * r)


# Determine the amplitude A using the boundary condition at r = a
# Compute the Hankel functions at r = a
H0_a = hankel1(0, k * a)
H1_a = hankel1(1, k * a)

# Derivative of the Hankel function H0 at r = a
# The derivative of H0 is -k * H1
H0_prime_a = -k * H1_a

# Radial velocity at r = a
v_r_a = - (1 / (1j * omega * rho_0)) * H0_prime_a * (1j / 4) * H0_a

# Solve for the amplitude correction factor
A = V0 / v_r_a

# Adjust pressure with the amplitude A
tilde_p *= A * np.exp(-alpha * r)

# Define reflection coefficient (e.g., -1 for a rigid boundary)
R = -1
L = 0.6

# Calculate distance to boundary
x_boundary = L
r_reflected = np.sqrt((X - 2 * x_boundary)**2 + Y**2)

# Compute reflected pressure
tilde_p_reflected = R * (1j / 4) * hankel1(0, k * r_reflected)

# Total pressure is sum of incident and reflected
tilde_p_total = tilde_p + tilde_p_reflected


# Compute pressure gradient components
dtilde_p_dx = np.gradient(tilde_p_total, x, axis=1)
dtilde_p_dy = np.gradient(tilde_p_total, y, axis=0)

# Compute magnitude of pressure gradient
grad_p_magnitude = np.sqrt(np.abs(dtilde_p_dx)**2 + np.abs(dtilde_p_dy)**2)

# Create a 3D surface plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Subsample the data for plotting to improve performance
stride = 5  # Adjust stride for resolution of the plot
X_sub = X[::stride, ::stride]
Y_sub = Y[::stride, ::stride]
Z_sub = grad_p_magnitude.real[::stride, ::stride]

# Plot the surface
surf = ax.plot_surface(X_sub, Y_sub, Z_sub, cmap='viridis', edgecolor='none')

# Add color bar and labels
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Magnitude of Pressure Gradient')
ax.set_title('Pressure Gradient Magnitude in 2D Space (3D Surface Plot)')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('Magnitude of Pressure Gradient')
ax.set_zlim(0, 10000)

# Set viewing angle for better visualization
ax.view_init(elev=30, azim=225)


# Add contour lines to the surface plot
ax.contour(X_sub, Y_sub, Z_sub, zdir='z', offset=Z_sub.min(), cmap='coolwarm')
# Extract data along y = 0
x_line = x
z_line = grad_p_magnitude.real[num_points // 2, :]  # Middle row

plt.figure()
plt.plot(x_line, z_line)
plt.title('Pressure Gradient Magnitude Along y = 0')
plt.xlabel('x (m)')
plt.ylabel('Magnitude of Pressure Gradient')
plt.grid(True)
plt.show()

plt.show()
