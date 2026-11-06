# Experiment 14 - Creating a Simple Network Using Cisco Packet Tracer

Aim:

To connect two PCs through a switch, configure a common IPv4 subnet and test connectivity in Cisco Packet Tracer.

Procedure:

1. Open Cisco Packet Tracer and create a blank topology.
2. Add PC0, PC1 and a 2960 switch with FastEthernet ports.
3. Use copper straight-through cables: PC0 FastEthernet0 to switch FastEthernet0/1, and PC1 FastEthernet0 to switch FastEthernet0/2.
4. In each PC's Desktop > IP Configuration, enter the addressing table below. Leave the default gateway blank because this topology has no router.
5. Leave both switch ports in the same default VLAN, or apply the simple access-port configuration below. Wait until link indicators are active.
6. From PC0 Desktop > Command Prompt, ping PC1. Repeat from PC1 to PC0. Initial ARP discovery can precede successful replies; record what actually happens.
7. If the test fails, inspect cable endpoints, link state, masks and VLAN membership before repeating.
8. Save the actual project through File > Save As > SimpleNetwork.pkt. Only an authentic application-generated project is a valid native deliverable.

Program / Configuration:

```text
PC0 -------- 2960 Switch -------- PC1
```

| Device | Interface | IPv4 address | Subnet mask | Gateway |
|---|---|---|---|---|
| PC0 | FastEthernet0 | 192.168.10.1 | 255.255.255.0 | Blank |
| PC1 | FastEthernet0 | 192.168.10.2 | 255.255.255.0 | Blank |

These are artificial lab addresses, not the user's observed network settings. A switch management IP is unnecessary for forwarding between the two PCs.

Switch CLI, for the specified 2960 model:

```text
enable
configure terminal
hostname LabSwitch
interface fastEthernet0/1
switchport mode access
no shutdown
exit
interface fastEthernet0/2
switchport mode access
no shutdown
end
show interfaces status
```

PC commands:

```text
PC0> ping 192.168.10.2
PC1> ping 192.168.10.1
```

Output / Observation:

**Execution Status: Not Verified**

Cisco Packet Tracer was not installed. The native topology and .pkt project could not be generated, and ping connectivity was not tested in Packet Tracer. No fake project file or invented ping results are included. The addressing and procedure are ready for practical execution.
