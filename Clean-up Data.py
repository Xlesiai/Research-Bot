import PyBot as PB


"""
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/30/analysis.log", "Cuckoo/Logs/2-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/31/analysis.log", "Cuckoo/Logs/4-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/32/analysis.log", "Cuckoo/Logs/6-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/33/analysis.log", "Cuckoo/Logs/8-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/34/analysis.log", "Cuckoo/Logs/10-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/35/analysis.log", "Cuckoo/Logs/11-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/36/analysis.log", "Cuckoo/Logs/12-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/37/analysis.log", "Cuckoo/Logs/15-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/38/analysis.log", "Cuckoo/Logs/17-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/39/analysis.log", "Cuckoo/Logs/19-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/40/analysis.log", "Cuckoo/Logs/21-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/41/analysis.log", "Cuckoo/Logs/23-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/42/analysis.log", "Cuckoo/Logs/25-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/43/analysis.log", "Cuckoo/Logs/27-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/44/analysis.log", "Cuckoo/Logs/29-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/45/analysis.log", "Cuckoo/Logs/1-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/46/analysis.log", "Cuckoo/Logs/3-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/47/analysis.log", "Cuckoo/Logs/5-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/48/analysis.log", "Cuckoo/Logs/7-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/49/analysis.log", "Cuckoo/Logs/9-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/50/analysis.log", "Cuckoo/Logs/13-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/51/analysis.log", "Cuckoo/Logs/14-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/52/analysis.log", "Cuckoo/Logs/16-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/53/analysis.log", "Cuckoo/Logs/18-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/54/analysis.log", "Cuckoo/Logs/20-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/55/analysis.log", "Cuckoo/Logs/22-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/56/analysis.log", "Cuckoo/Logs/24-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/57/analysis.log", "Cuckoo/Logs/26-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/58/analysis.log", "Cuckoo/Logs/28-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/59/analysis.log", "Cuckoo/Logs/30-NV.txt")
"""

pcap_docs = [
    open("Cuckoo/Infected/2/dump.pcap"),  open("Cuckoo/Infected/4/dump.pcap"),  open("Cuckoo/Infected/6/dump.pcap"),
    open("Cuckoo/Infected/8/dump.pcap"),  open("Cuckoo/Infected/10/dump.pcap"), open("Cuckoo/Infected/11/dump.pcap"),
    open("Cuckoo/Infected/12/dump.pcap"), open("Cuckoo/Infected/15/dump.pcap"), open("Cuckoo/Infected/17/dump.pcap"),
    open("Cuckoo/Infected/19/dump.pcap"), open("Cuckoo/Infected/21/dump.pcap"), open("Cuckoo/Infected/23/dump.pcap"),
    open("Cuckoo/Infected/25/dump.pcap"), open("Cuckoo/Infected/27/dump.pcap"), open("Cuckoo/Infected/29/dump.pcap"),
    open("Cuckoo/Benign/1/dump.pcap"),  open("Cuckoo/Benign/3/dump.pcap"),  open("Cuckoo/Benign/5/dump.pcap"),
    open("Cuckoo/Benign/7/dump.pcap"),  open("Cuckoo/Benign/9/dump.pcap"),  open("Cuckoo/Benign/13/dump.pcap"),
    open("Cuckoo/Benign/14/dump.pcap"), open("Cuckoo/Benign/16/dump.pcap"), open("Cuckoo/Benign/18/dump.pcap"),
    open("Cuckoo/Benign/20/dump.pcap"), open("Cuckoo/Benign/22/dump.pcap"), open("Cuckoo/Benign/24/dump.pcap"),
    open("Cuckoo/Benign/26/dump.pcap"), open("Cuckoo/Benign/28/dump.pcap"), open("Cuckoo/Benign/30/dump.pcap")]
