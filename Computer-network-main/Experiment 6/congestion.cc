#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/internet-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
#include <iostream>

using namespace ns3;
uint32_t drops = 0;

void QueueDrop(Ptr<const Packet> packet)
{
    ++drops;
}

void WindowChange(uint32_t oldWindow, uint32_t newWindow)
{
    std::cout << "Time " << Simulator::Now().GetSeconds()
              << " s; cwnd " << oldWindow << " -> " << newWindow << " bytes\n";
}

void ConnectWindowTrace()
{
    Config::ConnectWithoutContext(
        "/NodeList/0/$ns3::TcpL4Protocol/SocketList/0/CongestionWindow",
        MakeCallback(&WindowChange));
}

int main()
{
    Config::SetDefault("ns3::TcpL4Protocol::SocketType", TypeIdValue(TcpNewReno::GetTypeId()));
    NodeContainer nodes;
    nodes.Create(2);
    PointToPointHelper link;
    link.SetDeviceAttribute("DataRate", StringValue("1Mbps"));
    link.SetChannelAttribute("Delay", StringValue("10ms"));
    link.SetQueue("ns3::DropTailQueue<Packet>", "MaxSize", StringValue("10p"));
    link.DisableFlowControl();
    NetDeviceContainer devices = link.Install(nodes);
    InternetStackHelper internet;
    internet.Install(nodes);
    Ipv4AddressHelper addresses;
    addresses.SetBase("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces = addresses.Assign(devices);
    devices.Get(0)->GetObject<PointToPointNetDevice>()->GetQueue()->TraceConnectWithoutContext(
        "Drop", MakeCallback(&QueueDrop));

    PacketSinkHelper tcpSink("ns3::TcpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), 5000));
    PacketSinkHelper udpSink("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), 5001));
    tcpSink.Install(nodes.Get(1)).Start(Seconds(0));
    udpSink.Install(nodes.Get(1)).Start(Seconds(0));
    BulkSendHelper tcp("ns3::TcpSocketFactory", InetSocketAddress(interfaces.GetAddress(1), 5000));
    tcp.SetAttribute("MaxBytes", UintegerValue(0));
    ApplicationContainer tcpApp = tcp.Install(nodes.Get(0));
    tcpApp.Start(Seconds(1));
    tcpApp.Stop(Seconds(9));
    OnOffHelper udp("ns3::UdpSocketFactory", InetSocketAddress(interfaces.GetAddress(1), 5001));
    udp.SetConstantRate(DataRate("2Mbps"), 1000);
    ApplicationContainer udpApp = udp.Install(nodes.Get(0));
    udpApp.Start(Seconds(1));
    udpApp.Stop(Seconds(9));
    Simulator::Schedule(Seconds(1.01), &ConnectWindowTrace);
    Simulator::Stop(Seconds(12));
    Simulator::Run();
    std::cout << "Forward device queue drops: " << drops << "\n";
    Simulator::Destroy();
}
