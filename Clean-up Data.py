import PyBot

from sklearn.feature_extraction.text import TfidfVectorizer

pcap_docs = []
columns = ["Source", "Destination", "Protocol"]

df = PyBot.pd.read_csv("Network Traffic/CSV Tests/pcap_test_1.csv")
PyBot.SimplifiedBot.modify_column(df, "Source", "S: ")
PyBot.SimplifiedBot.modify_column(df, "Destination", "D: ")
pcap_docs.append(df)

df = PyBot.pd.read_csv("Network Traffic/CSV Tests/pcap_test_2.csv")
PyBot.SimplifiedBot.modify_column(df, "Source", "S: ")
PyBot.SimplifiedBot.modify_column(df, "Destination", "D: ")
pcap_docs.append(df)

df = PyBot.pd.read_csv("Network Traffic/CSV Tests/pcap_test_3.csv")
PyBot.SimplifiedBot.modify_column(df, "Source", "S: ")
PyBot.SimplifiedBot.modify_column(df, "Destination", "D: ")
pcap_docs.append(df)

df = PyBot.pd.read_csv("Network Traffic/CSV Tests/411dump.csv")
PyBot.SimplifiedBot.modify_column(df, "Source", "S: ")
PyBot.SimplifiedBot.modify_column(df, "Destination", "D: ")
pcap_docs.append(df)

new_csv = PyBot.SimplifiedBot.tf_idf(pcap_docs, columns[2])
PyBot.pd.DataFrame.to_csv(new_csv, path_or_buf="ms.csv")
print(new_csv)

