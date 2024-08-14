#define WIN_OFFSET 0x13A9

int 3
pop rax
push rax
sub rax, 0x144b
mov rcv, rax
mov rdx, rcx

push 0
call rax
pop rax
ret
