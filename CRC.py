def crc_encode(data, divisor):
    data = list(map(int, data))
    divisor = list(map(int, divisor))

    # Append zeros to the data to match the length of the divisor
    data += [0] * (len(divisor) - 1)

    # Perform CRC division
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == 1:
            for j in range(len(divisor)):
                data[i + j] ^= divisor[j]

    # Return the CRC-encoded message
    return data[-(len(divisor) - 1):]

def crc_check(encoded_data, divisor):
    encoded_data = list(map(int, encoded_data))
    divisor = list(map(int, divisor))

    # Perform CRC division
    for i in range(len(encoded_data) - len(divisor) + 1):
        if encoded_data[i] == 1:
            for j in range(len(divisor)):
                encoded_data[i + j] ^= divisor[j]

    # If remainder is all zeros, no error
    return sum(encoded_data) == 0

def main():
    # User input for data bits and CRC divisor
    data = input("Enter data bits (e.g., 110110): ")
    divisor = input("Enter CRC divisor (e.g., 1011): ")

    # CRC encoding
    encoded_data = crc_encode(data, divisor)
    print(f"CRC-encoded data: {data + ''.join(map(str, encoded_data))}")

    # Simulate transmission (you can introduce errors here)
    received_data = input("Enter received data: ")

    # CRC checking
    if crc_check(received_data, divisor):
        print("No error detected. Data is correct.")
    else:
        print("Error detected in the received data.")

if __name__ == "__main__":
    main()
