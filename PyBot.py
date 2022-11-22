"""
Tasks:
 - Google search, websites, images, videos
 - Play YouTube videos
 - Download websites, images, videos
 - Open, close, override, create, and delete notepads
"""

# Imports
import pandas as pd
from re import search
from time import sleep
from numpy import log10, abs
from collections import Counter
from urllib.request import urlretrieve
from webbrowser import open as web_open
from os import system, open as os_open, getcwd


class SimplifiedBot:
    # ----------------Searching----------------
    @staticmethod
    def web_search(url):
        """
            This function opens a new tab with the url if specified
        """
        print("web searching...")
        sleep(15)
        try:
            # opens up the default browser and opens a new tab with the url
            web_open(url)
        except Exception as e:
            # if any error has occurred print it out
            print(e)

    @staticmethod
    def google_search(term=None):
        """
            This google searches the term parameter, if none then just open up google
        """
        print("Google searching...")
        sleep(15)
        # if term is none open a new Google search
        if term is None:
            web_open(url="www.google.com")
        # else search on Google
        else:
            try:
                # this appends the search term to the link, creating a link where it opens up googles search results
                web_open(url="https://www.google.com/search?q=" + term)
            except Exception as e:
                # if there is any errors it will print it out
                print(e)

    @staticmethod
    def google_image_search(image=None):
        """
            this function google searches the image parameter on google images, if the image
            parameter is not specified then open up google images
        """
        print("Google image searching...")
        sleep(15)
        # if term is none open a new Google search
        if image is None:
            web_open(url="https://www.google.com/imghp?hl=en&ogbl")
        # else search on Google images
        else:
            try:
                # this appends the search term to the link, creating a link where it opens up googles image search results
                web_open(url="https://www.google.com/search?tbm=isch&q=" + image)
            except Exception as e:
                # if there is any errors it will print it out
                print(e)

    @staticmethod
    def google_video_search(video=None):
        """
            this function google searches the video parameter on google videos, if the video
            parameter is not specified then open up google video
        """
        print("Google video searching...")
        sleep(15)
        # if term is none open a new Google search
        if video is None:
            web_open(url="https://www.google.com/videohp")
        # else search on Google videos
        else:
            try:
                # this appends the search term to the link, creating a link where it opens up googles video search results
                web_open(url="https://www.google.com/search?tbm=vid&q=" + video)
            except Exception as e:
                # if there is any errors it will print it out
                print(e)

    # ----------------Video-Playing----------------
    @staticmethod
    def play_youtube_video(url=None):
        """
           this function opens up a youtube video thru the url parameter,
           if the url is not specified then it opens YouTube's homepage
        """
        print("YouTube searching...")
        sleep(15)
        # if term is none, open YouTube
        if url is None:
            web_open(url="www.youtube.com")
        # else open YouTube link
        else:
            # checks if the url has www.youtube.com in it
            if search("www\.youtube\.com", url):
                try:
                    # opens the youtube link in a new tab
                    web_open(url=url)
                except Exception as e:
                    # if any errors occurred print them out
                    print(e)
            else:
                print("Error: Invalid YouTube link")

    # ----------------NotePad----------------
    @staticmethod
    def open_notepad(path=None):
        """
            this function opens up window's notepad or opens up a txt document when a path is specified
        """
        print("opening notepad...")
        sleep(15)
        # if the path is not specified then open a untitled/default notepad
        if path is None:
            system("start notepad.exe")
        else:
            # checks if it has the '.txt' extension at the end of the path
            if search("\.txt", path):
                try:
                    # it will try to find and open the txt document in the path
                    os_open(path)  # type: ignore
                # if it failed then it will print out the error
                except Exception as e:
                    print(e)
            else:
                print("Error: Invalid notepad path")

    @staticmethod
    def close_notepad():
        """
            this function closes all instances of the notepad program
        """
        print("closing notepad...")
        sleep(15)
        try:
            # this will try to kill all notepad instances
            system("TASKKILL /F /IM notepad.exe")
        # if it failed then print out the error
        except Exception as e:
            print(e)

    # ----------------Operations----------------
    @staticmethod
    def run_virus(virus_name):
        """
            this function runs the virus in the cuckoo machine
        """
        print("running virus...")
        sleep(15)
        # this will look at the path and look for the virus and try to run it
        system("start C:\\Users\\Administrator\\Desktop" + "\\" + virus_name)

    @staticmethod
    def filter_logs(log_path, file_name):
        """
            this function filters paths from a file
        """
        # this will store the file into a variable
        file = open(log_path)
        # this will create a file and be used to store the filtered file
        temp_log = open(file_name, "a")
        # this runs the file line by line
        for line in file:
            # this searches for a valid path in the line
            r = search(r"[A-Z]\:(([\\].*)||([\/].*))\w+\.[A-Za-z0-9]{2,100}", line)
            # if it has been found then store it into the temp file
            if r:
                temp_log.write(r.group() + ".\n")

    @staticmethod
    def download(url, filename, filepath=None):
        """
            this goes and downloads what url the user specifies
        """
        print("downloading...")
        sleep(15)
        # if the user has not specified a download path then we download where the program is stored
        if filepath is None:
            filepath = getcwd()
        try:
            # this creates the path to download
            filepath = filepath + "\\" + filename
            # this downloads the file
            urlretrieve(url, filepath)
        # if the download fails then print out the error
        except Exception as e:
            print(e)

    @staticmethod
    def modify_column(frame, column, string):
        frame[column] = string + frame[column]

    @staticmethod
    def add_target(csv, column, pattern):
        for val in csv[column]:
            if val is pattern:
                csv['Target'] = 1
            else:
                csv['Target'] = 0

    @staticmethod
    def tfidf_logs(corpus):
        new_csv = pd.DataFrame()
        # TF
        for doc in corpus:
            temp = dict(Counter(doc))
            print(doc)
            df = pd.DataFrame.from_dict([temp])
            new_csv = pd.concat([df, new_csv]).fillna(0)

        # IDF
        temp = []
        for col in new_csv.columns:
            idf = 0
            for elm in new_csv[col]:
                if elm != 0:
                    idf += 1
            temp.append(idf)
        for col in new_csv.columns:
            for temp_idf in temp:
                new_csv[col] = new_csv[col].apply(lambda x: abs(x * log10(temp_idf / len(new_csv[col]))))

        return new_csv

    @staticmethod
    def tf_idf(docs, columns):
        unique = dict()
        new_csv = pd.DataFrame()

        # multiple columns ✓
        if type(columns) is type(list()):
            # multiple csv | multiple columns ✓
            if type(docs) is type(list()):
                for csv in docs:
                    temp2 = pd.DataFrame()
                    # Creates the Merge Columns
                    col_name = ''
                    for col in columns:
                        col_name += col + ' '
                    for col in columns:
                        try:
                            temp2[col_name] += csv[col] + ' '
                        except:
                            temp2[col_name] = csv[col] + ' '
                    # TF
                    unique = dict(Counter(temp2[col_name]))
                    df = pd.DataFrame.from_dict([unique])
                    new_csv = pd.concat([df, new_csv]).fillna(0)
                print('-------------------Merge------------------')
                print(temp2)
                print('-------------------TF------------------')
                print(new_csv)
                print('------------------IDF-------------------')

                # IDF
                for col in new_csv.columns:
                    idf = 0
                    for elm in new_csv[col]:
                        if elm != 0:
                            idf += 1
                    new_csv[col] = new_csv[col].apply(lambda x: abs(x * log10(idf / len(new_csv[col]))))
                print('-------------------------------------')

                return new_csv

            # single csv | multiple columns ✓
            else:
                col_name = ''
                for col in columns:
                    col_name += col + ' '
                for col in columns:
                    try:
                        new_csv[col_name] += docs[col] + ' '
                    except:
                        new_csv[col_name] = docs[col]
                # creates a dictionary each key is a unique item, and its value is its frequency in the document
                unique = dict(Counter(new_csv[col_name]))
                # tf-idf
                for key, value in unique.items():  # iterates through the dict
                    # finds the tf
                    tf = value / len(unique.values())
                    # finds the idf
                    idf = value
                    # calculates it and saves it to the existing dict
                    unique[key] = tf * idf
                # turns it into a dataframe
                new_csv = pd.DataFrame(unique, index=[0])
                # returns the dataframe
                return new_csv.fillna(0)

        # singular columns ✓
        else:
            # multiple csv | single column ✓
            if type(docs) is type(list()):
                for csv in docs:  # iterates through each csv
                    # creates a dictionary each key is a unique item, and its value is its frequency in the document
                    unique = dict(Counter(csv[columns]))
                    # tf-idf
                    for key, value in unique.items():  # iterates through the dict
                        # finds the tf
                        tf = value / len(unique.values())
                        # finds the idf
                        idf = value / len(docs)
                        # calculates it and saves it to the existing dict
                        unique[key] = tf * idf
                    # adds it to the dataframe
                    temp = pd.DataFrame.from_dict(unique, orient='index').T

                    if new_csv.empty:
                        new_csv = temp
                    else:
                        new_csv = new_csv.append(unique, ignore_index=True)
                return new_csv.fillna(0)

            # single csv | single column ✓
            else:
                # creates a dictionary each key is a unique item, and its value is its frequency in the document
                unique = dict(Counter(docs[columns]))
                # tf-idf
                for key, value in unique.items():  # iterates through the dict
                    # finds the tf
                    tf = value / len(unique.values())
                    # finds the idf
                    idf = value
                    # calculates it and saves it to the existing dict
                    unique[key] = tf * idf
                # turns it into a dataframe
                new_csv = pd.DataFrame(unique, index=[0])
                # returns the dataframe
                return new_csv.fillna(0)
