import socket
import struct
import sys

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

def send(message):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
  sock.sendto(message, (MCAST_GRP, MCAST_PORT))

def read():
  while 1:
    # read line from stdin and send it to the multicast group
    message = sys.stdin.readline().rstrip()
    send(message)

def main():
  read()

if __name__ == '__main__':
  main()