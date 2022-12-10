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
"""
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/2/analysis.log", "Cuckoo/Infected/2/dump.csv", "Cuckoo/Snipped/2-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/4/analysis.log", "Cuckoo/Infected/4/dump.csv", "Cuckoo/Snipped/4-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/6/analysis.log", "Cuckoo/Infected/6/dump.csv", "Cuckoo/Snipped/6-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/8/analysis.log", "Cuckoo/Infected/8/dump.csv", "Cuckoo/Snipped/8-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/10/analysis.log", "Cuckoo/Infected/10/dump.csv", "Cuckoo/Snipped/10-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/11/analysis.log", "Cuckoo/Infected/11/dump.csv", "Cuckoo/Snipped/11-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/12/analysis.log", "Cuckoo/Infected/12/dump.csv", "Cuckoo/Snipped/12-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/15/analysis.log", "Cuckoo/Infected/15/dump.csv", "Cuckoo/Snipped/15-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/17/analysis.log", "Cuckoo/Infected/17/dump.csv", "Cuckoo/Snipped/17-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/19/analysis.log", "Cuckoo/Infected/19/dump.csv", "Cuckoo/Snipped/19-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/21/analysis.log", "Cuckoo/Infected/21/dump.csv", "Cuckoo/Snipped/21-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/23/analysis.log", "Cuckoo/Infected/23/dump.csv", "Cuckoo/Snipped/23-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/25/analysis.log", "Cuckoo/Infected/25/dump.csv", "Cuckoo/Snipped/25-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/27/analysis.log", "Cuckoo/Infected/27/dump.csv", "Cuckoo/Snipped/27-V.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Infected/29/analysis.log", "Cuckoo/Infected/29/dump.csv", "Cuckoo/Snipped/29-V.csv")

PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/1/analysis.log", "Cuckoo/Benign/1/dump.csv", "Cuckoo/Snipped/1-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/3/analysis.log", "Cuckoo/Benign/3/dump.csv", "Cuckoo/Snipped/3-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/5/analysis.log", "Cuckoo/Benign/5/dump.csv", "Cuckoo/Snipped/5-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/7/analysis.log", "Cuckoo/Benign/7/dump.csv", "Cuckoo/Snipped/7-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/9/analysis.log", "Cuckoo/Benign/9/dump.csv", "Cuckoo/Snipped/9-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/13/analysis.log", "Cuckoo/Benign/13/dump.csv", "Cuckoo/Snipped/13-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/14/analysis.log", "Cuckoo/Benign/14/dump.csv", "Cuckoo/Snipped/14-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/16/analysis.log", "Cuckoo/Benign/16/dump.csv", "Cuckoo/Snipped/16-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/18/analysis.log", "Cuckoo/Benign/18/dump.csv", "Cuckoo/Snipped/18-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/20/analysis.log", "Cuckoo/Benign/20/dump.csv", "Cuckoo/Snipped/20-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/22/analysis.log", "Cuckoo/Benign/22/dump.csv", "Cuckoo/Snipped/22-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/24/analysis.log", "Cuckoo/Benign/24/dump.csv", "Cuckoo/Snipped/24-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/26/analysis.log", "Cuckoo/Benign/26/dump.csv", "Cuckoo/Snipped/26-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/28/analysis.log", "Cuckoo/Benign/28/dump.csv", "Cuckoo/Snipped/28-NV.csv")
PB.SimplifiedBot.snip_pcap("Cuckoo/Benign/30/analysis.log", "Cuckoo/Benign/30/dump.csv", "Cuckoo/Snipped/30-NV.csv")
