CFLAGS = -no-pie -fno-stack-protector

reto5: reto5.c
	gcc -o $@ $^ $(CFLAGS)

disable_aslr:
	echo 0 | sudo tee /proc/sys/kernel/randomize_va_space