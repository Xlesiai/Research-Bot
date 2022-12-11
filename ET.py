import pandas
import pandas as pd

import PyBot as pb

log_docs = [open("Cuckoo/Logs/Old Logs/2-V.txt"), open("Cuckoo/Logs/Old Logs/4-V.txt"), open(
    "Cuckoo/Logs/Old Logs/6-V.txt"),
            open("Cuckoo/Logs/Old Logs/8-V.txt"), open("Cuckoo/Logs/Old Logs/10-V.txt"), open(
        "Cuckoo/Logs/Old Logs/11-V.txt"),
            open("Cuckoo/Logs/Old Logs/12-V.txt"), open("Cuckoo/Logs/Old Logs/15-V.txt"), open(
        "Cuckoo/Logs/Old Logs/17-V.txt"),
            open("Cuckoo/Logs/Old Logs/19-V.txt"), open("Cuckoo/Logs/Old Logs/21-V.txt"), open(
        "Cuckoo/Logs/Old Logs/23-V.txt"),
            open("Cuckoo/Logs/Old Logs/25-V.txt"), open("Cuckoo/Logs/Old Logs/27-V.txt"), open(
        "Cuckoo/Logs/Old Logs/29-V.txt"),
            open("Cuckoo/Logs/Old Logs/1-NV.txt"), open("Cuckoo/Logs/Old Logs/3-NV.txt"), open(
        "Cuckoo/Logs/Old Logs/5-NV.txt"),
            open("Cuckoo/Logs/Old Logs/7-NV.txt"), open("Cuckoo/Logs/Old Logs/9-NV.txt"), open(
        "Cuckoo/Logs/Old Logs/13-NV.txt"),
            open("Cuckoo/Logs/Old Logs/14-NV.txt"), open("Cuckoo/Logs/Old Logs/16-NV.txt"), open(
        "Cuckoo/Logs/Old Logs/18-NV.txt"),
            open("Cuckoo/Logs/Old Logs/20-NV.txt"), open("Cuckoo/Logs/Old Logs/22-NV.txt"), open(
        "Cuckoo/Logs/Old Logs/24-NV.txt"),
            open("Cuckoo/Logs/Old Logs/26-NV.txt"), open("Cuckoo/Logs/Old Logs/28-NV.txt"), open(
        "Cuckoo/Logs/Old Logs/30-NV.txt")]

pcap_docs = [pd.read_csv("Cuckoo/PCAP/2-V.csv"),   pd.read_csv("Cuckoo/PCAP/4-V.csv"),   pd.read_csv("Cuckoo/PCAP/6-V.csv"),
             pd.read_csv("Cuckoo/PCAP/8-V.csv"),   pd.read_csv("Cuckoo/PCAP/10-V.csv"),  pd.read_csv("Cuckoo/PCAP/11-V.csv"),
             pd.read_csv("Cuckoo/PCAP/12-V.csv"),  pd.read_csv("Cuckoo/PCAP/15-V.csv"),  pd.read_csv("Cuckoo/PCAP/17-V.csv"),
             pd.read_csv("Cuckoo/PCAP/19-V.csv"),  pd.read_csv("Cuckoo/PCAP/21-V.csv"),  pd.read_csv("Cuckoo/PCAP/23-V.csv"),
             pd.read_csv("Cuckoo/PCAP/25-V.csv"),  pd.read_csv("Cuckoo/PCAP/27-V.csv"),  pd.read_csv("Cuckoo/PCAP/29-V.csv"),
             pd.read_csv("Cuckoo/PCAP/1-NV.csv"),  pd.read_csv("Cuckoo/PCAP/3-NV.csv"),  pd.read_csv("Cuckoo/PCAP/5-NV.csv"),
             pd.read_csv("Cuckoo/PCAP/7-NV.csv"),  pd.read_csv("Cuckoo/PCAP/9-NV.csv"),  pd.read_csv("Cuckoo/PCAP/13-NV.csv"),
             pd.read_csv("Cuckoo/PCAP/14-NV.csv"), pd.read_csv("Cuckoo/PCAP/16-NV.csv"), pd.read_csv("Cuckoo/PCAP/18-NV.csv"),
             pd.read_csv("Cuckoo/PCAP/20-NV.csv"), pd.read_csv("Cuckoo/PCAP/22-NV.csv"), pd.read_csv("Cuckoo/PCAP/24-NV.csv"),
             pd.read_csv("Cuckoo/PCAP/26-NV.csv"), pd.read_csv("Cuckoo/PCAP/28-NV.csv"), pd.read_csv("Cuckoo/PCAP/30-NV.csv")]

pcap1_docs = [
    pd.read_csv("Cuckoo/Infected/2/dump.csv"),  pd.read_csv("Cuckoo/Infected/4/dump.csv"),  pd.read_csv("Cuckoo/Infected/6/dump.csv"),
    pd.read_csv("Cuckoo/Infected/8/dump.csv"),  pd.read_csv("Cuckoo/Infected/10/dump.csv"), pd.read_csv("Cuckoo/Infected/11/dump.csv"),
    pd.read_csv("Cuckoo/Infected/12/dump.csv"), pd.read_csv("Cuckoo/Infected/15/dump.csv"), pd.read_csv("Cuckoo/Infected/17/dump.csv"),
    pd.read_csv("Cuckoo/Infected/19/dump.csv"), pd.read_csv("Cuckoo/Infected/21/dump.csv"), pd.read_csv("Cuckoo/Infected/23/dump.csv"),
    pd.read_csv("Cuckoo/Infected/25/dump.csv"), pd.read_csv("Cuckoo/Infected/27/dump.csv"), pd.read_csv("Cuckoo/Infected/29/dump.csv"),
    pd.read_csv("Cuckoo/Benign/1/dump.csv"),  pd.read_csv("Cuckoo/Benign/3/dump.csv"),  pd.read_csv("Cuckoo/Benign/5/dump.csv"),
    pd.read_csv("Cuckoo/Benign/7/dump.csv"),  pd.read_csv("Cuckoo/Benign/9/dump.csv"), pd.read_csv("Cuckoo/Benign/13/dump.csv"),
    pd.read_csv("Cuckoo/Benign/14/dump.csv"), pd.read_csv("Cuckoo/Benign/16/dump.csv"), pd.read_csv("Cuckoo/Benign/18/dump.csv"),
    pd.read_csv("Cuckoo/Benign/20/dump.csv"), pd.read_csv("Cuckoo/Benign/22/dump.csv"), pd.read_csv("Cuckoo/Benign/24/dump.csv"),
    pd.read_csv("Cuckoo/Benign/26/dump.csv"), pd.read_csv("Cuckoo/Benign/28/dump.csv"), pd.read_csv("Cuckoo/Benign/30/dump.csv"),

]
# ---------------------testing---------------------
"""
new_csv = pandas.DataFrame()
new_csv = pb.SimplifiedBot.tfidf_logs(log_docs)
new_csv.to_csv('Cuckoo/Logs/logs.csv')
"""

new_csv = pandas.DataFrame()
new_csv = pb.SimplifiedBot.tf_idf(pcap1_docs, ['Protocol', 'Info'])
new_csv.to_csv('Cuckoo/PCAP/pcap1.csv')
