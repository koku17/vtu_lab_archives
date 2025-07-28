#include<stdio.h>
#include<fcntl.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<unistd.h>
#include<string.h>

int main(){
	int fd;
	char buf[1024];

	// Create the named pipe (FIFO)
	char *myfifo="/tmp/myfifo";
	mkfifo(myfifo,0666);
	printf("Run Reader process to read the FIFO File\n");

	// Open the named pipe for writing
	fd=open(myfifo,O_WRONLY);

	// Write data to the FIFO
	strcpy(buf,"Hello from Writer Process");
	write(fd,buf,sizeof(buf));

	// Close the FIFO
	close(fd);

	// Remove the FIFO
	unlink(myfifo);
	return 0;
}
