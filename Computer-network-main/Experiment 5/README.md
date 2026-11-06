# Experiment 5 - ARP and RARP Protocol Simulation

Aim:

To simulate IP-to-MAC and MAC-to-IP address lookups using a small address table.

Algorithm:

1. Store two documentation IP addresses and locally administered sample MAC addresses.
2. Read an IP address and look up its MAC address.
3. Create a reversed table, read a MAC address and look up its IP address.
4. Display a matched address or Address not found.

Program / Commands:

[Source: main.py](main.py)

```powershell
python main.py
```
This is an in-memory simulation only. ARP normally maps IPv4 addresses to local-link hardware addresses. RARP is a legacy method for obtaining an IP address from a hardware address. No packets are injected and no local address cache is changed.

Output / Observation:

Execution Status: Verified

The captured output below uses piped input. Input is not echoed, so some prompts share lines.

Successful ARP/RARP lookups and missing addresses were tested. Only artificial documentation addresses were used.

```text
ARP - enter IP address: MAC address: 02:00:00:00:00:01
RARP - enter MAC address: IP address: 192.0.2.11

Unknown-address test:
ARP - enter IP address: MAC address: Address not found
RARP - enter MAC address: IP address: Address not found
```
