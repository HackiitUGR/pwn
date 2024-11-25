CFLAGS = -no-pie -fno-stack-protector -static # static para que haya gadgets pop rdi y pop rsi

reto4: reto4.c
	gcc -o $@ $^ $(CFLAGS)