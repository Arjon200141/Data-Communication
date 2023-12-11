import numpy as np
import matplotlib.pyplot as plt

def amplitude_modulation(message_signal, carrier_frequency, modulation_index, time):
    # Modulate the message signal using AM formula
    modulation_signal = (1 + modulation_index * np.sin(2 * np.pi * carrier_frequency * time)) * message_signal
    return modulation_signal

def main():
    # Set parameters
    message_frequency = 1  # Frequency of the message signal
    carrier_frequency = 10  # Frequency of the carrier signal
    modulation_index = 1  # Modulation index

    # Set time values
    sampling_rate = 1000
    time = np.arange(0, 1, 1/sampling_rate)

    # Generate message signal (e.g., a sinusoidal signal)
    message_signal = np.sin(2 * np.pi * message_frequency * time)

    # Generate modulated signal
    modulated_signal = amplitude_modulation(message_signal, carrier_frequency, modulation_index, time)

    # Plot original message signal
    plt.subplot(3, 1, 1)
    plt.plot(time, message_signal)
    plt.title('Message Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # Plot carrier signal
    plt.subplot(3, 1, 2)
    carrier_signal = np.sin(2 * np.pi * carrier_frequency * time)
    plt.plot(time, carrier_signal)
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # Plot modulated signal
    plt.subplot(3, 1, 3)
    plt.plot(time, modulated_signal)
    plt.title('Amplitude Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # Adjust layout for better visualization
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
