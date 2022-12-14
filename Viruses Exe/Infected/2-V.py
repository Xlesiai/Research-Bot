
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
SimplifiedBot.google_search("dogs")
SimplifiedBot.run_virus("wannacry.exe")
SimplifiedBot.google_image_search("dogs")
SimplifiedBot.download(
    url=r"data:image/jpeg;base64,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",
    filename="dog.jpeg")
