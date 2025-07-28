#!/bin/ns

set ns [new Simulator]
set tf [open out/out3.tr w]
set nf [open out/out3.nam w]

$ns trace-all $tf
$ns namtrace-all $nf

set n0 [$ns node]
set n1 [$ns node]
$n0 color "magenta"
$n0 label "src1"

set n2 [$ns node]
$n2 color "magenta"
$n2 label "src2"

set n3 [$ns node]
set n4 [$ns node]
$n3 color "blue"
$n3 label "dest2"

set n5 [$ns node]
$n5 color "blue"
$n5 label "dest1"

$ns make-lan "$n0 $n1 $n2 $n3 $n4" 100Mb 100ms LL Queue/DropTail Mac/802_3
$ns duplex-link $n4 $n5 1Mb 1ms DropTail

set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0

set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ftp0 set packetSize_ 500
$ftp0 set interval_ 0.0001

set sink5 [new Agent/TCPSink]
$ns attach-agent $n5 $sink5
$ns connect $tcp0 $sink5

set tcp2 [new Agent/TCP]
$ns attach-agent $n2 $tcp2

set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set packetSize_ 600
$ftp2 set interval_ 0.001

set sink3 [new Agent/TCPSink]
$ns attach-agent $n3 $sink3
$ns connect $tcp2 $sink3

set file1 [open out/out3.1.tr w]
$tcp0 attach $file1

set file2 [open out/out3.2.tr w]
$tcp2 attach $file2

$tcp0 trace cwnd_
$tcp2 trace cwnd_

proc finish {} {
	global ns nf tf
	$ns flush-trace
	close $tf
	close $nf
	exec awk -f awk/out3.awk out/out3.1.tr > out/out3.1.dat &
	exec awk -f awk/out3.awk out/out3.2.tr > out/out3.2.dat &
	exec xgraph -color red out/out3.1.dat -color green out/out3.2.dat &
	exec nam out/out3.nam &
	exit 0
}

$ns at .1 "$ftp0 start"
$ns at 5 "$ftp0 stop"
$ns at 7 "$ftp0 start"
$ns at .2 "$ftp2 start"
$ns at 8 "$ftp2 stop"
$ns at 14 "$ftp0 stop"
$ns at 10 "$ftp2 start"
$ns at 15 "$ftp2 stop"
$ns at 16 "finish"

$ns run
