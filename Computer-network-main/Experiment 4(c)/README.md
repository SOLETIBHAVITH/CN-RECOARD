# Experiment 4(c) - File Transfer Using TCP Sockets

Aim:

To transfer a binary file over a TCP connection and confirm receipt.

Algorithm:

1. Select an existing local file through the server command-line argument.
2. Start the server on loopback port 31003 and accept a client.
3. Send an eight-byte unsigned big-endian file length followed by exactly that many bytes.
4. Read the complete length header and receive the data in a loop.
5. Save bytes to a new output file, then acknowledge completion with K.
6. Display byte counts and close all files and sockets.

Program / Commands:

[Server](server.py) | [Client](client.py)

```powershell
# Terminal 1: choose an existing, non-sensitive local sample
python server.py "C:\path\to\sample.bin"
# Terminal 2: choose a new output filename
python client.py received.bin
```
The length header gives a clear end-of-file condition, including for empty files. Both header and data can arrive over many receives. Existing output files are preserved. A failed transfer may leave a partial new file; discard it before retrying. The sample source must remain unchanged during transfer. The acknowledgement confirms the byte count, not a cryptographic integrity check.

Output / Observation:

Execution Status: Verified

A binary sample containing every byte value and a NUL was transferred. Source and destination bytes and SHA-256 matched (0dfa2c3bcc0994686de4632299053404ba070c4e314e2e039b0b4b2fd931a3eb). No sample or transferred copy is committed.

```text
Server:
File server ready on localhost:31003
Sent bytes: 8197
Client confirmed complete transfer

Client:
Received bytes: 8197
Saved: received.bin
```
