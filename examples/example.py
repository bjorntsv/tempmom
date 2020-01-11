# -*- coding: utf-8 -*-

"""
example.py

This script shows simple examples on how to utilize the tempmom python package.
The script is structured in the following way:

    1. Establishing a theoretical signal.
    2. Utilizing the tempmom.TemporalMomentsAll() class to establish an array
       of all temporal moments.

Note:
    - The tempmom.TemporalMoments() class can be utilized to establish
      individual temporal moments.
    - The tempmom.TemporalMoments().peak_value() is not a temporal moment, it
      simply finds the peak value of the signal considered.
"""

import numpy as np
import matplotlib.pyplot as plt
import tempmom

# -------------------- #
# EXAMPLE SIGNAL
# -------------------- #

# Variables
alpha = 20
s_freq = 2048
t = np.arange(0, 1, 1/s_freq)

# Signal
y = np.exp(-alpha*t)

# Plot signal
plt.figure(1, figsize=(6, 4))
plt.plot(t, y, color='black', linewidth=0.75)
plt.title('Exponential function as a signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# -------------------- #
# TEMPORAL MOMENTS
# -------------------- #

y_tempmom = tempmom.TemporalMomentsAll(data=y, fs=s_freq).full()

print('The signal peak value is ' + str(round(y_tempmom[0], 3)))
print('The signal energy is ' + str(round(y_tempmom[1], 6)))
print('The signal central time is ' + str(round(y_tempmom[2], 6)))
print('The signal ms duration is ' + str(round(y_tempmom[3], 6)))
print('The signal rms duration is ' + str(round(y_tempmom[4], 6)))
print('The signal central skewness is ' + str(round(y_tempmom[5], 6)))
print('The signal normalized skewness is ' + str(round(y_tempmom[6], 6)))
print('The signal central kurtosis is ' + str(round(y_tempmom[7], 6)))
print('The signal normalized kurtosis is ' + str(round(y_tempmom[8], 6)))
print('The signal root energy amplitude is ' + str(round(y_tempmom[9], 6)))
