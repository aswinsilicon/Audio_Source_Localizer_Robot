import numpy as np
from scipy.signal import firwin, lfilter
import matplotlib.pyplot as plt

# Filter parameters
fs = 44100  # Sampling frequency (Hz)
lowcut = 300     # Lower cutoff frequency (Hz)
highcut = 3000   # Upper cutoff frequency (Hz)
numtaps = 128    # Number of filter coefficients (odd number preferred)

# Design FIR bandpass filter
coeffs = firwin(numtaps, [lowcut, highcut], pass_zero=False, fs=fs, window='hamming')

# Take FFT of coeffs
fft_coeffs = np.fft.fft(coeffs)

# Extract real and imaginary parts
real_coeffs = np.real(fft_coeffs)
imag_coeffs = np.imag(fft_coeffs)

# Print real values as a C array declaration
print("static const double hreal[",numtaps,"] = {")
print(", ".join(map(str, real_coeffs)))
print("};")

# Print imaginary values as a C array declaration
print("\nstatic const double himag[",numtaps,"] = {")
print(", ".join(map(str, imag_coeffs)))
print("};")