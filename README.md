# Optical Wave Simulation Project

This project models optical diffraction and interference using Python.

## Aim

The aim was to investigate how light propagates through single and double slits, using numerical simulation and visualisation. This is relevant to optical physics, photonics, imaging systems and wave-based sensing technologies.

## Physics

The single-slit diffraction pattern is modelled using:

I(theta) = I0 (sin(beta) / beta)^2

where beta = pi a sin(theta) / lambda.

The double-slit pattern combines the single-slit diffraction envelope with the interference term:

I(theta) = I0 (sin(beta) / beta)^2 cos^2(alpha)

where alpha = pi d sin(theta) / lambda.

## Methods

Python was used to:
- Define physical parameters including wavelength, slit width and slit separation.
- Calculate intensity as a function of angle.
- Convert angular position to screen position.
- Plot and compare diffraction and interference patterns.
- Investigate the effect of changing wavelength.

## Key Findings

- A narrower slit produces a wider diffraction pattern.
- Double slits produce high-frequency interference fringes within a broader single-slit envelope.
- Longer wavelengths produce wider fringe spacing.
- The simulation demonstrates how wave interference can be modelled computationally, with relevance to optical and photonic systems.

## Tools Used

Python, NumPy, Matplotlib


## Gaussian Beam Propagation

I also modelled Gaussian laser beam propagation, which is relevant to optical systems, imaging, photonics and laser-based measurement.

The beam radius is given by:

w(z) = w0 sqrt(1 + (z / zR)^2)

where zR = pi w0^2 / lambda is the Rayleigh range.

The simulation shows how a laser beam spreads after its waist and how the transverse intensity profile becomes wider and lower with propagation distance.

This demonstrates the use of physical modelling and Python visualisation to analyse optical beam behaviour.