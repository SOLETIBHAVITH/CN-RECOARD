# Experiment 9 - Local DNS Server Host Name and IP Address

Aim:

To list configured DNS resolver addresses and attempt reverse-DNS hostname lookup.

Algorithm:

1. On Windows, find active adapters and read their DNS server addresses using Get-DnsClientServerAddress.
2. On Linux, read nameserver entries from /etc/resolv.conf.
3. Remove duplicate addresses and display each configured resolver.
4. Attempt socket.gethostbyaddr for each resolver address.
5. Display the returned hostname or a reverse-DNS-unavailable message.

Program / Commands:

[Source: main.py](main.py)

```powershell
python main.py
```
Windows requires the built-in NetAdapter and DnsClient PowerShell modules. The program lists configured resolvers on active interfaces; it does not assume the computer's own hostname is a DNS server. VPN policy, adapter priority, encrypted DNS and stub resolvers can affect which upstream server actually handles a particular query. Reverse DNS may be absent. Keep actual resolver details outside the public repository.

Output / Observation:

Execution Status: Verified

Configured resolver retrieval and reverse-DNS attempts were executed on Windows. Actual addresses and hostnames are redacted; this is not the machine-hostname program from Experiment 2.

```text
DNS server IP: [redacted configured resolver address]
DNS server hostname: reverse DNS unavailable
DNS server IP: [redacted configured resolver address]
DNS server hostname: reverse DNS unavailable
DNS server IP: [redacted configured resolver address]
DNS server hostname: reverse DNS unavailable
DNS server IP: [redacted configured resolver address]
DNS server hostname: [redacted reverse-DNS hostname]
```
