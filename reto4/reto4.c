#include <stdio.h>
#include <stdlib.h>

void win(int arg1, int arg2) {
	if (arg1 != 0x1234 || arg2 != 0x1337) {
		printf("nope! 0x%x, 0x%x\n", arg1, arg2);
		return;
	}
	system("/bin/sh");
}

int main() {
	printf("Hi! Introduce your input:\n");
	char input[32];
	gets(input);
	printf("Bye!\n");
}