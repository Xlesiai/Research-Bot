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

SimplifiedBot.google_search("cats")
SimplifiedBot.google_image_search("cats")
SimplifiedBot.download(
    url=r"data:image/jpeg;base64,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",
    filename="cats.jpeg")
