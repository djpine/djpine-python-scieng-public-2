import numpy as np
import matplotlib.pyplot as plt
import yaml


class FallingBall:
    """
    A class to analyze data from falling ball experiment with air
    resistance
    """

    def __init__(self, filename):
        """Read data from & metadata from txt and yaml files"""
        self.filename = filename

        # open YAML file and read in metadata dictionary
        fmeta = open(filename + ".yaml", "r")
        self.meta = yaml.safe_load(fmeta)
        fmeta.close()

        # open text file and read in crossing times data
        self.crossing_times = np.loadtxt(filename + ".txt",
                                         unpack=True, delimiter=",")

        # determine initial velocity v0
        radius = self.meta["radius_cm"] / 100.0  # [m] ball radius
        y00 = self.meta["magnet_to_laser_cm"] / 100.0  # [m]
        g = self.meta["gravity_acceleration_si"]  # [m/s^2]
        mass = self.meta["mass_gm"] / 1000.0  # [kg]
        y0 = y00 - 2.0 * radius  # [m] fall to first laser
        self.v0 = np.sqrt(2.0 * g * y0)  # [m/s] initial velocity

        # determine terminal velocity vt
        cdrag = self.meta["drag_coefficient"]
        density_air = self.meta["density_air_si"]  # [kg/m^3]
        drag = 0.5 * cdrag * np.pi * radius**2 * density_air
        self.vt = np.sqrt(mass * g / drag)  # [m/s] terminal velocity

        # determine laser y-coordinates
        dy = self.meta["laser_spacing_cm"] / 100.0  # [m]
        nlines = self.crossing_times.size // 2
        self.y_laser = np.linspace(0.0, nlines-1, nlines) * dy

        # determine particle y-positions
        y2 = self.y_laser + 2.0 * radius
        yp = np.concatenate((self.y_laser, y2))
        self.yp = np.sort(yp)

        # determine ideal particle y-positions with no friction
        self.y_nofric = self.crossing_times * (self.v0 + 0.5 * g *
                                               self.crossing_times)

        # determine difference from ideal no-friction displacements
        self.dy = self.yp - self.y_nofric

        # determine uncertainties in difference displacements
        v = self.v0 + g * self.crossing_times
        self.dy_err = np.abs(v * self.meta["time_uncertainty_s"])

    def mdata(self):
        """Print out nicely-formatted metadata"""
        for key, value in self.meta.items():
            print(key + ": " + str(value))

    def plot(self, model=False, save=False):
        fig, ax = plt.subplots(figsize=(6.5, 4.0))
        ax.errorbar(self.crossing_times, 1.0e3 * self.dy, fmt="oC0",
                    yerr=1.0e3 * self.dy_err, ecolor="gray", ms=3)
        ax.axhline(color="gray", lw=0.5, zorder=-1)
        ax.set_xlabel(r"$t$ [s]")
        ax.set_ylabel(r"$y(t) - y_0(t)$ [mm]")
        txt = self.filename
        txt += "\n" + f"mass = {self.meta['mass_gm']:0.1f} gm"
        txt += "\n" + f"radius = {self.meta['radius_cm']:0.2f} cm"
        ax.text(0.02, 0.02, txt, ha="left", va="bottom",
                transform=ax.transAxes)
        if model:
            tmax = 1.05 * self.crossing_times[-1]
            tfit = np.linspace(0.0, tmax, 100)
            yfit = self.fall(tfit)  # [m]
            ax.plot(tfit, 1.0e3 * yfit, color="k", lw=0.5)
        if save:
            fig.savefig("figures/" + self.filename + ".pdf")
        fig.show()

    def fall(self, time):
        g = self.meta["gravity_acceleration_si"]
        t = g * time / self.vt
        a = np.log(np.cosh(t) + (self.v0 / self.vt) * np.sinh(t))
        y = (self.vt**2 / g) * a
        y_nodrag = self.v0 * time + 0.5 * g * time**2
        return y - y_nodrag


class Impedance:
    """
    A class to read & process data from an HP4194A impedence analyzer
    """

    def __init__(self, input_filename):
        """Read and format data & metadata from csv and yaml files"""
        self.input_filename = input_filename

        # open YAML file and read in metadata dictionary
        fmeta = open(input_filename + ".yaml", "r")
        self.meta = yaml.safe_load(fmeta)
        fmeta.close()

        # get numerical parameters from dictionary and cast to numbers
        self.freqlo = float(self.meta["start_frequency_Hz"])
        self.freqhi = float(self.meta["stop_frequency_Hz"])
        self.npoints = int(self.meta["number_of_points"])
        self.navgs = int(self.meta["number_of_averages"])

        # open CSV file and read in data from Impedance analyzer
        self.freq, self.ampl, self.phase = np.loadtxt(
            input_filename + ".csv",  unpack=True, delimiter=",")

    def mdata(self):
        """Print out metadata"""
        for key, value in self.meta.items():
            print(key + " : " + str(value))

    def get_data(self):
        """Return frequency, amplitude, phase of complex impedence"""
        return self.freq, self.ampl, self.phase

    def pmax(self):
        """Return frequency, amplitude, & phase of phase maximum"""
        imax = np.argmax(self.phase)
        return self.freq[imax], self.ampl[imax], self.phase[imax]

    def pmin(self):
        """Return frequency, amplitude, & phase of phase minimum"""
        imin = np.argmin(self.phase)
        return self.freq[imin], self.ampl[imin], self.phase[imin]

    def plot(self, save=False):
        """Plot amplitude & phase of complex impedence vs frequency"""
        fig, ax = plt.subplots(2, 1, figsize=(9.4, 7.5), sharex=True)
        ax[0].semilogx(self.freq, self.phase, marker="D", ms=3,
                       c="C1")
        ax[0].set_ylabel("phase (degrees)")
        ax[1].semilogx(self.freq, self.ampl, marker="o", ms=3, c="C0")
        ax[1].set_xlabel("frequency [Hz]")
        ax[1].set_ylabel("amplitude [ohms]")
        txt = r"$f_{{lo}}={0:0.2e}$ Hz".format(self.freqlo)
        txt += "\n" + r"$f_{{hi}}={0:0.2e}$ Hz".format(self.freqhi)
        txt += "\n" + "number of points = {0:d}".format(self.npoints)
        txt += "\n" + "number of averages = {0:d}".format(self.navgs)
        ax[0].text(0.02, 0.95, txt, ha="left", va="top",
                   transform=ax[0].transAxes)
        plt.subplots_adjust(hspace=0.07)
        if save is not False:
            plt.savefig(self.input_filename + ".pdf")
        plt.show()
