from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure(figsize=(8, 4))
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot([1, 3, 2, 4, 3, 5])
ax.set_title("A simple plot")
ax.grid(True)
ax.set_xlabel("time")
ax.set_ylabel("volts")
fig.savefig("figures/oop_test.pdf")
canvas.show()
