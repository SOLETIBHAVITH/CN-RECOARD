def binary(value):
    return bool(value) and all(bit in "01" for bit in value)


def remainder(bits, generator):
    work = [int(bit) for bit in bits]
    divisor = [int(bit) for bit in generator]
    for start in range(len(work) - len(divisor) + 1):
        if work[start] == 1:
            for offset in range(len(divisor)):
                work[start + offset] ^= divisor[offset]
    return "".join(str(bit) for bit in work[-(len(generator) - 1):])


def main():
    data = input("Data bits: ").strip()
    generator = input("Generator bits: ").strip()
    if not binary(data) or not binary(generator) or len(generator) < 2:
        print("Enter nonempty binary data and a generator of at least two bits.")
        return
    if generator[0] != "1" or generator[-1] != "1":
        print("The generator must start and end with 1.")
        return
    crc = remainder(data + "0" * (len(generator) - 1), generator)
    codeword = data + crc
    print("CRC remainder:", crc)
    print("Transmitted codeword:", codeword)
    received = input("Received codeword (Enter for transmitted codeword): ").strip() or codeword
    if not binary(received) or len(received) != len(codeword):
        print("Received codeword must contain the same number of binary bits.")
        return
    print("Received check:", "No error detected" if "1" not in remainder(received, generator)
          else "Error detected")
    damaged = ("1" if codeword[0] == "0" else "0") + codeword[1:]
    print("Single-bit corrupted codeword:", damaged)
    print("Corrupted check:", "Error detected" if "1" in remainder(damaged, generator)
          else "No error detected")


if __name__ == "__main__":
    main()
