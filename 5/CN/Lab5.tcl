#!/bin/ns

set ns [new Simulator]
set tf [open out/out5.tr w]
set nf [open out/out5.nam w]

$ns trace-all $tf
$ns namtrace-all $nf

set n0 [$ns node]
set n1 [$ns node]

$n0 label "Sender"
$n1 label "Receiver"

$ns duplex-link $n0 $n1 .2Mb 200ms DropTail
$ns queue-limit $n0 $n1 10

$ns duplex-link-op $n0 $n1 orient right

set tcp1 [new Agent/TCP]
set sink2 [new Agent/TCPSink]
set ftp0 [new Application/FTP]

$tcp1 set windowInit_ 4
$tcp1 set maxcwnd_ 4
$tcp1 set packetSize_ 500

$ns attach-agent $n0 $tcp1
$ns attach-agent $n1 $sink2
$ns connect $tcp1 $sink2
$ftp0 attach-agent $tcp1

$ns at .1 "$ftp0 start"
$ns at 3.5 "$ftp0 stop"

proc finish {} {
	global ns tf nf
	$ns flush-trace
	close $tf
	close $nf
	exec nam out/out5.nam &
	exit 0
}

$ns at 5 "finish"
$ns run
