import pandas

import PyBot as pb

docs = []
columns = ["Source", "Destination", "Protocol"]
df = pandas.read_csv("pcap_test_1.csv")
docs.append(df)
df = pandas.read_csv("pcap_test_2.csv")
docs.append(df)
df = pandas.read_csv("pcap_test_3.csv")
docs.append(df)

# ---------------------testing---------------------
new_csv = pandas.DataFrame()
# single doc, single column
# new_csv = pb.SimplifiedBot.tf_idf(docs[0], columns[2])

# multiple doc, single column
new_csv = pb.SimplifiedBot.tf_idf(docs, columns[2])

# single doc, multiple columns
# new_csv = pb.SimplifiedBot.tf_idf(docs[0], columns)

# multiple doc, multiple columns
# new_csv = pb.SimplifiedBot.tf_idf(docs, columns)

print(new_csv)