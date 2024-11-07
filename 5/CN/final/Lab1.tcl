#!/bin/ns

# Create Simulator
set ns [new Simulator]

# Open Trace file and NAM file
set ntrace [open out/out1.tr w]
set namfile [open out/out1.nam w]

$ns trace-all $ntrace
$ns namtrace-all $namfile

# Finish Procedure
proc finish {} {
	global ns ntrace namfile

	# Dump all the trace data and close the files
	$ns flush-trace
	close $ntrace
	close $namfile

	# Show the number of packets dropped
	exec printf "The number of packet drops is " &
	exec grep -c "^d" out/out1.tr &
	exec nam out/out1.nam &
	exit 0
}

# Create 3 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

# Label the nodes
$n0 label "TCP Source"
$n2 label "Sink"

# Set the color
$ns color 1 blue


# Create Links between nodes
# Modify the bandwidth to observe the variation in packet drop
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail

# Make the Link Orientation
$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n1 $n2 orient right

# Set Queue Size
# Modify the queue length to observe the variation in packet drop
$ns queue-limit $n0 $n1 10
$ns queue-limit $n1 $n2 10

# Set up a Transport layer connection
set tcp0 [new Agent/TCP]
set sink0 [new Agent/TCPSink]

$ns attach-agent $n0 $tcp0
$ns attach-agent $n2 $sink0
$ns connect $tcp0 $sink0

# Set up an Application layer Traffic
set cbr0 [new Application/Traffic/CBR]

$cbr0 set type_ CBR
$cbr0 set packetSize_ 100
$cbr0 set rate_ 1Mb
$cbr0 set random_ false
$cbr0 attach-agent $tcp0

$tcp0 set class_ 1

# Schedule Events
$ns at 0 "$cbr0 start"
$ns at 5 "finish"

# Run the Simulation
$ns run
