import pandas

import PyBot as pb

docs = []
columns = ["Source", "Destination", "Protocol"]

df = pandas.read_csv("pcap_test_1.csv")
pb.SimplifiedBot.modify_column(df, "Source", "S: ")
pb.SimplifiedBot.modify_column(df, "Destination", "D: ")
docs.append(df)

df = pandas.read_csv("pcap_test_2.csv")
pb.SimplifiedBot.modify_column(df, "Source", "S: ")
pb.SimplifiedBot.modify_column(df, "Destination", "D: ")
docs.append(df)

df = pandas.read_csv("pcap_test_3.csv")
pb.SimplifiedBot.modify_column(df, "Source", "S: ")
pb.SimplifiedBot.modify_column(df, "Destination", "D: ")
docs.append(df)

# ---------------------testing---------------------
new_csv = pandas.DataFrame()
# single doc, single column
new_csv = pb.SimplifiedBot.tf_idf(docs[0], columns[1])
pandas.DataFrame.to_csv(new_csv, path_or_buf="ss.csv")
print(new_csv)

# multiple doc, single column
new_csv = pb.SimplifiedBot.tf_idf(docs, columns[2])
pandas.DataFrame.to_csv(new_csv, path_or_buf="ms.csv")
print(new_csv)

# single doc, multiple columns
new_csv = pb.SimplifiedBot.tf_idf(docs[0], columns)
pandas.DataFrame.to_csv(new_csv, path_or_buf="sm.csv")
print(new_csv)

# multiple doc, multiple columns
new_csv = pb.SimplifiedBot.tf_idf(docs, columns)
pandas.DataFrame.to_csv(new_csv, path_or_buf="mm.csv")
print(new_csv)

