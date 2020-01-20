#!/usr/bin/env python3

import sys
import os


global dName, arguments, ports
arguments = len(sys.argv)
dName = sys.argv[1]
ports = []


def srlornot(var):
    try:
        int(var)
        return var
    except ValueError:
        print("\nPort has to be a number\n--Exits--")
        sys.exit()


def addport(port):
    ports.append(port)

def istelnet(port):
    cmd = ("nc -w3 -z -v %s %s 2>&1 | grep telnet | grep open" % (dName, port) )
    check = os.popen(cmd).read()
#    print("inne i istelnet check: " + check)  # test code + "cmd: " + cmd)
    if check == '':
        check = 0
    else:
        check = 1
    return check

def openclose(port):
        if istelnet(port) == 0:
            print("Port " + str(port) + " is closed")
            print(dName + ':' + str(port) + " - CLOSED\n\n")
        else:
            print("Port " + str(port) + " is open")
            print(dName + ':' + str(port) + " - OPEN\n\n")


if arguments < 3:
    print("You must parse a website address and port number (or range < 22 53 > in the argument")
    sys.exit()
elif arguments > 4:
    print("Too many arguments")
    sys.exit()

if arguments == 3:
    var = srlornot(sys.argv[2])
    port = int(var)
    addport(port)

if arguments == 4:
    var1 = srlornot(sys.argv[2])
    var2 = srlornot(sys.argv[3])
    port1 = int(var1)
    port2 = int(var2)
    if port1 < port2:
        var = port2 - port1
        count = 0
        while (count < var + 1):
            send = port1 + count
            addport(send)
            count = count + 1
    elif port1 > port2:
        var = port1 - port2
        count = 0
        while (count < var + 1):
            send = port1 + count
            addport(send)
            count = count + 1
    else:
        sys.exit()


if len(ports) > 1:
    for port in ports:
        openclose(port)
else:
    openclose(ports)
