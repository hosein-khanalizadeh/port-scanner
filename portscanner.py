#!/usr/bin/python

import os
import sys
import re
from socket import socket , gethostbyname , gethostbyaddr , AF_INET , SOCK_STREAM


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
cyan = '\033[36m'
reset = "\033[0;0m"

ip_regex = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

def banner():
    print(f"""{blue}
 *******************************************************************
 *     ____             __  _____                                  *
 *    / __ \____  _____/ /_/ ___/_________ _____  ____  ___  _____ *
 *   / /_/ / __ \/ ___/ __/\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/ *
 *  / ____/ /_/ / /  / /_ ___/ / /__/ /_/ / / / / / / /  __/ /     *
 * /_/    \____/_/   \__//____/\___/\__,_/_/ /_/_/ /_/\___/_/      *
 *                                                                 *
 *******************************************************************

{reset}""")

def port_scanner(range_of_port:list , ip:str):
    if int(range_of_port[0]) < int(range_of_port[1]):
        for port in range(int(range_of_port[0]) , int(range_of_port[1])):
            s = socket(AF_INET , SOCK_STREAM)
            res = s.connect_ex((ip , port))
            if res == 0:
                print(f'{green} [+] Port {port} is open !{reset}')
            else:
                print(f'{red} [+] Port {port} is close !{reset}')
    else:
        print(f'{red} [-] Port Range is Incorrect !{reset}')

def main():
    try:
        os.system('clear')
    except:
        os.system('cls')
    banner()
    host = input(f'{yellow} domian or ip >>> {reset}')
    ports_range = input(f'{yellow} ports_range >>> {reset}')
    print()
    if (re.search(ip_regex, host)):
        addr = host
        name = gethostbyaddr(addr)
    elif host.startswith('http://'):
        name = host[7:]
        addr = gethostbyname(name)
    elif host.startswith('https://'):
        name = host[8:]
        addr = gethostbyname(name)
    else:
        name = host
        addr = gethostbyname(name)
    try:
        range_of_port = ports_range.split('-', 2)
        print(f'{cyan} name : {name}{reset}')
        print(f'{cyan} addr : {addr}{reset}')
        print(f'{cyan} port range : {ports_range}{reset}')
        print()
        port_scanner(range_of_port, addr)
        print()
    except:
        print(f'{red} [!] Port Range is not True !{reset}')
        print(f'{red} [!] True Range : 20-80 .{reset}')
        sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
