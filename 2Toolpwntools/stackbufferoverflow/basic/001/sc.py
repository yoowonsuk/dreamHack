from pwn import *

s1 = "/bin".encode("utf-8")
s2 = "//sh".encode("utf-8")

s1 = hex(u32(s1))
s2 = hex(u32(s2))
print(s1)
print(s2)
