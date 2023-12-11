import numpy as np
import matplotlib.pyplot as plt

def phase_modulation(message_signal, modulation_index, frequency_carrier, sampling_rate):
    time = np.arange(0, len(message_signal) / sampling_rate, 1 / sampling_rate)
    carrier_signal = np.cos(2 * np.pi * frequency_carrier * time)

    modulated_signal = np.cos(2 * np.pi * frequency_carrier * time + modulation_index * message_signal)

    return time, modulated_signal, carrier_signal

def plot_signals(time, message_signal, modulated_signal, carrier_signal):
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(time, message_signal, label='Message Signal')
    plt.title('Message Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time, carrier_signal, label='Carrier Signal')
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time, modulated_signal, label='PM Signal')
    plt.title('Phase Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    sampling_rate = 1000  # Hz
    frequency_carrier = 50  # Hz
    modulation_index = 1.0

    # Create a message signal (sinusoidal waveform)
    time = np.arange(0, 1, 1 / sampling_rate)
    message_frequency = 5  # Hz
    message_signal = np.sin(2 * np.pi * message_frequency * time)

    # Perform Phase Modulation
    time, modulated_signal, carrier_signal = phase_modulation(message_signal, modulation_index, frequency_carrier, sampling_rate)

    # Plot the signals
    plot_signals(time, message_signal, modulated_signal, carrier_signal)

if __name__ == "__main__":
    main()
