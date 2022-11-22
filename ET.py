import pandas
import PyBot as pb

log_docs = [open("Cuckoo/Logs/2-V.txt"),   open("Cuckoo/Logs/4-V.txt"),   open("Cuckoo/Logs/6-V.txt"),
            open("Cuckoo/Logs/8-V.txt"),   open("Cuckoo/Logs/10-V.txt"),  open("Cuckoo/Logs/11-V.txt"),
            open("Cuckoo/Logs/12-V.txt"),  open("Cuckoo/Logs/15-V.txt"),  open("Cuckoo/Logs/17-V.txt"),
            open("Cuckoo/Logs/19-V.txt"),  open("Cuckoo/Logs/21-V.txt"),  open("Cuckoo/Logs/23-V.txt"),
            open("Cuckoo/Logs/25-V.txt"),  open("Cuckoo/Logs/27-V.txt"),  open("Cuckoo/Logs/29-V.txt"),
            open("Cuckoo/Logs/1-NV.txt"),  open("Cuckoo/Logs/3-NV.txt"),  open("Cuckoo/Logs/5-NV.txt"),
            open("Cuckoo/Logs/7-NV.txt"),  open("Cuckoo/Logs/9-NV.txt"),  open("Cuckoo/Logs/13-NV.txt"),
            open("Cuckoo/Logs/14-NV.txt"), open("Cuckoo/Logs/16-NV.txt"), open("Cuckoo/Logs/18-NV.txt"),
            open("Cuckoo/Logs/20-NV.txt"), open("Cuckoo/Logs/22-NV.txt"), open("Cuckoo/Logs/24-NV.txt"),
            open("Cuckoo/Logs/26-NV.txt"), open("Cuckoo/Logs/28-NV.txt"), open("Cuckoo/Logs/30-NV.txt")]

pcap_docs = [open("Cuckoo/PCAP/2-V.csv"),   open("Cuckoo/PCAP/4-V.csv"),   open("Cuckoo/PCAP/6-V.csv"),
             open("Cuckoo/PCAP/8-V.csv"),   open("Cuckoo/PCAP/10-V.csv"),  open("Cuckoo/PCAP/11-V.csv"),
             open("Cuckoo/PCAP/12-V.csv"),  open("Cuckoo/PCAP/15-V.csv"),  open("Cuckoo/PCAP/17-V.csv"),
             open("Cuckoo/PCAP/19-V.csv"),  open("Cuckoo/PCAP/21-V.csv"),  open("Cuckoo/PCAP/23-V.csv"),
             open("Cuckoo/PCAP/25-V.csv"),  open("Cuckoo/PCAP/27-V.csv"),  open("Cuckoo/PCAP/29-V.csv"),
             open("Cuckoo/PCAP/1-NV.csv"),  open("Cuckoo/PCAP/3-NV.csv"),  open("Cuckoo/PCAP/5-NV.csv"),
             open("Cuckoo/PCAP/7-NV.csv"),  open("Cuckoo/PCAP/9-NV.csv"),  open("Cuckoo/PCAP/13-NV.csv"),
             open("Cuckoo/PCAP/14-NV.csv"), open("Cuckoo/PCAP/16-NV.csv"), open("Cuckoo/PCAP/18-NV.csv"),
             open("Cuckoo/PCAP/20-NV.csv"), open("Cuckoo/PCAP/22-NV.csv"), open("Cuckoo/PCAP/24-NV.csv"),
             open("Cuckoo/PCAP/26-NV.csv"), open("Cuckoo/PCAP/28-NV.csv"), open("Cuckoo/PCAP/30-NV.csv")]
# ---------------------testing---------------------
new_csv = pandas.DataFrame()
new_csv = pb.SimplifiedBot.tfidf_logs(log_docs)
new_csv.to_csv('Cuckoo/Logs/logs.csv')
print(new_csv)
