#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - make 5 zombie processes.
 * Return:0
 */


int main(void)
{
	pid_t zombie;
	int clone_number = 0;

	while (clone_number < 5)
	{
		zombie = fork();

		if (zombie)
			printf("Zombie process created, PID: %i\n", zombie);
		else
			exit(0);

		clone_number++;
	}

	return (0);
}
