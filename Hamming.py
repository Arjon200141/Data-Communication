def hamming_encode(data):
    # Calculate the number of parity bits
    m = len(data)
    r = 1
    while 2**r < m + r + 1:
        r += 1

    # Create the encoded data array
    encoded_data = [0] * (m + r)
    j = 0

    # Fill in the data bits in their positions (powers of 2 are reserved for parity bits)
    for i in range(1, m + r + 1):
        if i & (i - 1) != 0:  # Skip powers of 2
            encoded_data[i - 1] = int(data[j])
            j += 1

    # Calculate the parity bits
    for i in range(r):
        index = 2**i - 1
        parity = 0
        for j in range(index, m + r, 2**(i + 1)):
            parity ^= encoded_data[j]
        encoded_data[index] = parity

    return encoded_data

def hamming_decode(received_data):
    # Calculate the number of parity bits
    n = len(received_data)
    r = 1
    while 2**r < n + r + 1:
        r += 1

    # Initialize the error positions and syndrome
    error_positions = 0
    syndrome = 0

    # Calculate the syndrome and identify error positions
    for i in range(r):
        parity = 0
        for j in range(2**i - 1, n, 2**(i + 1)):
            parity ^= received_data[j]
        syndrome += parity * 2**i
        error_positions += parity * (2**i)

    # Correct the error, if any
    if syndrome != 0:
        corrected_bit = error_positions
        received_data[corrected_bit] = 1 - received_data[corrected_bit]

    # Extract the original data
    decoded_data = []
    for i in range(1, n + 1):
        if i & (i - 1) != 0:  # Skip powers of 2
            decoded_data.append(received_data[i - 1])

    return decoded_data

def main():
    data = input("Enter 4 bits of data: ")

    # Ensure that the input is a 4-bit binary number
    if len(data) != 4 or not all(bit in "01" for bit in data):
        print("Invalid input. Please enter a 4-bit binary number.")
        return

    data_bits = [int(bit) for bit in data]

    # Encode the data
    encoded_data = hamming_encode(data_bits)
    print("Encoded Data:", encoded_data)

    # Introduce a simulated error
    error_position = 3
    encoded_data[error_position - 1] = 1 - encoded_data[error_position - 1]
    print("Simulated Error at Position", error_position, ":", encoded_data)

    # Decode the data
    decoded_data = hamming_decode(encoded_data)
    print("Decoded Data:", decoded_data)

if __name__ == "__main__":
    main()
