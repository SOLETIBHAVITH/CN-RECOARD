# Experiment 10 - CRC Error Detection

Aim:

To generate CRC check bits using modulo-2 division and detect corruption in a received codeword.

Algorithm:

1. Read and validate binary data and a generator polynomial beginning and ending with 1.
2. Append degree(generator) zero bits to the data.
3. Perform modulo-2 division using XOR and take the remainder.
4. Append the remainder to the data to form the transmitted codeword.
5. Read a received codeword, divide it and check for a zero remainder.
6. Flip one transmitted bit and demonstrate an error indication.

Program / Commands:

[Source: main.py](main.py)

```powershell
python main.py
```
Original syllabus: "Write a code for error correction code (like CRC)." CRC provides **error detection**, not automatic correction. A nonzero remainder detects corruption; a zero remainder means no error was detected, not proof that every possible error is absent.

Output / Observation:

Execution Status: Verified

The captured output below uses piped input. Input is not echoed, so some prompts share lines.

Sample inputs: data 1101011011; generator 10011; Enter to verify the transmitted word. The known remainder 1110, each possible single-bit corruption of the sample, independent polynomial division and invalid input handling were checked.

```text
Data bits: Generator bits: CRC remainder: 1110
Transmitted codeword: 11010110111110
Received codeword (Enter for transmitted codeword): Received check: No error detected
Single-bit corrupted codeword: 01010110111110
Corrupted check: Error detected
```
