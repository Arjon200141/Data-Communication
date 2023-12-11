def nrz_l_encoding(bits):
    return [int(bit) * 2 - 1 for bit in bits]


def main():
    binary_input = input("Enter binary input: ")

    nrz_l_signal = nrz_l_encoding(binary_input)

    print("NRZ-L encoding:", nrz_l_signal)


if __name__ == "__main__":
    main()
