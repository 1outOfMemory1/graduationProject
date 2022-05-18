import math

import tensorflow as tf

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import tensorflow.keras
import warnings
from scipy.fftpack import fft

x = np.arange(0, 10, 0.01)
y = fft([math.sin(2 * np.pi * ele) for ele in x])
y = abs(y)
y = y[x.shape[0] //2:]
plt.plot(y)
plt.show()
print(x.shape)
