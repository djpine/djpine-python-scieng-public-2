import numpy as np
import time

a = np.linspace(0.0, 32.0, 10000000)  # 10 million
print(a)
startTime = time.process_time()
a = a * a
endTime = time.process_time()
print(a)
print(f"Run time = {endTime - startTime} seconds")
