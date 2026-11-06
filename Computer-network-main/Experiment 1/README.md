# Experiment 1 - Network Commands and Packet Capture

Aim:

To use basic network commands and examine ping and traceroute protocol data units with a packet analyzer.

Procedure:

1. Work on your own computer and select only an authorized test interface and destination.
2. Run the Windows commands below and identify adapter, connection, DNS and route information locally.
3. In Wireshark with Npcap, select its loopback adapter for loopback ping, or the actual authorized adapter for external probes.
4. Apply capture filter `icmp`, start capture, run ping and tracert, then stop capture promptly.
5. Apply display filter `icmp.type == 8 || icmp.type == 0`. Inspect source/destination IPs, echo type, identifier and sequence number to pair requests and replies.
6. Apply `icmp.type == 11` for TTL-exceeded messages from intermediate routers. Expand the quoted original IP header to identify the probe that expired. A loopback trace has no intermediate router, so it does not demonstrate this event.
7. For the Linux UDP traceroute procedure, capture ICMP plus the UDP probe port range and examine TTL-exceeded and final destination-unreachable responses.
8. Keep only redacted observations in the record; do not publish local adapter details or private captures.

Program / Commands:

Windows PowerShell or Command Prompt:

```powershell
ipconfig /all
netstat -ano
nslookup example.com
ping -n 2 127.0.0.1
tracert -d -h 3 -w 250 127.0.0.1
# To study real hops, use an authorized reachable destination:
tracert -d -h 5 -w 500 example.com
```

`ipconfig` shows Windows adapter configuration. `netstat` lists connections/listeners; `-a`, `-n`, `-o` request all endpoints, numeric addresses and PIDs. `nslookup` queries DNS. Windows `tracert` uses increasing-TTL ICMP echo probes. Timeouts do not prove that a hop is down; a device may filter probes or replies.

Linux/WSL with networking tools installed:

```bash
ifconfig
netstat -an
nslookup example.com
ping -c 2 127.0.0.1
traceroute -n -m 5 example.com
# In a separate terminal, capture authorized loopback ping:
sudo tcpdump -i lo -nn 'icmp'
```

For a common Linux UDP traceroute implementation, replace `INTERFACE` with the authorized interface name and stop capture with Ctrl+C:

```bash
sudo tcpdump -i INTERFACE -nn 'icmp or (udp portrange 33434-33534)'
```

The usual UDP traceroute sends probes to increasing high UDP ports; routers return ICMP Time Exceeded and the destination may return ICMP Port Unreachable. Implementations/options can select other probe types. The filter covers the documented short trace, not every possible traceroute implementation or port range.

`tcpdump` is a packet-capture utility; `ifconfig` is a legacy Linux interface utility, often supplied by net-tools. Neither is a native equivalent command spelling for `ipconfig`. Linux tools may need installation in WSL/Linux and capture privileges; WSL sees its own networking environment. Windows and Linux command flags are not interchangeable.

Output / Observation:

Execution Status: Partially Verified

Windows ipconfig /all, netstat -ano, nslookup example.com, ping and loopback tracert ran successfully. Adapter, connection, DNS and route identifiers are intentionally omitted from this public record.

Actual loopback output:

```text

Pinging 127.0.0.1 with 32 bytes of data:
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128

Ping statistics for 127.0.0.1:
    Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms


Tracing route to 127.0.0.1 over a maximum of 3 hops

  1    <1 ms    <1 ms    <1 ms  127.0.0.1

Trace complete.
```

Live packet capture and PDU inspection were not verified because Wireshark/Npcap was unavailable. Linux tcpdump, ifconfig and traceroute were not executed; no configured Linux/WSL distribution was present. A one-hop loopback trace does not demonstrate intermediate TTL-expired replies.

References: [Microsoft tracert](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert), [tcpdump manual](https://www.tcpdump.org/manpages/tcpdump.1.html).
