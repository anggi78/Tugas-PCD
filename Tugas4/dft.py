import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, endpoint=False)
y = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

N = len(y)
Y = np.zeros(N, dtype=np.complex_)
for k in range(N):
    for n in range(N):
        Y[k] += y[n] * np.exp(-2j * np.pi * k * n / N)

freqs = np.arange(N)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, y)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[1].plot(freqs, np.abs(Y))
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Magnitude')
plt.show()
