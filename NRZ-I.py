def nrz_i_encoding(bits):
    encoded_signal = []
    prev_bit = 1
    for bit in bits:
        if bit == '1':
            prev_bit = -prev_bit
        encoded_signal.append(prev_bit)
    return encoded_signal


def main():
    binary_input = input("Enter binary input: ")

    nrz_i_signal = nrz_i_encoding(binary_input)

    print("NRZ-I encoding:", nrz_i_signal)


if __name__ == "__main__":
    main()
