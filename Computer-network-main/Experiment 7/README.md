# Experiment 7 - TCP/UDP Performance Using a Simulation Tool

Aim:

To compare TCP and UDP transmission, throughput, loss and delay using identical NS3 link and application parameters.

Algorithm:

1. Read TCP or UDP as the selected transport and create two simulated nodes.
2. Join them with a 1 Mb/s, 10 ms point-to-point link and a 10-packet DropTail device queue.
3. Install the selected socket receiver and a 2 Mb/s, 1024-byte OnOff source.
4. Generate traffic from 1 to 9 seconds, then continue until 12 seconds to drain queues.
5. Collect forward-flow IP packet counts, bytes and delays using FlowMonitor; exclude reverse TCP acknowledgements.
6. Print missing-packet percentage, IP throughput, application goodput and mean received-packet delay.
7. Repeat with the other transport and compare the measured results over the same 1-to-12-second interval.

Program / Commands:

[Source: performance.cc](performance.cc)

Requires a configured **ns-3.46** Linux/WSL source tree, a supported C++ compiler, CMake and Python 3. Put the source in that tree's `scratch` directory:

```bash
./ns3 configure
./ns3 build
./ns3 run "scratch/performance --transport=TCP"
./ns3 run "scratch/performance --transport=UDP"
```

The trials use the same link, queue, offered application rate, packet size and timing. TCP uses NewReno with a 1024-byte segment size and is subject to transport backpressure; UDP continues at the configured rate. Device flow control is disabled to expose device queue overflow.

Metrics:

- Missing packets = forward IP transmissions minus forward IP receptions at simulation end, after three seconds of drainage. This is an IP-attempt loss measure; TCP retransmissions are separate IP transmissions and TCP may recover application bytes.
- Missing percentage = 100 times missing packets divided by transmitted packets.
- IP throughput = received IP bytes times 8 divided by the fixed 11-second measurement interval; convert to Mbps. IP headers are included.
- Application goodput = bytes delivered to PacketSink times 8 divided by the same interval; transport headers are excluded.
- Mean delay = FlowMonitor delay sum divided by received IP packets, in milliseconds. A zero value with no received packets is a guarded calculation, not a measured zero-delay path.

The fixed interval includes drain time. FlowMonitor also counts TCP control packets. These are protocol differences to interpret, rather than identical one-to-one application-packet populations. No XML trace, build directory or plot belongs in this laboratory repository.

Output / Observation:

**Execution Status: Not Verified**

NS3 and a configured Linux/WSL toolchain were unavailable; C++ compilation and both simulation runs were not performed. No numerical throughput, loss or delay values are supplied.

Expected behavior only: overload can produce UDP loss; TCP adapts its rate and can retransmit. Which transport has higher throughput or delay depends on the actual measured trial, so no winner is asserted.

Reference: [ns-3.46 FlowMonitor model documentation](https://github.com/nsnam/ns-3-dev-git/blob/ns-3.46/src/flow-monitor/doc/flow-monitor.rst).
