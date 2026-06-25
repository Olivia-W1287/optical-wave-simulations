import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Gaussian beam parameters
# -----------------------------

wavelength = 650e-9       # wavelength of red light in metres
w0 = 0.5e-3               # beam waist radius in metres
z_R = np.pi * w0**2 / wavelength   # Rayleigh range

# z values: propagation distance from the beam waist
z = np.linspace(-2 * z_R, 2 * z_R, 1000)

# beam radius as a function of z
w_z = w0 * np.sqrt(1 + (z / z_R)**2)

# -----------------------------
# Plot beam radius
# -----------------------------

plt.figure(figsize=(8, 4.5))
plt.plot(z, w_z * 1000, label="Beam radius")
plt.plot(z, -w_z * 1000, label="Beam radius")
plt.xlabel("Propagation distance z / m")
plt.ylabel("Beam radius / mm")
plt.title("Gaussian Beam Propagation")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/gaussian_beam_radius.png", dpi=300)
plt.show()


# -----------------------------
# Intensity profile at different distances
# -----------------------------

x = np.linspace(-3e-3, 3e-3, 1000)

z_positions = [0, z_R, 2 * z_R]

plt.figure(figsize=(8, 4.5))

for position in z_positions:
    w = w0 * np.sqrt(1 + (position / z_R)**2)
    intensity = (w0 / w)**2 * np.exp(-2 * x**2 / w**2)

    label = f"z = {position:.2f} m"
    plt.plot(x * 1000, intensity, label=label)

plt.xlabel("Transverse position x / mm")
plt.ylabel("Normalised intensity")
plt.title("Gaussian Beam Intensity Profiles")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/gaussian_intensity_profiles.png", dpi=300)
plt.show()