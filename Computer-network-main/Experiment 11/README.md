# Experiment 11 - Wireshark Filter Expressions for Packet Capture

Aim:

To distinguish capture filters from display filters and select common network protocols and endpoints.

Procedure:

1. Open Wireshark and choose an authorized interface, or open an authorized existing capture.
2. Before capture, enter a capture expression in Capture Options. It limits which packets are recorded.
3. Capture only the required test traffic and stop promptly.
4. Enter a display expression in the display-filter toolbar to inspect packets already recorded. This hides packets without removing them from the capture.
5. Inspect the selected packet's IP addresses, ports and protocol details to confirm each filter's meaning.
6. Clear one filter before testing the next. Retain only redacted observations.

Program / Commands:

The addresses below are documentation examples, not observed local addresses. Replace them with an authorized test peer when applying the filters.

| Select | Capture filter (libpcap/BPF) | Display filter | Meaning |
|---|---|---|---|
| TCP | `tcp` | `tcp` | TCP packets |
| UDP | `udp` | `udp` | UDP packets |
| IPv4 ICMP | `icmp` | `icmp` | IPv4 ICMP messages |
| IPv6 ICMP | `icmp6` | `icmpv6` | IPv6 ICMP messages |
| Conventional DNS | `udp port 53 or tcp port 53` | `dns` | Port-based DNS capture versus decoded DNS display |
| Plain HTTP candidate traffic | `tcp port 80` | `http` | TCP port 80 capture versus decoded HTTP display |
| IPv4 address | `ip host 192.0.2.10` | `ip.addr == 192.0.2.10` | Either IPv4 endpoint matches |
| IPv4 source | `ip src host 192.0.2.10` | `ip.src == 192.0.2.10` | Source IPv4 address matches |
| IPv4 destination | `ip dst host 192.0.2.10` | `ip.dst == 192.0.2.10` | Destination IPv4 address matches |
| TCP port | `tcp port 31001` | `tcp.port == 31001` | Either TCP port matches |
| UDP destination port | `udp dst port 5004` | `udp.dstport == 5004` | UDP destination port matches |

Capture filters are not display filters: do not paste `ip.addr == ...` into the capture-filter box. BPF port filters do not verify the application protocol. HTTP can use other ports; encrypted HTTPS payloads are not ordinary `http` without decryption. DNS over encrypted transports is not selected as decoded DNS merely by port 53. Use `ipv6.addr`, `ipv6.src` and `ipv6.dst` for IPv6 address display filters.

Output / Observation:

**Execution Status: Not Verified**

Wireshark/TShark and a capture driver were not available. The expressions were checked against official filter documentation; parser validation and packet-selection observations were not performed. No matching-packet counts are claimed.

References: [capture-filter syntax](https://www.wireshark.org/docs/man-pages/pcap-filter.html), [display-filter syntax](https://www.wireshark.org/docs/man-pages/wireshark-filter.html), [Wireshark filter guide](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html).
