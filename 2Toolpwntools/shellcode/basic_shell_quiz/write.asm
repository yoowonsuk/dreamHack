section .text
global _start
_start:
    ;/* write(fd=1, buf='hello', n=48) */
    ;/* push 'hello\x00' */
    mov rax, 0x0a6f6c6c6568
    push rax
    mov rsi, rsp
    push 1
    pop rdi
    push 0x6
    pop rdx
    ;/* call write() */
    push 1
    pop rax
    syscall
