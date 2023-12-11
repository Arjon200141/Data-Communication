import AM as np

def amplitude_modulation(carrier_frequency, modulation_index, message_signal, time):
    carrier_signal = np.cos(2 * np.pi * carrier_frequency * time)
    modulated_signal = (1 + modulation_index * message_signal) * carrier_signal
    return modulated_signal


def main():
    carrier_frequency = float(input("Enter carrier frequency: "))
    modulation_index = float(input("Enter modulation index: "))

    # Time vector
    fs = 1000  # Sampling frequency
    t = 1  # seconds
    time = np.linspace(0, t, t * fs, endpoint=False)

    # Generating a simple message signal (sine wave)
    frequency = float(input("Enter message signal frequency: "))
    message_signal = np.sin(2 * np.pi * frequency * time)

    # Modulation
    am_signal = amplitude_modulation(carrier_frequency, modulation_index, message_signal, time)

    print("Amplitude Modulated signal:", am_signal)


if __name__ == "__main__":
    main()
