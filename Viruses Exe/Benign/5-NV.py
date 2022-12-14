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


SimplifiedBot.google_search("Pets")
SimplifiedBot.web_search("https://en.wikipedia.org/wiki/Pet")
SimplifiedBot.open_notepad()
SimplifiedBot.download(url=r"data:image/jpeg;base64,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",
                       filename="Pets.jpeg")
SimplifiedBot.close_notepad()
