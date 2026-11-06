# Experiment 15 - Study of Network Topology Using Benchmark LAN Trainer Kit

Aim:

To study bus, star, ring and mesh arrangements supported by the available Benchmark LAN trainer kit and test their connectivity.

Procedure:

1. Identify the trainer's exact model, manufacturer manual, supported topology modules and patch-panel labels. No hardware model or connector numbering is assumed here.
2. With the instructor, list the kit, supported node modules/PCs, appropriate cables and any required terminators, switch or token-ring unit. Follow the manual's connection and power sequence.
3. Build each supported arrangement using the topology-specific connections in the table below. Do not substitute arbitrary cables or assume every kit supports all four topologies.
4. Where real PCs/IP networking are supported, assign different lab addresses in the same subnet, such as 192.168.10.1/24 and 192.168.10.2/24. Otherwise use the kit's documented frame/token test facility.
5. Observe link/token/activity indicators and send the kit's test frames or run the ping commands below where applicable.
6. Record actual node connectivity and frame/token behavior. Perform a cable-failure demonstration only at an instructor-approved patch point, then restore it and repeat the test.
7. Compare component count, path arrangement, failure behavior and measured connectivity. Mark unsupported arrangements as not demonstrated.
8. Restore and power down the equipment according to its manual.

Program / Connections:

| Topology | Components and connection arrangement | Operation | Advantage | Limitation |
|---|---|---|---|---|
| Bus | Supported shared-medium bus modules; for a genuine legacy coax bus, use compatible BNC T-connectors and termination at both ends as specified by the kit | All attached nodes share the medium; classic Ethernet bus access uses collision detection | Little shared backbone cabling | Backbone or termination faults affect the segment; shared bandwidth and collisions |
| Star | PCs/node modules each connect by a separate supported cable to a central switch or hub module | Frames pass through the center; a switch learns MAC locations, while a hub repeats bits | A leaf-cable fault usually isolates one node | Central equipment failure affects all attached nodes; hubs share a collision domain |
| Ring | Supported ring/token modules or a compatible ring access unit connected in the order specified by the kit | Frames/token pass around a logical ring under the kit's protocol | Token-based rings can give orderly medium access | A single ring interruption can disrupt service unless bypass or a redundant ring is provided |
| Mesh | Nodes with enough independent ports and supported forwarding/routing; connect each intended pair separately | Multiple possible paths provide redundancy when the protocol can use them | Alternative paths can tolerate some link failures | Many ports/cables and forwarding complexity; a full mesh of n nodes has n(n-1)/2 links |

Do not make a ring/mesh by blindly connecting unmanaged Ethernet switch ports together. Redundant bridged links need suitable loop prevention; physical ring wiring alone does not create token-ring behavior. Ring and bus modules must be used only if this particular kit supports them.

Connectivity commands for a kit that supports ordinary Windows PCs:

```powershell
# From the node configured as 192.168.10.1:
ping -n 4 192.168.10.2
# Reverse the test from the other node:
ping -n 4 192.168.10.1
```

The example IPs are proposed lab settings, not observed private configuration. Use only the exact kit manual for socket labels, jumper positions and electrical connections.

Output / Observation:

**Execution Status: Not Verified**

Physical Demonstration: Not Performed. No Benchmark LAN trainer kit, model-specific manual or laboratory hardware was connected to this environment. No cable tests, indicator observations, packet counts or failure-recovery results are claimed. All four arrangements are study procedures pending a supported kit and instructor supervision.
