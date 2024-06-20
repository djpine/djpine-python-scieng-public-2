import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import yaml


def displacement(time, mass, g, drag_coef_v2, v0):
    v1 = np.sqrt(mass * g / drag_coef_v2)
    arg = g * time / v1
    return (v1**2 / g) * np.log(np.cosh(arg) + (v0 / v1) * np.sinh(arg))


def deriv(f, x, h=1.e-9, *params):
    return (f(x + h, *params) - f(x - h, *params)) / (2. * h)


filename = "steel1"

g = 9.795  # [m/s^2] acceleration due to gravity
laser_separation = 0.18  # [m]

t_noise = 0.0005  # [s]

density_air = 1.1839  # kg/m^3
cd = 0.47  # drag coefficient for a sphere

tmax = 0.6  # falls about 1.7+ meters total

fmeta = open(filename + ".yaml", "r")
meta = yaml.safe_load(fmeta)
fmeta.close()

mass = meta["mass_gm"] / 1000.0  # ball mass in kg
radius = meta["radius_cm"] / 100.0  # ball radius in m
y00 = meta["magnet_to_laser_cm"] / 100.0  # [m]]

drag_coef_v2 = 0.5 * cd * np.pi * radius**2 * density_air

y0 = y00 - 2.0 * radius
v0 = 0.0

time = np.linspace(0.0, tmax, 200)

y = displacement(time, mass, g, drag_coef_v2, v0)
v = deriv(displacement, time, 1.e-1, *(mass, g, drag_coef_v2, v0))
a = (v[:-1] - v[1:]) / (time[1] - time[0])

ynofric = v0 * time + 0.5 * g * time**2

# Find times when sphere edges pass laser beam
laser_postitions_m = np.arange(
    y0, ynofric[-1], laser_separation)  # [m]
tcross_front = np.zeros(laser_postitions_m.size)  # [s]
tcross_back = np.zeros(laser_postitions_m.size)  # [s]
for i, yf in enumerate(laser_postitions_m):
    # First, find time front edge crosses beam
    def dy(t): return displacement(t, mass, g, drag_coef_v2, v0) - yf
    tc_guess = (2.0 * yf / g)**0.5
    tcross_front[i] = brentq(dy, 0.9 * tc_guess, 1.1 * tc_guess)
    # Second, find time back edge crosses beam
    yb = yf + 2.0 * radius
    def dy(t): return displacement(t, mass, g, drag_coef_v2, v0) - yb
    tc_guess = (2.0 * yb / g)**0.5
    tcross_back[i] = brentq(dy, 0.9 * tc_guess, 1.1 * tc_guess)

tcross = np.sort(np.concatenate((tcross_front, tcross_back)))
# Add noise to crossing times
rng = np.random.default_rng()
tcross += t_noise * rng.standard_normal(tcross.size)
tcross -= tcross[0]

# Save crossing times to text data file
np.savetxt(filename + ".txt", tcross, fmt="%0.6f")

# Plot data generated
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.5, 8), sharex=True)
ax1.plot(time, 1000.0 * (y - ynofric))
ax1.set_xlim(0.0, tmax)
ax1.set_ylabel(r"$y(t)-y_0(t)$ [mm]")
ax1.text(0.02, 0.02, f"material = {meta['material']}", ha="left", va="bottom",
         transform=ax1.transAxes)
ax2.plot(time, y * 100.0)
ax2.set_xlim(0.0, tmax)
ax2.set_ylabel(r"$y(t)$ [cm]")
ax2.set_xlabel(r"$t$ [s]")
fig.tight_layout()
fig.show()
