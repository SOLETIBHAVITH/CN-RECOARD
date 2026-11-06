# Experiment 2 - Identifying Host Name and IP Address

Aim:

To obtain the executing computer's hostname and IPv4 address using the socket library.

Algorithm:

1. Read the hostname using socket.gethostname.
2. Resolve that hostname using socket.gethostbyname.
3. Display both values, or report a lookup error.

Program / Commands:

[Source: main.py](main.py)

```powershell
python main.py
```
A computer can have several interfaces; this prints one address returned for its hostname, not necessarily its public Internet address.

Output / Observation:

Execution Status: Verified

Executed successfully on Windows. Bracketed values are intentional redactions of actual environment identifiers, not sample measurements. The program itself prints the real values.

```text
Host name: [redacted local hostname]
IP address: [redacted local IPv4 address]
```
