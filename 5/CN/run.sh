#!/bin/sh

for i in *.xwd ; do convert -transparent '#e5e5e5' $i ${i%.xwd}.png ; done
ffmpeg -start_number 0 -i nam0%4d.png -r 60 -loop 0 test.gif -y
convert test.gif -fill white -opaque black test.dark.gif
rm -rf *.png *.xwd
