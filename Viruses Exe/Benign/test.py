from os import system
from time import sleep
from webbrowser import open as web_open


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


def run_virus(virus_name):
    """
        this function runs the virus in the cuckoo machine
    """
    print("running virus...")
    sleep(15)
    # this will look at the path and look for the virus and try to run it
    system("start C:\\Users\\Administrator\\Desktop" + "\\" + virus_name)

google_search("cuckoo sandbox")
run_virus("wannacry.exe")
