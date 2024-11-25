#include <stdio.h>
#include <stdlib.h>

void win() {
	system("/bin/sh");
}

int main() {
	printf("Hi! Introduce your input:\n");
	char input[32];
	gets(input);
	printf("Bye!\n");
}