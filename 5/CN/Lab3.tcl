#!/usr/bin/ns

# Create Simulator
set ns [new Simulator]

# Use colors to differentiate the trafics
$ns color 1 Blue
$ns color 2 Red

# Open Trace and NAM file
set ntrace [open /tmp/out5.tr w]
set namfile [open /tmp/out5.nam w]

$ns trace-all $ntrace
$ns namtrace-all $namfile

# Create congestion graph windows
set wf0 [open /tmp/wf0 w]
set wf1 [open /tmp/wf1 w]

# Finish Procedure
proc finish {} {
	# Dump all trace data and Close the files
	global ns ntrace namfile
	$ns flush-trace
	close $ntrace
	close $namfile
	
	exec xgraph /tmp/wf0 /tmp/wf1 &
	exec nam /tmp/out5.nam &
	exit 0
}

# Plot Window Procedure
proc PlotWindow {tcpSource file} {
	global ns
	set time .1
	set now [$ns now]
	 
	set cwnd [$tcpSource set cwnd_]
	puts $file "$now $cwnd"
	$ns at [expr $now + $time] "PlotWindow $tcpSource $file"
}

# Create 6 nodes
for {set i 0} {$i<6} {incr i} {
	set n($i) [$ns node]
}

# Create duplex links between the nodes
$ns duplex-link $n(0) $n(2) 2Mb 10ms DropTail
$ns duplex-link $n(1) $n(2) 2Mb 10ms DropTail
$ns duplex-link $n(2) $n(3) .6Mb 100ms DropTail

# Nodes n(3), n(4) and n(5) are considered in a LAN
set lan [$ns newLan "$n(3) $n(4) $n(5)" .5Mb 40ms LL Queue/DropTail MAC/802_3 Channel]

# Orientation to the nodes
$ns duplex-link-op $n(0) $n(2) orient right-down
$ns duplex-link-op $n(1) $n(2) orient right-up
$ns duplex-link-op $n(2) $n(3) orient right

# Setup queue between n(2) and n(3) and monitor the queue
$ns queue-limit $n(2) $n(3) 20
$ns duplex-link-op $n(2) $n(3) queuePos .5

# Set error model on link n(2) to n(3)
set loss_module [new ErrorModel]
$loss_module ranvar [new RandomVariable/Uniform]
$loss_module drop-target [new Agent/Null]
$ns lossmodel $loss_module $n(2) $n(3)

# Set up the TCP connection between n(0) and n(4)
set tcp0 [new Agent/TCP/Newreno]
$tcp0 set fid_ 1
$tcp0 set window_ 8000
$tcp0 set packetSize_ 552
$ns attach-agent $n(0) $tcp0
set sink0 [new Agent/TCPSink/DelAck]
$ns attach-agent $n(4) $sink0
$ns connect $tcp0 $sink0

# Apply FTP Application over TCP
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ftp0 set type_ FTP

# Set up another TCP connection between n(5) and n(1)
set tcp1 [new Agent/TCP/Newreno]
set sink1 [new Agent/TCPSink/DelAck]
$tcp1 set fid_ 2
$tcp1 set window_ 8000
$tcp1 set packetSize_ 552
$ns attach-agent $n(5) $tcp1
$ns attach-agent $n(1) $sink1
$ns connect $tcp1 $sink1

# Apply FTP application over TCP
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

# Schedule Events
$ns at .1 "$ftp0 start"
$ns at .1 "PlotWindow $tcp0 $wf0"
$ns at .5 "$ftp1 start"
$ns at .5 "PlotWindow $tcp1 $wf1"
$ns at 25 "$ftp0 stop"
$ns at 25.1 "$ftp1 stop"
$ns at 25.2 "finish"

# Run the simulation
$ns run
