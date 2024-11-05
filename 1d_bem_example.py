import numpy as np
import matplotlib.pyplot as plt

# Physical constants
c = 343          # Speed of sound in air (m/s)
rho_0 = 1.225    # Density of air (kg/m^3)
f = 1000         # Frequency (Hz)
omega = 2 * np.pi * f  # Angular frequency (rad/s)
k = omega / c    # Wavenumber (rad/m)
V0 = 1.0         # Amplitude of piston velocity (m/s)

# Spatial domain
x = np.linspace(0, 2, 500)  # Positions from 0 to 2 meters

# Compute the pressure
# Solution to the wave equation: traveling wave in positive x-direction
tilde_p = -rho_0 * c * V0 * np.exp(-1j * k * x)

# Compute the pressure gradient
dtilde_p_dx = np.gradient(tilde_p, x)

# Alternatively, compute analytical derivative
# dtilde_p_dx = 1j * k * rho_0 * c * V0 * np.exp(-1j * k * x)

# Plotting
plt.figure(figsize=(12, 6))

# Real part of pressure gradient
plt.subplot(1, 2, 1)
plt.plot(x, np.real(dtilde_p_dx), label='Real Part')
plt.title('Real Part of Pressure Gradient')
plt.xlabel('Position x (m)')
plt.ylabel('Re{dp/dx}')
plt.grid(True)
plt.legend()

# Imaginary part of pressure gradient
plt.subplot(1, 2, 2)
plt.plot(x, np.imag(dtilde_p_dx), label='Imaginary Part', color='orange')
plt.title('Imaginary Part of Pressure Gradient')
plt.xlabel('Position x (m)')
plt.ylabel('Im{dp/dx}')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
