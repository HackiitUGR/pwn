CFLAGS = -no-pie -fno-stack-protector -z execstack

reto3: reto3.c
	gcc -o $@ $^ $(CFLAGS)

disable_aslr:
	echo 0 | sudo tee /proc/sys/kernel/randomize_va_space