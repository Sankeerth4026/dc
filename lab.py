import numpy as np
import matplotlib.pyplot as plt

# Input parameters
n = int(input('Enter n value for N-bit PCM system: '))      # Bits per sample
n1 = int(input('Enter number of samples in a period: '))    # Samples per period

# Derived parameters
L = 2 ** n                              # Number of quantization levels
x = np.arange(0, 4 * np.pi, 2 * np.pi / n1)  # Time vector
s = 8 * np.sin(x)                       # Analog input signal

# Step 1: Plot analog signal
#plt.figure(figsize=(10, 12))
plt.subplot(4, 1, 1)
plt.plot(s, linewidth=1.5)
plt.title('Analog Signal')
plt.ylabel('Amplitude')
plt.xlabel('Sample Index')
plt.grid(True)

# ...existing code...

# Step 2: Sampling (already discrete)
plt.subplot(4, 1, 2)
plt.stem(s, basefmt=" ")
plt.title('Sampled Signal')
plt.ylabel('Amplitude')
plt.xlabel('Sample Index')
plt.grid(True)

# Step 3: Quantization
vmax = 8
vmin = -vmax
delta = (vmax - vmin) / L                  # Quantization step size
partition = np.arange(vmin, vmax + delta, delta)  # Partition levels
codebook = np.arange(vmin + delta / 2, vmax, delta)  # Codebook levels

# Manual quantization
q = np.zeros_like(s)
index = np.zeros_like(s, dtype=int)
for i in range(len(s)):
    if s[i] >= vmax:
        q[i] = vmax - delta / 2
        index[i] = L - 1
    elif s[i] <= vmin:
        q[i] = vmin + delta / 2
        index[i] = 0
    else:
        index[i] = int(np.floor((s[i] - vmin) / delta))
        q[i] = vmin + (index[i] + 0.5) * delta

plt.subplot(4, 1, 3)
plt.stem(q, basefmt=" ")
plt.title('Quantized Signal')
plt.ylabel('Amplitude')
plt.xlabel('Sample Index')
plt.grid(True)

# Step 4: Encoding (decimal → binary)
code = np.zeros((len(index), n), dtype=int)
for i in range(len(index)):
    b = np.array(list(np.binary_repr(index[i], width=n)), dtype=int)
    code[i, :] = b

# Create encoded bitstream
bit_stream = code.flatten()

plt.subplot(4, 1, 4)
plt.step(np.arange(len(bit_stream)), bit_stream, where='mid', linewidth=1.5)
plt.ylim(-0.5, 1.5)
plt.title('PCM Encoded Bit Stream')
plt.ylabel('Binary Value')
plt.xlabel('Bit Index')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Decoding (binary → decimal → amplitude)
decoded_matrix = bit_stream.reshape(-1, n)
decoded_index = np.array([int("".join(str(bit) for bit in row), 2) for row in decoded_matrix])
q_reconstructed = vmin + (decoded_index + 0.5) * delta

plt.figure(figsize=(8, 4))
plt.plot(q_reconstructed, linewidth=1.5)
plt.title('Reconstructed Signal after Decoding')
plt.ylabel('Amplitude')
plt.xlabel('Sample Index')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Error and SNR Calculation
MSE = np.mean((s - q_reconstructed) ** 2)
signal_power = np.mean(s ** 2)
SNR = 10 * np.log10(signal_power / MSE)

print('\n--- PCM System Analysis ---')
print(f'Quantization Step Size (Δ): {delta:.4f}')
print(f'Mean Square Error (MSE): {MSE:.4f}')
print(f'Signal Power: {signal_power:.4f}')
print(f'Signal-to-Noise Ratio (SNR): {SNR:.2f} dB')