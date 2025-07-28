# Three nodes network & measure packets dropped
set ns [new Simulator]
set tf [open out/out1.tr w]
set nf [open out/out1.nam w]

$ns trace-all $tf
$ns namtrace-all $nf

# Create nodes
set num 3
for {set i 0} {$i < $num} {incr i} {
	set node($i) [$ns node]
}

# Create links
$ns duplex-link $node(0) $node(1) 1Mb 10ms DropTail
$ns duplex-link $node(1) $node(2) 800Kb 10ms DropTail

# Create queues
$ns duplex-link-op $node(1) $node(2) queuePos 0.5
$ns queue-limit $node(1) $node(2) 10

# Label nodes
$node(0) label "UDP"
$node(2) label "Null"

# Label flows
$ns color 0 Red

# Create connections
set udp [$ns create-connection UDP $node(0) Null $node(2) 0]
set cbr [$udp attach-app Traffic/CBR]

# Traffic
$cbr set packetSize_ 960
$cbr set rate_ 1Mb
$cbr set interval_ 0.001
$ns at 0.0 "$cbr start"
$ns at 10 "finish"

proc finish {} {
	global ns tf nf
	$ns flush-trace
	close $tf
	close $nf
	exit 0
}

# Start simulation
$ns run
