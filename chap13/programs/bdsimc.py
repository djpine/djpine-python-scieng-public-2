import numpy as np
from scipy.constants import Boltzmann as kB
import numba
import yaml


spec = [("sim_steps", numba.int32),
        ("dt", numba.float64),
        ("x_min", numba.float64),
        ("x_width", numba.float64),
        ("pot_depth", numba.float64),
        ("G", numba.float64),
        ("x", numba.float64[:])]


@numba.experimental.jitclass(spec)
class BDsim:
    """Simulates vertical motion of Brownian particle."""

    def __init__(self, sim_steps, dt, x_min, x_width, pot_depth, G):
        self.sim_steps = sim_steps
        self.dt = dt
        self.x_min = x_min
        self.x_width = x_width
        self.pot_depth = pot_depth
        self.G = G
        self.x = np.zeros(self.sim_steps)

    def run_simulation(self, x0):
        self.x[0] = x0  # initial particle height
        for i in range(1, self.sim_steps):
            self.x[i] = self.x[i - 1] + self.dh(self.x[i - 1])

    def dh(self, xi):
        """
        x(t+dt) - x(t)
        """
        # Calculate dimensionless D
        denom = 1.0 + xi * (4.5 + 3.0 * xi)
        D = xi * (1.0 + 3.0 * xi) / denom
        # Calculate dD/dx
        dDdx = (1.0 + xi * (6.0 + 10.5 * xi)) / denom ** 2
        # Calcuate random displacement
        xrand = np.sqrt(2.0 * D * self.dt) * \
            np.random.standard_normal()
        # Return full displacement
        return (dDdx + D * self.F(xi)) * self.dt + xrand

    def F(self, xi):
        """
        Force from potentials on sphere = -dU/dx - G
        """
        ex = np.exp(-(xi - self.x_min) / self.x_width)
        return (2.0 * self.pot_depth /
                self.x_width) * (ex * (ex - 1.0)) - self.G


class read_params:
    """Reads simulation parameters from yaml file"""

    def __init__(self, yaml_data_file_name):
        # Open yaml file, read, and close
        fmeta = open(yaml_data_file_name + ".yaml", "r")
        meta = yaml.safe_load(fmeta)
        fmeta.close()
        # extract parameters read from yaml file
        self.temp_C = float(meta["temp_C"])
        self.temp_K = self.temp_C + 273.15
        self.kT = kB * self.temp_K  # [J] energy scale
        self.diameter = float(meta["diameter"])
        self.radius = 0.5 * self.diameter  # length scale
        self.viscosity = float(meta["viscosity"])
        self.D0 = self.kT / (6.0 * np.pi *
                             self.viscosity * self.radius)
        self.dt = float(meta["dt"])  # [s] time increment
        self.z_min_nm = float(meta['z_min_nm'])  # height of pot min
        self.z_width_nm = float(meta['z_width_nm'])  # pot width
        self.pot_depth_kT = float(meta['pot_depth_kT'])  # pot depth
        self.sim_steps = int(float(meta["sim_steps"]))
        self.density_sphere = float(meta["density_sphere"])
        self.density_fluid = float(meta["density_fluid"])
        self.g = float(meta["g"])
        volume = (4.0 / 3.0) * np.pi * self.radius ** 3
        self.delta_mg = (self.density_sphere -
                         self.density_fluid) * volume * self.g
        # Form dimensionless parameters needed for simulation
        self.dt_nd = self.dt * self.D0 / self.radius ** 2
        self.x_min = self.z_min_nm * 1.0e-9 / self.radius
        self.x_width = self.z_width_nm * 1.0e-9 / self.radius
        self.G = self.delta_mg * (self.radius / self.kT)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import time
    # Read in simultaion parameters from yaml file
    data_file_name = "sim_data01"
    param = read_params(data_file_name)
    # Initialixe particle height (x) array
    x_start = param.x_min

    # Do simulation: get dimensionless height x as a function of time
    sim01 = BDsim(param.sim_steps, param.dt_nd, param.x_min,
                  param.x_width, param.pot_depth_kT, param.G)
    start_pd = time.perf_counter()
    sim01.run_simulation(x_start)
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nrun time = {0:0.4g} seconds".format(runtime))

    # Save data to NumPy npy file
    start_pd = time.perf_counter()
    np.save(data_file_name + ".npy", sim01.x)
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
    h, be = np.histogram(sim01.x, bins=400, range=(0.0015, 0.02))
    # Make x array for histogram
    xb = 0.5 * (be[:-1] + be[1:])
    # Plot histogram
    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    ax.plot(xb * param.radius * 1e9, h / sim01.sim_steps)
    ax.set_xlabel("z [nm]")
    ax.set_ylabel("histogram of time at height")
    txt = f"Potential well depth = {param.pot_depth_kT:0.1f} kT"
    txt += "\n" + f"Potential well minimum = {param.z_min_nm:0.1f} nm"
    ax.text(0.98, 0.94, txt, va="top", ha="right",
            transform=ax.transAxes)
    ax.grid()
    ax.set_xlim(left=0.0)
    plt.show
