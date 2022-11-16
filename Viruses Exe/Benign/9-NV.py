"""
Tasks:
 - Google search, websites, images, videos
 - Play YouTube videos
 - Download websites, images, videos
 - Open, close, override, create, and delete notepads
"""

# Imports
from re import search
from time import sleep
# from urllib.request import urlretrieve
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
            #urlretrieve(url, filepath)
        # if the download fails then print out the error
        except Exception as e:
            print(e)

SimplifiedBot.google_search()
SimplifiedBot.google_video_search("cat videos")
SimplifiedBot.play_youtube_video("https://www.youtube.com/watch?v=uHKfrz65KSU")
SimplifiedBot.google_search("malls near me")
SimplifiedBot.download(url= "data:image/jpeg;base64,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",
                             filename="mall.jpeg")