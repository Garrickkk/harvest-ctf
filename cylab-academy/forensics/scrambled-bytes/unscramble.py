
import random
from scapy.all import rdpcap, IP, UDP, Raw

packets =[
    p for p in rdpcap("capture.pcapng")
    if IP in p and UDP in p and Raw in p
    and p[IP].src == "172.17.0.2" and p[IP].dst == "172.17.0.3"
    and p[UDP].dport == 56742 and len(p[Raw].load) == 1
]
count =len(packets)
first_time= int(packets[0].time)
print(count, "packets, first sent at", first_time)

for seed in range(first_time - 10, first_time + 2):
    random.seed(seed)
    order = list(range(count))
    random.shuffle(order)
    if random.randrange(65536) == packets[0][UDP].sport:
        print("seed found:", seed)
        break
else:
    raise SystemExit("no seed matched")

random.seed(seed)
order = list(range(count))
random.shuffle(order)
original= bytearray(count)
mismatches = 0
for position, packet in zip(order, packets):
    if random.randrange(65536) !=packet[UDP].sport:
        mismatches += 1
    original[position] =packet[Raw].load[0]^random.randrange(256)

print("source port mismatches:", mismatches)
open("flag.out", "wb").write(original)
