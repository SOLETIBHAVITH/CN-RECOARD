# Experiment 13 - Inspecting Network Packets Using Wireshark

Aim:

To capture authorized test traffic and inspect packet addresses, protocols and header details.

Procedure:

1. Open Wireshark with a working Npcap capture driver on Windows.
2. Select the Npcap loopback capture interface for the loopback test below. Use another interface only for traffic you are authorized to inspect.
3. Set capture filter `icmp` so unrelated application traffic is excluded before collection.
4. Start capture, run the ping command below, and stop capture immediately after the test.
5. Apply display filter `icmp`. Select an echo request and inspect the packet list, packet details tree and packet bytes pane.
6. Expand IPv4 and ICMP to read source/destination addresses, type, identifier and sequence number. Find its matching echo reply.
7. For this loopback test, both endpoints are 127.0.0.1. Link-layer presentation depends on the capture interface and need not contain an Ethernet MAC header.
8. On an authorized TCP test from Experiment 4(a), repeat using capture filter `tcp port 31001` and display filter `tcp.port == 31001`; inspect flags and ports.
9. Record observed fields with local identifiers redacted. Close the capture without adding it to the repository.

Program / Commands:

```powershell
ping -n 2 127.0.0.1
```

Wireshark display filters:

```text
icmp
icmp.type == 8
icmp.type == 0
tcp.port == 31001
ip.addr == 127.0.0.1
```

The capture filter must match the current test: an ICMP-only capture cannot later reveal TCP packets that were excluded at capture time. Pair echo request/reply identifiers and sequence numbers; do not infer observations from the command alone.

Output / Observation:

**Execution Status: Not Verified**

Wireshark/Npcap was unavailable, so interface selection, live capture and packet inspection were not performed. Running a ping command does not by itself verify packet-analyzer observations. No private traffic or capture files are committed.

Reference: [Wireshark capture guide](https://www.wireshark.org/docs/wsug_html_chunked/ChapterCapture.html).
