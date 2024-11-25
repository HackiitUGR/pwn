#include <stdio.h>
#include <stdlib.h>

void win() {
	system("/bin/sh");
}

int main() {
	printf("Hi! Introduce your input:\n");

	char input[32];
	unsigned long value = 0;
	gets(input);

	if (value == 0xdeadbeefcacabaca) {
		printf("Success!\n");
		win();
	} else {
		printf("Nope! value: 0x%lx\n", value);
	}
	printf("Bye!\n");
}