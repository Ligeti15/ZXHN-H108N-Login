# ZXHN-H108N-Login
Hacking ZXHN H108N Router (brute-force)
This project is a demonstration of how to crack the login of ZTE (ZXHN-H108N) via telnet as described here: https://jalalsela.com/hacking-zxhn-h108n-router/

usage: zte-crack.py [-h] [-a ADDR] [-u USER] [-w WORDLIST] [-p]

This is a brute-force tool build to crack the ZTE ZXHN H108N Telnet password.
For more information, check: https://jalalsela.com/hacking-zxhn-h108n-router/

optional arguments:
  -h, --help            show this help message and exit
  -a ADDR, --addr ADDR  The IP address of ZTE AP (default: 192.168.1.1)
  -u USER, --user USER  Username to use (default: root)
  -w WORDLIST, --wordlist WORDLIST
                        The path to the worldlist
  -p, --password        Password to use (default: public)

Create by: Jalal Sela (Ligeti)
