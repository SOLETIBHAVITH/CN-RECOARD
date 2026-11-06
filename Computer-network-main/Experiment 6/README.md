# Experiment 6 - Network Simulator (NS2 and NS3) and Congestion Control

Aim:

To study NS2 and NS3 and observe TCP congestion-window changes and queue drops on a constrained link.

Procedure:

1. Use a Linux laboratory machine or a configured WSL Linux distribution with the selected simulator installed.
2. Create two nodes joined by a 1 Mb/s, 10 ms point-to-point link with a 10-packet forward queue.
3. Start a bulk TCP transfer and competing 2 Mb/s UDP traffic at 1 second.
4. Stop both traffic sources at 9 seconds and allow queued traffic to drain until 12 seconds.
5. Observe the TCP congestion window and count queue drops.
6. Compare how TCP adjusts its window when traffic exceeds link capacity; do not compare raw cwnd units across simulators.

Program / Commands:

NS2 is a discrete-event simulator commonly configured using Tcl. NS3 is a separate simulator with C++ models and a different build system; these are not interchangeable versions of one API.

- [NS2 source: congestion.tcl](congestion.tcl), intended for NS2 2.35; TCP Reno, cwnd in packets.
- [NS3 source: congestion.cc](congestion.cc), written against the ns-3.46 C++ APIs; TCP NewReno, cwnd in bytes.

For NS2, with an existing `ns` installation, copy the source to an empty temporary working directory:

```bash
ns congestion.tcl
```

The program prints window samples and counts `d` events in `congestion.tr`. Inspect that generated trace outside this repository. It refuses to overwrite an existing trace.

For NS3, use a configured ns-3.46 source tree with its supported C++ compiler, CMake and Python 3 build runner. Copy `congestion.cc` into that tree's `scratch` folder:

```bash
./ns3 configure
./ns3 build
./ns3 run scratch/congestion
```

The NS3 program traces each TCP congestion-window change and the forward device queue's Drop events. Device flow control is disabled so the bounded DropTail device queue can visibly drop packets. No capture or plot is generated. The examples use an isolated simulated subnet, not the machine's private configuration.

Output / Observation:

**Execution Status: Not Verified**

No NS2/NS3 executable or configured WSL Linux distribution was available. Native simulator execution and NS3 compilation were not verified. Source APIs were checked against the ns-3.46 headers and example code; this does not replace compilation.

Expected behavior, not measured output: competing traffic can overflow the bounded queue; TCP window growth and reductions reflect congestion control. UDP does not adjust its sending rate in these examples. No packet-drop counts, window values or timestamps are claimed.

References: [NS2 manual](https://www.isi.edu/nsnam/ns/doc/), [ns-3.46 source and documentation](https://gitlab.com/nsnam/ns-3-dev/-/tree/ns-3.46).
