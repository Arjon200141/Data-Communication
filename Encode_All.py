import matplotlib.pyplot as plt

def unipolar_encoding(binary_sequence):
    return [int(bit) for bit in binary_sequence]

def nrz_i_encoding(binary_sequence):
    nrz_i_output = []
    current_level = 1
    for bit in binary_sequence:
        if bit == '0':
            nrz_i_output.extend([current_level, current_level])
        else:
            current_level *= -1
            nrz_i_output.extend([current_level, current_level])
    return nrz_i_output

def nrz_l_encoding(binary_sequence):
    return [2 * int(bit) - 1 for bit in binary_sequence]

def rz_encoding(binary_sequence):
    rz_output = []
    for bit in binary_sequence:
        rz_output.extend([int(bit), 0])
    return rz_output

def manchester_encoding(binary_sequence):
    manchester_output = []
    for bit in binary_sequence:
        if bit == '0':
            manchester_output.extend([1, -1])
        else:
            manchester_output.extend([-1, 1])
    return manchester_output

def differential_manchester_encoding(binary_sequence):
    differential_manchester_output = []
    last_bit = '0'
    for bit in binary_sequence:
        if bit == '0':
            differential_manchester_output.extend([1, -1] if last_bit == '1' else [-1, 1])
        else:
            differential_manchester_output.extend([-1, 1] if last_bit == '1' else [1, -1])
        last_bit = bit
    return differential_manchester_output

def plot_waveform(encoding, title):
    plt.plot(encoding)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')


def main():
    binary_sequence = input("Enter a binary sequence: ")

    unipolar_output = unipolar_encoding(binary_sequence)
    nrz_i_output = nrz_i_encoding(binary_sequence)
    nrz_l_output = nrz_l_encoding(binary_sequence)
    rz_output = rz_encoding(binary_sequence)
    manchester_output = manchester_encoding(binary_sequence)
    differential_manchester_output = differential_manchester_encoding(binary_sequence)

    plot_waveform(unipolar_output, 'Unipolar Encoding')
    plot_waveform(nrz_i_output, 'NRZ-I Encoding')
    plot_waveform(nrz_l_output, 'NRZ-L Encoding')
    plot_waveform(rz_output, 'RZ Encoding')
    plot_waveform(manchester_output, 'Manchester Encoding')
    plot_waveform(differential_manchester_output, 'Differential Manchester Encoding')

    # Combine all figures in one page
    plt.figure()
    plt.subplot(3, 2, 1)
    plt.plot(unipolar_output)
    plt.title('Unipolar Encoding')

    plt.subplot(3, 2, 2)
    plt.plot(nrz_i_output)
    plt.title('NRZ-I Encoding')

    plt.subplot(3, 2, 3)
    plt.plot(nrz_l_output)
    plt.title('NRZ-L Encoding')

    plt.subplot(3, 2, 4)
    plt.plot(rz_output)
    plt.title('RZ Encoding')

    plt.subplot(3, 2, 5)
    plt.plot(manchester_output)
    plt.title('Manchester Encoding')

    plt.subplot(3, 2, 6)
    plt.plot(differential_manchester_output)
    plt.title('Differential Manchester Encoding')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
