import numpy as np
import matplotlib.pyplot as plt

def generate_fm_signal(message_signal, modulation_index, frequency_deviation, sampling_rate):
    time = np.arange(0, len(message_signal) / sampling_rate, 1 / sampling_rate)

    # Generate the FM signal
    fm_signal = np.sin(2 * np.pi * time * frequency_deviation * np.sin(2 * np.pi * time * message_signal))

    return time, fm_signal

def main():
    # Parameters
    sampling_rate = 1000  # Hz
    duration = 1  # seconds
    frequency_message = 5  # Hz
    modulation_index = 2
    frequency_deviation = 50  # Hz

    # Generate a simple message signal (sine wave)
    time_message = np.arange(0, duration, 1 / sampling_rate)
    message_signal = np.sin(2 * np.pi * frequency_message * time_message)

    # Generate FM signal
    time_fm, fm_signal = generate_fm_signal(message_signal, modulation_index, frequency_deviation, sampling_rate)

    # Plot the original message signal
    plt.subplot(2, 1, 1)
    plt.plot(time_message, message_signal)
    plt.title('Message Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Plot the FM signal
    plt.subplot(2, 1, 2)
    plt.plot(time_fm, fm_signal)
    plt.title('Frequency Modulation (FM) Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
