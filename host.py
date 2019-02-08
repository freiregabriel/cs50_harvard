#!/usr/bin/env python
import socket
import sys
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
sys.stdout.write("\n** Get IP script by Gabriel Freire **\n\nHost:\t{}\nIP:\t{}\n *****************".format(hostname, ip_addr))
sys.stdout.flush()