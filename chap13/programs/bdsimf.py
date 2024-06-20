import numpy as np
import numba
from scipy.constants import Boltzmann as kB
import yaml


@numba.jit(nopython=True)
def run_simulation(sim_steps, x0):
    x = np.zeros(sim_steps, dtype=np.float64)
    x[0] = x0  # initial particle height
    for i in range(1, sim_steps):
        x[i] = x[i - 1] + dh(x[i - 1])
    return x


@numba.jit(nopython=True)
def dh(xi):
    """
    x(t+dt) - x(t)
    """
    # Calculate dimensionless D
    denom = 1.0 + xi * (4.5 + 3.0 * xi)
    D = xi * (1.0 + 3.0 * xi) / denom
    # Calculate dD/dx
    dDdx = (1.0 + xi * (6.0 + 10.5 * xi)) / denom ** 2
    # Calcuate random displacement
    xrand = np.sqrt(2.0 * D * dt) * np.random.standard_normal()
    # Return full displacement
    return (dDdx + D * F(xi)) * dt + xrand


@numba.jit(nopython=True)
def F(xi):
    """
    Force from potentials on sphere = -dU/dx - G
    """
    ex = np.exp(-(xi - x_min) / x_width)
    return (2.0 * pot_depth / x_width) * (ex * (ex - 1.0)) - G


def read_params(yaml_data_file_name):
    """Reads simulation parameters from yaml file"""
    # Open yaml file, read, and close
    fmeta = open(yaml_data_file_name, "r")
    meta = yaml.safe_load(fmeta)
    fmeta.close()
    # extract parameters read from yaml file
    temp_C = float(meta["temp_C"])
    temp_K = temp_C + 273.15
    kT = kB * temp_K  # energy scale
    diameter = float(meta["diameter"])
    radius = 0.5 * diameter  # length scale
    viscosity = float(meta["viscosity"])
    D0 = kT / (6.0 * np.pi * viscosity * radius)

    dt = float(meta["dt"]) * (D0 / radius ** 2)  # dimensionless time
    x_min = float(meta['z_min_nm']) * 1.0e-9 / radius  # ht of pot min
    x_width = float(meta['z_width_nm']) * 1.0e-9 / radius  # pot width
    pot_depth = float(meta['pot_depth_kT'])  # pot depth

    density_sphere = float(meta["density_sphere"])
    density_fluid = float(meta["density_fluid"])
    volume = (4.0 / 3.0) * np.pi * radius ** 3
    g = float(meta["g"])
    G = (density_sphere - density_fluid) * volume * g * (radius / kT)
    sim_steps = int(float(meta["sim_steps"]))
    return sim_steps, dt, x_min, x_width, pot_depth, G


if __name__ == "__main__":
    import time
    # Read in simultaion parameters from yaml file
    data_file_name = "sim_data01"
    sim_steps, dt, x_min, x_width, pot_depth, G = read_params(
        data_file_name + ".yaml")
    # Initialixe particle height (x) array
    x_start = x_min

    # Do simulation: get height x as a function of time
    for i in range(2):
        start_pd = time.perf_counter()
        x = run_simulation(sim_steps, x_start)
        end_pd = time.perf_counter()
        runtime = end_pd - start_pd
        print("\nrun time = {0:0.4g} seconds".format(runtime))

    # Save data to NumPy npy file
    start_pd = time.perf_counter()
    np.save(data_file_name + ".npy", x)
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nsave npy time = {0:0.4g} seconds".format(runtime))

    # Read data from NumPy npy file
    start_pd = time.perf_counter()
    y = np.load(data_file_name + ".npy")
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nload npy time = {0:0.4g} seconds".format(runtime))

    # Calculate histogram of displacements
    import matplotlib.pyplot as plt
    h, be = np.histogram(x, bins=400, range=(0.0015, 0.05))
    xb = 0.5 * (be[:-1] + be[1:])
    plt.plot(xb, h)
    plt.grid()
    plt.show
