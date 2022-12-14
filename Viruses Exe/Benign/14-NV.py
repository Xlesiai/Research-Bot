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

SimplifiedBot.google_search("Cars")
SimplifiedBot.web_search("https://en.wikipedia.org/wiki/Cars_(film)")
SimplifiedBot.google_image_search("Cars")
SimplifiedBot.download("data:image/jpeg;base64,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")
SimplifiedBot.open_notepad()
SimplifiedBot.google_video_search("Cars")
SimplifiedBot.play_youtube_video("https://www.youtube.com/watch?v=2LeOH9AGJQM")
