import numpy as np
dataPt, time, height, error = np.loadtxt("mydata.txt", skiprows=5,
                                         unpack=True)
np.savetxt("mydataout.txt",
           list(zip(dataPt, time, height, error)),
           fmt="%12d %10.2f %12.0f %12.1f")

np.savetxt('mydataout.csv',
           list(zip(dataPt, time, height, error)),
           fmt="%0.1f", delimiter=",")
