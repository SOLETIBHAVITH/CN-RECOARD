set ns [new Simulator]
set tracefile "congestion.tr"
if {[file exists $tracefile]} {
    puts stderr "Use a clean working directory; congestion.tr already exists."
    exit 1
}
set trace [open $tracefile w]
$ns trace-all $trace
set sender [$ns node]
set receiver [$ns node]
$ns duplex-link $sender $receiver 1Mb 10ms DropTail
$ns queue-limit $sender $receiver 10

set tcp [new Agent/TCP/Reno]
$tcp set packetSize_ 1000
$ns attach-agent $sender $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $receiver $sink
$ns connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp

set udp [new Agent/UDP]
$ns attach-agent $sender $udp
set null [new Agent/Null]
$ns attach-agent $receiver $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 1000
$cbr set rate_ 2Mb
$cbr attach-agent $udp

proc sampleWindow {} {
    global ns tcp
    puts "Time [$ns now] s; TCP cwnd [$tcp set cwnd_] packets"
    if {[$ns now] < 9.0} {
        $ns at [expr {[$ns now] + 0.5}] "sampleWindow"
    }
}

proc finish {} {
    global ns trace tracefile
    $ns flush-trace
    close $trace
    set input [open $tracefile r]
    set drops 0
    while {[gets $input line] >= 0} {
        if {[lindex $line 0] eq "d"} {incr drops}
    }
    close $input
    puts "Dropped packets in trace: $drops"
    puts "Trace saved: $tracefile"
    exit 0
}

$ns at 1.0 "$ftp start"
$ns at 1.0 "$cbr start"
$ns at 1.5 "sampleWindow"
$ns at 9.0 "$ftp stop"
$ns at 9.0 "$cbr stop"
$ns at 12.0 "finish"
$ns run
