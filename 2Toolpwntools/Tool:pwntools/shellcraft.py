from pwn import *
context.arch = 'amd64' # 대상 아키텍처 x86-64
code = shellcraft.sh() # 셸을 실행하는 셸 코드 
print(code)
