

import numpy as np
from numpy import uint8, uint16
import test_packets as tpkts
import time
from pktcomm import PacketError, LoopBack


intf = LoopBack(pkt_class=tpkts.BasePacket, addr=0x01)

def send_ex():
    pkt = tpkts.expkt(payload=(10,))
    pkt.payload = [1]*10
    pkt.len_payload = 10
    print(pkt)
    return intf.pkt_sendrecv(pkt, dest=0x0F)

def send_ack():
    pkt = tpkts.ack()
    pkt.ack_code = tpkts.ack_codes.ACK_TYPE_INVALIDLEN
    r = intf.pkt_sendrecv(pkt, dest=0x03)
    return r

#print(send_ex())

a = send_ex()
print(a)
