def nrz_i_encoding(bits):
    encoded_signal = []
    prev_bit = 1
    for bit in bits:
        if bit == '1':
            prev_bit = -prev_bit
        encoded_signal.append(prev_bit)
    return encoded_signal


def nrz_l_encoding(bits):
    return [int(bit) * 2 - 1 for bit in bits]


def rz_encoding(bits):
    return [int(bit) if bit == '1' else 0 for bit in bits]


def manchester_encoding(bits):
    encoded_signal = []
    for bit in bits:
        if bit == '0':
            encoded_signal.extend([-1, 1])
        else:
            encoded_signal.extend([1, -1])
    return encoded_signal


def differential_manchester_encoding(bits):
    encoded_signal = []
    state = 1
    for bit in bits:
        if bit == '0':
            state = -state
        encoded_signal.extend([state, -state])
    return encoded_signal


def display_signal(signal, encoding_name):
    print(f"{encoding_name} encoding: {signal}")


def main():
    binary_input = input("Enter binary input: ")

    nrz_i_signal = nrz_i_encoding(binary_input)
    display_signal(nrz_i_signal, "NRZ-I")

    nrz_l_signal = nrz_l_encoding(binary_input)
    display_signal(nrz_l_signal, "NRZ-L")

    rz_signal = rz_encoding(binary_input)
    display_signal(rz_signal, "RZ")

    manchester_signal = manchester_encoding(binary_input)
    display_signal(manchester_signal, "Manchester")

    diff_manchester_signal = differential_manchester_encoding(binary_input)
    display_signal(diff_manchester_signal, "Differential Manchester")


if __name__ == "__main__":
    main()
