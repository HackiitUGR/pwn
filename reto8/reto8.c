#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void ask_input() {
	printf("Introduce the length:\n");
	unsigned length = 0;
	scanf("%u", &length);

	printf("Introduce your input of %u bytes:\n", length);
	char input[32];
	read(STDIN_FILENO, input, length);

	printf("Thanks! Your input was:\n");
	write(STDOUT_FILENO, input, length);
	printf("\n");
}

int main() {
	printf("Hi!\n\n");
	ask_input();
	ask_input();
	printf("Bye!\n");
}