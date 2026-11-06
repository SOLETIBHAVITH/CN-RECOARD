#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/internet-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
#include <iomanip>
#include <iostream>
#include <string>

using namespace ns3;

int main(int argc, char* argv[])
{
    std::string transport = "TCP";
    CommandLine command;
    command.AddValue("transport", "TCP or UDP", transport);
    command.Parse(argc, argv);
    if (transport != "TCP" && transport != "UDP")
    {
        std::cerr << "Use --transport=TCP or --transport=UDP\n";
        return 1;
    }
    Config::SetDefault("ns3::TcpL4Protocol::SocketType", TypeIdValue(TcpNewReno::GetTypeId()));
    Config::SetDefault("ns3::TcpSocket::SegmentSize", UintegerValue(1024));
    std::string factory = transport == "TCP" ? "ns3::TcpSocketFactory" : "ns3::UdpSocketFactory";
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

    PacketSinkHelper sink(factory, InetSocketAddress(Ipv4Address::GetAny(), 5000));
    ApplicationContainer sinks = sink.Install(nodes.Get(1));
    sinks.Start(Seconds(0));
    OnOffHelper source(factory, InetSocketAddress(interfaces.GetAddress(1), 5000));
    source.SetConstantRate(DataRate("2Mbps"), 1024);
    ApplicationContainer senders = source.Install(nodes.Get(0));
    senders.Start(Seconds(1));
    senders.Stop(Seconds(9));
    FlowMonitorHelper flowHelper;
    Ptr<FlowMonitor> monitor = flowHelper.InstallAll();
    Simulator::Stop(Seconds(12));
    Simulator::Run();
    // After drain time, classify any unreceived IP packets as missing at the end.
    monitor->CheckForLostPackets(Seconds(0));
    Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier>(flowHelper.GetClassifier());
    std::cout << std::fixed << std::setprecision(3) << "Transport: " << transport << "\n";
    for (const auto& entry : monitor->GetFlowStats())
    {
        auto flow = classifier->FindFlow(entry.first);
        if (flow.destinationPort != 5000)
        {
            continue; // Exclude reverse TCP ACK flows.
        }
        const auto& stats = entry.second;
        uint32_t missing = stats.txPackets - stats.rxPackets;
        double loss = stats.txPackets ? 100.0 * missing / stats.txPackets : 0;
        double delay = stats.rxPackets ? stats.delaySum.GetSeconds() * 1000 / stats.rxPackets : 0;
        std::cout << "Forward IP packets sent: " << stats.txPackets
                  << "\nForward IP packets received: " << stats.rxPackets
                  << "\nMissing by simulation end: " << missing
                  << "\nMissing percentage: " << loss
                  << "\nIP throughput over 11 s (Mbps): " << stats.rxBytes * 8.0 / 11 / 1e6
                  << "\nMean received-IP-packet delay (ms): " << delay << "\n";
    }
    auto receiver = DynamicCast<PacketSink>(sinks.Get(0));
    std::cout << "Application goodput over 11 s (Mbps): " << receiver->GetTotalRx() * 8.0 / 11 / 1e6 << "\n";
    Simulator::Destroy();
}
