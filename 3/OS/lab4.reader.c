#include<fcntl.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdio.h>
#define MAX_BUF 1024

int main(){
	int fd;

	// A temporary FIFO file is not created in reader
	char *myfifo = "/tmp/myfifo";
	char buf[MAX_BUF];

	// Open the named pipe for reading
	fd=open(myfifo,O_RDONLY);

	// Read data from the FIFO
	read(fd,buf,MAX_BUF);
	printf("Writer: %s\n",buf);

	// Close the FIFO
	close(fd);
	return 0;
}
