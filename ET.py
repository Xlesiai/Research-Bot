import pandas
import PyBot as pb

docs = []

#df = pandas.read_csv("Cuckoo/Logs/1-NV.txt")
#docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/2-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/3-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/4-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/5-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/6-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/7-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/8-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/9-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/10-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/11-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/12-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/13-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/14-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/15-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/16-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/17-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/18-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/19-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/20-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/21-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/22-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/23-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/24-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/25-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/26-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/27-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/28-NV.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/29-V.txt")
docs.append(df)

df = pandas.read_csv("Cuckoo/Logs/30-NV.txt")
docs.append(df)




# ---------------------testing---------------------
new_csv = pandas.DataFrame()

new_csv = pb.SimplifiedBot.tfidf_logs(docs)
new_csv.to_csv('Cuckoo/Logs/test.csv')
print(new_csv)

