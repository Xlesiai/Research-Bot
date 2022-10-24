"""
Tasks:
 - Google search, websites, images, videos
 - Play YouTube videos
 - Download websites, images, videos
 - Open, close, override, create, and delete notepads
 - ReadME.md
"""

# Imports
from os import system, open as os_open, getcwd
from re import search
from time import sleep
from webbrowser import open as web_open
from urllib.request import urlretrieve


class SimplifiedBot:
    # ----------------Searching----------------
    """
    This opens a new tab with the url
    """
    @staticmethod
    def web_search(url):
        print("web searching...")
        sleep(15)
        try:
            # opens up the default browser and opens a new tab with the url
            web_open(url)
        except Exception as e:
            # if any error has occurred print it out
            print(e)

    """
        This google searches the term parameter, if none then just open up google
    """
    @staticmethod
    def google_search(term=None):
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

    """
        this function google searches the image parameter on google images, if the image
        parameter is not specified then open up google images
    """
    @staticmethod
    def google_image_search(image=None):
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

    """
        this function google searches the video parameter on google videos, if the video
        parameter is not specified then open up google video
    """
    @staticmethod
    def google_video_search(video=None):
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
    """
    this function opens up a youtube video thru the url parameter, if the url is not specified then it opens youtube's homepage
    """
    @staticmethod
    def play_youtube_video(url=None):
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
        print("opening notepad...")
        sleep(15)
        if path is None:
            system("start notepad.exe")
        else:
            if search("\.txt", path):
                try:
                    os_open(path)
                except Exception as e:
                    print(e)
            else:
                print("Error: Invalid notepad path")

    @staticmethod
    def close_notepad():
        print("closing notepad...")
        sleep(15)
        try:
            system("TASKKILL /F /IM notepad.exe")
        except Exception as e:
            print(e)

    # ----------------Operations----------------
    @staticmethod
    def download(url, filename, filepath=None):
        print("downloading...")
        sleep(15)
        if filepath is None:
            filepath = getcwd()
        try:
            filepath = filepath + "\\" + filename
            urlretrieve(url, filepath)
        except Exception as e:
            print(e)

    @staticmethod
    def open_file(path):
        print("opening...")
        sleep(15)
        try:
            os_open(path)
        except Exception as e:
            print(e)

    @staticmethod
    def run_virus(virus_name):
        print("running virus...")
        sleep(15)
        system("start C:\\Users\\Administrator\\Desktop" + "\\" + virus_name)

    @staticmethod
    def filter_logs(log_path, file_name):
        file = open(log_path)
        temp_log = open(file_name, "a")

        for line in file:
            r = search(r"[A-Z]\:(([\\].*)||([\/].*))\w+\.[A-Za-z0-9]{2,100}", line)
            if r:
                temp_log.write(r.group() + ".\n")

