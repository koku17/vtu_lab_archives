# OS-AIML-2024 Lab Programs
The Programs here mentioned are the part of the subject "Operating System".

## Tree Structure

```
.
├── ./lab1.c
├── ./lab2.fcfs.c
├── ./lab2.pr.c
├── ./lab2.rr.c
├── ./lab2.sjf.c
├── ./lab3.c
├── ./lab4.reader.c
├── ./lab4.writer.c
├── ./lab5.c
├── ./lab6.best.c
├── ./lab6.first.c
├── ./lab6.worst.c
├── ./lab7.fifo.c
├── ./lab7.lru.c
├── ./lab8.c
├── ./lab8.dld.c
├── ./lab8.sld.c
├── ./lab9.c
├── ./lab10.c
├── ./LICENSE
├── ./makefile
└── ./README.md
```

### Compilation
Compilation of the following problem don't requier advanced tools. <br/>
It will be ran on just on either `cc` , `clang` or `gcc` .

### Makefile
Here we are using makefile to compile the Program(s) in bulk with different names with extension `*.bin` .

#### Building
Compile all files once.
```
make build
```

#### Clean
Remove all compiled binaries `*.bin` .
```
make clean
```

#### Archive
Generates compressed Tape archive `archive.tgz` .
```
make ark
```
To extract the archive
```
tar -xvf archive.tgz
```

#### CD-ROM
Make a CD-ROM Storage for copying archived C sources in Virtual Machine(s). <br/>
You need the package `cdr-tools` with the utility `mkisofs` .
```
make cdrom
```
---
## LICENSE
THIS SOFTWARE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION,<br/>
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
