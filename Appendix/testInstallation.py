""" Checks Python installation and generates a pdf image file that
    reports the versions of Python and selected installed packages.
    Students can sent output file to instructor."""
import scipy, numpy, matplotlib, pandas, datetime, platform, sys
import matplotlib.pyplot as plt

# If you are a student, please fill in your first and last names
# inside the single quotes in the two lines below. You do not need to
# modify anything else in this file.
student_first_name = 'Gisele'
student_last_name = 'Sparks'
# If you are an instructor, modify the text between the double quotes
# on the next 3 lines. You do not need to  modify anything else in
# this file.
classname = "Quantum Mechanics I"
term = "Fall_2024"  # must contain no spaces
email = "instructor@abcu.edu"
timestamp = datetime.datetime.now()
tm = "{0:s}".format(timestamp.strftime("%Y-%m-%d %H:%M"))
plt.figure(figsize=(8, 6))
plt.plot([0, 1], "C0", [1, 0], 'C1')
plt.text(0.5, 1.0, "{0:s} {1:s}\n{2:s}\n{3:s}"
         .format(student_first_name, student_last_name, classname,
                 term),
         ha="center", va="top", size='x-large',
         bbox=dict(facecolor="C2", alpha=0.4))
plt.text(0.5, 0.7, "Python {0:s}".format(platform.python_version()),
         ha="center", va="top", size="large")
pkgstr = "scipy: {0:s}\nnumpy {1:s}\nmatplotlib: {2:s}"
pkgstr += "\nmatplotlib backend: {3:s}\npandas: {4:s}"
pkgstr += "\nPlatform: {5:s}\nSystem: {6:s}"
pkgstr += "\n{7:s}"
plt.text(0.5, 0.4, pkgstr.format(scipy.__version__,
         numpy.__version__, matplotlib.__version__,
         matplotlib.get_backend(), pandas.__version__,
         platform.platform(), sys.version, tm),
         ha="center", va="top", color="C5")
filename = student_last_name + "_" + student_first_name
filename += "_" + term + ".pdf"
ttlstr = "This plot has been saved on your computer as"
ttlstr += "\n'{0:s}'\nE-mail this file to '{1:s}'"
plt.title(ttlstr.format(filename, email), fontsize=10)
plt.savefig(filename)
plt.show()
