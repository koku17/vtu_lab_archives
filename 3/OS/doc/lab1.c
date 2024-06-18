#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<stdlib.h>

int main(){
	pid_t child_pid;
	child_pid=fork();
	int status;
	if(child_pid<0){
		fprintf(stderr,"fork() failed !\n");
		exit(-1);
	}

	if(child_pid==0){
		printf("Child process (PID : %d) is running ...\n",getpid());
		char *args[]={"/bin/ls","-a",NULL};
		execvp(args[0],args);
		perror("exec() failed !");
		exit(1);
	}else{
		printf("Parent process (PID : %d) is waiting for the child to complete\n",getpid());
		wait(&status);
		if(WIFEXITED(status))
			printf("Child process (PID : %d) has completed with status %d\n",child_pid,WEXITSTATUS(status));
	}
	return(0);
}
