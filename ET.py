import pandas as pd
import PyBot as pb





docs = []
df = pd.read_csv("M:\\School\\2022 Fall\\RISE\\pcap_test_1.csv")
docs.append(df)
df = pd.read_csv("M:\\School\\2022 Fall\\RISE\\pcap_test_2.csv")
docs.append(df)
df = pd.read_csv("M:\\School\\2022 Fall\\RISE\\pcap_test_3.csv")
docs.append(df)
new_csv = pb.SimplifiedBot.tf_idf(docs, "Protocol")
print(new_csv)


