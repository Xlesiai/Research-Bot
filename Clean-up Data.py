import PyBot as PB

# pre-encryption logs

PB.SimplifiedBot.filter_logs("Cuckoo/Infected/2/analysis.log", "Cuckoo/Logs/Pre-Encryption/2-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/4/analysis.log", "Cuckoo/Logs/Pre-Encryption/4-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/6/analysis.log", "Cuckoo/Logs/Pre-Encryption/6-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/8/analysis.log", "Cuckoo/Logs/Pre-Encryption/8-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/10/analysis.log", "Cuckoo/Logs/Pre-Encryption/10-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/11/analysis.log", "Cuckoo/Logs/Pre-Encryption/11-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/12/analysis.log", "Cuckoo/Logs/Pre-Encryption/12-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/15/analysis.log", "Cuckoo/Logs/Pre-Encryption/15-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/17/analysis.log", "Cuckoo/Logs/Pre-Encryption/17-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/19/analysis.log", "Cuckoo/Logs/Pre-Encryption/19-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/21/analysis.log", "Cuckoo/Logs/Pre-Encryption/21-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/23/analysis.log", "Cuckoo/Logs/Pre-Encryption/23-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/25/analysis.log", "Cuckoo/Logs/Pre-Encryption/25-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/27/analysis.log", "Cuckoo/Logs/Pre-Encryption/27-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Infected/29/analysis.log", "Cuckoo/Logs/Pre-Encryption/29-V.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/1/analysis.log", "Cuckoo/Logs/Pre-Encryption/1-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/3/analysis.log", "Cuckoo/Logs/Pre-Encryption/3-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/5/analysis.log", "Cuckoo/Logs/Pre-Encryption/5-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/7/analysis.log", "Cuckoo/Logs/Pre-Encryption/7-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/9/analysis.log", "Cuckoo/Logs/Pre-Encryption/9-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/13/analysis.log", "Cuckoo/Logs/Pre-Encryption/13-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/14/analysis.log", "Cuckoo/Logs/Pre-Encryption/14-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/16/analysis.log", "Cuckoo/Logs/Pre-Encryption/16-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/18/analysis.log", "Cuckoo/Logs/Pre-Encryption/18-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/20/analysis.log", "Cuckoo/Logs/Pre-Encryption/20-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/22/analysis.log", "Cuckoo/Logs/Pre-Encryption/22-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/24/analysis.log", "Cuckoo/Logs/Pre-Encryption/24-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/26/analysis.log", "Cuckoo/Logs/Pre-Encryption/26-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/28/analysis.log", "Cuckoo/Logs/Pre-Encryption/28-NV.txt")
PB.SimplifiedBot.filter_logs("Cuckoo/Benign/30/analysis.log", "Cuckoo/Logs/Pre-Encryption/30-NV.txt")

# TF-IDF


log_corpus = [open("Cuckoo/Logs/Pre-Encryption/2-V.txt"), open("Cuckoo/Logs/Pre-Encryption/4-V.txt"), open("Cuckoo/Logs/Pre-Encryption/6-V.txt"),
              open("Cuckoo/Logs/Pre-Encryption/8-V.txt"), open("Cuckoo/Logs/Pre-Encryption/10-V.txt"), open("Cuckoo/Logs/Pre-Encryption/11-V.txt"),
              open("Cuckoo/Logs/Pre-Encryption/12-V.txt"), open("Cuckoo/Logs/Pre-Encryption/15-V.txt"), open("Cuckoo/Logs/Pre-Encryption/17-V.txt"),
              open("Cuckoo/Logs/Pre-Encryption/19-V.txt"), open("Cuckoo/Logs/Pre-Encryption/21-V.txt"), open("Cuckoo/Logs/Pre-Encryption/23-V.txt"),
              open("Cuckoo/Logs/Pre-Encryption/25-V.txt"), open("Cuckoo/Logs/Pre-Encryption/27-V.txt"), open("Cuckoo/Logs/Pre-Encryption/29-V.txt"),

              open("Cuckoo/Logs/Pre-Encryption/1-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/3-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/5-NV.txt"),
              open("Cuckoo/Logs/Pre-Encryption/7-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/9-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/13-NV.txt"),
              open("Cuckoo/Logs/Pre-Encryption/14-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/16-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/18-NV.txt"),
              open("Cuckoo/Logs/Pre-Encryption/20-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/22-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/24-NV.txt"),
              open("Cuckoo/Logs/Pre-Encryption/26-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/28-NV.txt"), open("Cuckoo/Logs/Pre-Encryption/30-NV.txt")]

PB.SimplifiedBot.tfidf_logs(log_corpus).to_csv("Cuckoo/Logs/Pre-Encryption.csv")


# Generalized logs


PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/2-V.txt", "Cuckoo/Logs/Generalized Logs/2-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/4-V.txt", "Cuckoo/Logs/Generalized Logs/4-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/6-V.txt", "Cuckoo/Logs/Generalized Logs/6-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/8-V.txt", "Cuckoo/Logs/Generalized Logs/8-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/10-V.txt", "Cuckoo/Logs/Generalized Logs/10-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/11-V.txt", "Cuckoo/Logs/Generalized Logs/11-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/12-V.txt", "Cuckoo/Logs/Generalized Logs/12-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/15-V.txt", "Cuckoo/Logs/Generalized Logs/15-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/17-V.txt", "Cuckoo/Logs/Generalized Logs/17-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/19-V.txt", "Cuckoo/Logs/Generalized Logs/19-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/21-V.txt", "Cuckoo/Logs/Generalized Logs/21-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/23-V.txt", "Cuckoo/Logs/Generalized Logs/23-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/25-V.txt", "Cuckoo/Logs/Generalized Logs/25-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/27-V.txt", "Cuckoo/Logs/Generalized Logs/27-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/29-V.txt", "Cuckoo/Logs/Generalized Logs/29-V.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/1-NV.txt", "Cuckoo/Logs/Generalized Logs/1-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/3-NV.txt", "Cuckoo/Logs/Generalized Logs/3-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/5-NV.txt", "Cuckoo/Logs/Generalized Logs/5-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/7-NV.txt", "Cuckoo/Logs/Generalized Logs/7-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/9-NV.txt", "Cuckoo/Logs/Generalized Logs/9-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/13-NV.txt", "Cuckoo/Logs/Generalized Logs/13-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/14-NV.txt", "Cuckoo/Logs/Generalized Logs/14-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/16-NV.txt", "Cuckoo/Logs/Generalized Logs/16-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/18-NV.txt", "Cuckoo/Logs/Generalized Logs/18-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/20-NV.txt", "Cuckoo/Logs/Generalized Logs/20-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/22-NV.txt", "Cuckoo/Logs/Generalized Logs/22-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/24-NV.txt", "Cuckoo/Logs/Generalized Logs/24-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/26-NV.txt", "Cuckoo/Logs/Generalized Logs/26-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/28-NV.txt", "Cuckoo/Logs/Generalized Logs/28-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/30-NV.txt", "Cuckoo/Logs/Generalized Logs/30-NV.txt", r"([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", ".../")


# TF-IDF


general_corpus = [open("Cuckoo/Logs/Generalized Logs/2-V.txt"), open("Cuckoo/Logs/Generalized Logs/4-V.txt"), open("Cuckoo/Logs/Generalized Logs/6-V.txt"),
                  open("Cuckoo/Logs/Generalized Logs/8-V.txt"), open("Cuckoo/Logs/Generalized Logs/10-V.txt"), open("Cuckoo/Logs/Generalized Logs/11-V.txt"),
                  open("Cuckoo/Logs/Generalized Logs/12-V.txt"), open("Cuckoo/Logs/Generalized Logs/15-V.txt"), open("Cuckoo/Logs/Generalized Logs/17-V.txt"),
                  open("Cuckoo/Logs/Generalized Logs/19-V.txt"), open("Cuckoo/Logs/Generalized Logs/21-V.txt"), open("Cuckoo/Logs/Generalized Logs/23-V.txt"),
                  open("Cuckoo/Logs/Generalized Logs/25-V.txt"), open("Cuckoo/Logs/Generalized Logs/27-V.txt"), open("Cuckoo/Logs/Generalized Logs/29-V.txt"),

                  open("Cuckoo/Logs/Generalized Logs/1-NV.txt"), open("Cuckoo/Logs/Generalized Logs/3-NV.txt"), open("Cuckoo/Logs/Generalized Logs/5-NV.txt"),
                  open("Cuckoo/Logs/Generalized Logs/7-NV.txt"), open("Cuckoo/Logs/Generalized Logs/9-NV.txt"), open("Cuckoo/Logs/Generalized Logs/13-NV.txt"),
                  open("Cuckoo/Logs/Generalized Logs/14-NV.txt"), open("Cuckoo/Logs/Generalized Logs/16-NV.txt"), open("Cuckoo/Logs/Generalized Logs/18-NV.txt"),
                  open("Cuckoo/Logs/Generalized Logs/20-NV.txt"), open("Cuckoo/Logs/Generalized Logs/22-NV.txt"), open("Cuckoo/Logs/Generalized Logs/24-NV.txt"),
                  open("Cuckoo/Logs/Generalized Logs/26-NV.txt"), open("Cuckoo/Logs/Generalized Logs/28-NV.txt"), open("Cuckoo/Logs/Generalized Logs/30-NV.txt")]

PB.SimplifiedBot.tfidf_logs(general_corpus).to_csv("Cuckoo/Logs/Generalized.csv")

# Removed logs

PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/2-V.txt", "Cuckoo/Logs/Removed Logs/2-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/4-V.txt", "Cuckoo/Logs/Removed Logs/4-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/6-V.txt", "Cuckoo/Logs/Removed Logs/6-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/8-V.txt", "Cuckoo/Logs/Removed Logs/8-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/10-V.txt", "Cuckoo/Logs/Removed Logs/10-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/11-V.txt", "Cuckoo/Logs/Removed Logs/11-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/12-V.txt", "Cuckoo/Logs/Removed Logs/12-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/15-V.txt", "Cuckoo/Logs/Removed Logs/15-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/17-V.txt", "Cuckoo/Logs/Removed Logs/17-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/19-V.txt", "Cuckoo/Logs/Removed Logs/19-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/21-V.txt", "Cuckoo/Logs/Removed Logs/21-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/23-V.txt", "Cuckoo/Logs/Removed Logs/23-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/25-V.txt", "Cuckoo/Logs/Removed Logs/25-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/27-V.txt", "Cuckoo/Logs/Removed Logs/27-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/29-V.txt", "Cuckoo/Logs/Removed Logs/29-V.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/1-NV.txt", "Cuckoo/Logs/Removed Logs/1-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/3-NV.txt", "Cuckoo/Logs/Removed Logs/3-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/5-NV.txt", "Cuckoo/Logs/Removed Logs/5-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/7-NV.txt", "Cuckoo/Logs/Removed Logs/7-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/9-NV.txt", "Cuckoo/Logs/Removed Logs/9-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/13-NV.txt", "Cuckoo/Logs/Removed Logs/13-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/14-NV.txt", "Cuckoo/Logs/Removed Logs/14-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/16-NV.txt", "Cuckoo/Logs/Removed Logs/16-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/18-NV.txt", "Cuckoo/Logs/Removed Logs/18-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/20-NV.txt", "Cuckoo/Logs/Removed Logs/20-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/22-NV.txt", "Cuckoo/Logs/Removed Logs/22-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/24-NV.txt", "Cuckoo/Logs/Removed Logs/24-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/26-NV.txt", "Cuckoo/Logs/Removed Logs/26-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/28-NV.txt", "Cuckoo/Logs/Removed Logs/28-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")
PB.SimplifiedBot.generalize("Cuckoo/Logs/Pre-Encryption/30-NV.txt", "Cuckoo/Logs/Removed Logs/30-NV.txt", r"[A-Za-z]\:(\\|\/){1,2}([A-Za-z0-9-_~ @]+(\\|\/){1,2})+", "")

# TF-IDF

removed_corpus = [open("Cuckoo/Logs/Removed Logs/2-V.txt"), open("Cuckoo/Logs/Removed Logs/4-V.txt"), open("Cuckoo/Logs/Removed Logs/6-V.txt"),
                  open("Cuckoo/Logs/Removed Logs/8-V.txt"), open("Cuckoo/Logs/Removed Logs/10-V.txt"), open("Cuckoo/Logs/Removed Logs/11-V.txt"),
                  open("Cuckoo/Logs/Removed Logs/12-V.txt"), open("Cuckoo/Logs/Removed Logs/15-V.txt"), open("Cuckoo/Logs/Removed Logs/17-V.txt"),
                  open("Cuckoo/Logs/Removed Logs/19-V.txt"), open("Cuckoo/Logs/Removed Logs/21-V.txt"), open("Cuckoo/Logs/Removed Logs/23-V.txt"),
                  open("Cuckoo/Logs/Removed Logs/25-V.txt"), open("Cuckoo/Logs/Removed Logs/27-V.txt"), open("Cuckoo/Logs/Removed Logs/29-V.txt"),

                  open("Cuckoo/Logs/Removed Logs/1-NV.txt"), open("Cuckoo/Logs/Removed Logs/3-NV.txt"), open("Cuckoo/Logs/Removed Logs/5-NV.txt"),
                  open("Cuckoo/Logs/Removed Logs/7-NV.txt"), open("Cuckoo/Logs/Removed Logs/9-NV.txt"), open("Cuckoo/Logs/Removed Logs/13-NV.txt"),
                  open("Cuckoo/Logs/Removed Logs/14-NV.txt"), open("Cuckoo/Logs/Removed Logs/16-NV.txt"), open("Cuckoo/Logs/Removed Logs/18-NV.txt"),
                  open("Cuckoo/Logs/Removed Logs/20-NV.txt"), open("Cuckoo/Logs/Removed Logs/22-NV.txt"), open("Cuckoo/Logs/Removed Logs/24-NV.txt"),
                  open("Cuckoo/Logs/Removed Logs/26-NV.txt"), open("Cuckoo/Logs/Removed Logs/28-NV.txt"), open("Cuckoo/Logs/Removed Logs/30-NV.txt")]

PB.SimplifiedBot.tfidf_logs(removed_corpus).to_csv("Cuckoo/Logs/Removed.csv")


# filter pcap

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
"""
