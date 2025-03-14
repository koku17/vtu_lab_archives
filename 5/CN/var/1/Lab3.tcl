set ns [new Simulator]
set tf [open out/out3.tr w]
set nf [open out/out3.nam w]

$ns trace-all $tf
$ns namtrace-all $nf

# Create nodes
set node(0) [$ns node]
set num 6

for {set i 1} {$i <= $num} {incr i} {
	set node($i) [$ns node]
	lappend nodelist $node($i)
}

# create LAN and links
$ns make-lan $nodelist 10Mb 10ms LL Queue/DropTail
$ns duplex-link $node(0) $node(1) 1Mb 10ms DropTail
$ns duplex-link-op $node(0) $node(1) queuePos 0.5
$ns duplex-link-op $node(0) $node(1) orient right

# Create connections
set tcp0 [$ns create-connection TCP $node(0) TCPSink $node(5) 0]
set tcp1 [$ns create-connection TCP $node(2) TCPSink $node(6) 0]
set ftp0 [$tcp0 attach-app FTP]
set ftp1 [$tcp1 attach-app FTP]

$tcp0 attach $tf
$tcp0 trace cwnd_
$tcp1 attach $tf
$tcp1 trace cwnd_

$ns at 0.1 "$ftp0 start"
$ns at 0.2 "$ftp1 start"
$ns at 10 "finish"

proc finish {} {
	global ns tf nf
	$ns flush-trace
	close $tf
	close $nf
	exit 0
}

# Start simulator
$ns run
