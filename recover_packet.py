import pyshark
import pandas as pd


#capture = pyshark.LiveCapture('eth0', bpf_filter='ip and tcp port 80')
#capture.sniff(timeout=120)
capture = pyshark.FileCapture('/tmp/mycapture.pcap', display_filter='tcp.port == 80 || udp.port == 80')

# DataFrame
csv_data = ['protocole', 'port', 'ip', 'entete']
data = pd.DataFrame(columns=csv_data)

for packet in capture:
    try:
        data = data.append(
            {
                'protocole' : packet.transport_layer,
                'port' : packet[packet.transport_layer].srcport,
                'ip' : packet.ip.src,
                'entete' : packet.tcp.segment_data.checksum
                #encapsulation = 
                #contenu =
            }, ignore_index=True       
        )
    except AttributeError:
        continue    

#print(data.head())
#print(data.shape)

data.to_csv("./data/tcp.csv")






