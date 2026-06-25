import numpy as np
import matplotlib.pyplot as plt


def single_slit_intensity(theta, wavelength, slit_width):
    """
    Calculate the Fraunhofer diffraction intensity pattern for a single slit.
    """
    beta = np.pi * slit_width * np.sin(theta) / wavelength

    # Avoid division by zero at theta = 0
    intensity = np.ones_like(beta)
    nonzero = beta != 0
    intensity[nonzero] = (np.sin(beta[nonzero]) / beta[nonzero]) ** 2

    return intensity


def double_slit_intensity(theta, wavelength, slit_width, slit_separation):
    """
    Calculate the double-slit pattern:
    single-slit diffraction envelope multiplied by double-slit interference.
    """
    beta = np.pi * slit_width * np.sin(theta) / wavelength
    alpha = np.pi * slit_separation * np.sin(theta) / wavelength

    envelope = np.ones_like(beta)
    nonzero = beta != 0
    envelope[nonzero] = (np.sin(beta[nonzero]) / beta[nonzero]) ** 2

    interference = np.cos(alpha) ** 2

    return envelope * interference


# Physical parameters
wavelength = 650e-9        # 650 nm red light
slit_width = 40e-6         # 40 micrometres
slit_separation = 150e-6   # 150 micrometres

# Angular range
theta = np.linspace(-0.05, 0.05, 5000)  # radians

# Calculate intensities
single = single_slit_intensity(theta, wavelength, slit_width)
double = double_slit_intensity(theta, wavelength, slit_width, slit_separation)

# Convert angle to screen position
screen_distance = 1.0  # metres
x = screen_distance * np.tan(theta)

# Plot single-slit diffraction
plt.figure(figsize=(8, 4.5))
plt.plot(x * 1000, single)
plt.xlabel("Position on screen / mm")
plt.ylabel("Normalised intensity")
plt.title("Single-Slit Diffraction Pattern")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/single_slit_diffraction.png", dpi=300)
plt.show()

# Plot double-slit interference
plt.figure(figsize=(8, 4.5))
plt.plot(x * 1000, double)
plt.xlabel("Position on screen / mm")
plt.ylabel("Normalised intensity")
plt.title("Double-Slit Interference with Diffraction Envelope")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/double_slit_interference.png", dpi=300)
plt.show()


wavelengths = {
    "Blue light, 450 nm": 450e-9,
    "Green light, 532 nm": 532e-9,
    "Red light, 650 nm": 650e-9,
}

plt.figure(figsize=(8, 4.5))

for label, wl in wavelengths.items():
    intensity = double_slit_intensity(theta, wl, slit_width, slit_separation)
    plt.plot(x * 1000, intensity, label=label)

plt.xlabel("Position on screen / mm")
plt.ylabel("Normalised intensity")
plt.title("Effect of Wavelength on Double-Slit Interference")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/wavelength_comparison.png", dpi=300)
plt.show()