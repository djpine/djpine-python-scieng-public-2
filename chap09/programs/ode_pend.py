import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import seaborn as sns

def f(t, y, Q, d, Omega):
    theta, omega = y      # unpack current values of dep variables
    d_theta_dt = omega    # calculate derivatives
    d_omega_dt = -omega / Q - np.sin(theta) + d * np.cos(Omega * t)
    return d_theta_dt, d_omega_dt

# Parameters
Q = 2.0          # quality factor (inverse damping)
d = 1.091        # forcing amplitude
Omega = 0.67     # drive frequency

# Initial values
theta0 = 0.0     # initial angular displacement
omega0 = 0.0     # initial angular velocity

# Make time array for solution
t_start, t_stop = 0.0, 300.0

# Call the ODE solver
mthd = "Radau"
psoln = solve_ivp(f, [t_start, t_stop], [theta0, omega0],
                  args=(Q, d, Omega), method=mthd,
                  rtol=1e-8, atol=1e-10, dense_output=True)

# Calculate dense solution for plotting
t_increment = 0.1
t = np.arange(t_start, t_stop, t_increment)
z = psoln.sol(t)

# Plot results
fig = plt.figure(figsize=(9.5, 4.5))
c = sns.color_palette("icefire_r", 3)  # a Seaborn palette

# Plot theta as a function of time
ax1 = fig.add_subplot(221)
ax1.plot(t, z[0, :], color=c[0])
ax1.set_xlabel("time", fontsize=14)
ax1.set_ylabel(r"$\theta$", fontsize=14)
ax1.text(0.98, 0.98, "{0:s}".format(mthd), ha="right", va="top",
         transform=ax1.transAxes)

# Plot omega as a function of time
ax2 = fig.add_subplot(223)
ax2.plot(t, z[1, :], color=c[1])
ax2.set_xlabel("time", fontsize=14)
ax2.set_ylabel(r"$\omega$", fontsize=14)

# Plot omega vs theta
ax3 = fig.add_subplot(122)
pi, twopi = np.pi, 2.0 * np.pi
ax3.plot((z[0, :]), z[1, :], "-", ms=1, color=c[2])
ax3.set_xlabel(r"$\theta$", fontsize=14)
ax3.set_ylabel(r"$\omega$", fontsize=14)
ax3.axhline(lw=0.5, color="gray", zorder=-1)
ax3.axvline(lw=0.5, color="gray", zorder=-1)
fig.tight_layout()
fig.savefig("./figures/ode_pend.pdf")
plt.show()
