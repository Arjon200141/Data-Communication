import numpy as np
import matplotlib.pyplot as plt

def amplitude_modulation(message_signal,career_frequency,modulation_index,time):
    modulation_signal=(1 + modulation_index * np.sin(2*np.pi*career_frequency*time)*message_signal)
    return modulation_signal

def main():
    message_frequency = 1
    career_frequency = 10
    modulation_index = 1

    sampling_rate = 1000
    time = np.arange(0,1,1/sampling_rate)

    message_signal =np.sin( 2 * np.pi * message_frequency * time )

    modulated_signal = amplitude_modulation(message_signal,career_frequency,modulation_index,time)

    plt.subplot(3,1,1)
    plt.plot(time , message_signal)
    plt.title('Message Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('Time')

    plt.subplot(3, 1, 2)
    career_signal =np.sin( 2 * np.pi * career_frequency * time )
    plt.title('Career Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('Time')

    plt.subplot(3, 1, 3)
    plt.plot(time , modulated_signal)
    plt.title('Amplitude Modulated Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('Time')

    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()