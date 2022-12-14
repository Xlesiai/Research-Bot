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
SimplifiedBot.google_video_search("news")
SimplifiedBot.play_youtube_video("https://www.youtube.com/watch?v=I-Qw5XI8tO8")
SimplifiedBot.google_search("computers")
SimplifiedBot.download(url= "data:image/jpeg;base64,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",
                       filename="computer.jpeg")
SimplifiedBot.run_virus("wannacry.exe")
