#sudo apt-get install python-scapy tcpdump
from scapy.all import *

def arp_display(pkt):
  if pkt.haslayer(DHCP):
    print pkt[Ether].src

print "Druecken Sie den Dashbutton"
print sniff(prn=arp_display, filter="(udp and (port 67 or 68))", store=0)
