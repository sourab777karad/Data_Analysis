import requests

def fetch(url, path): 
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)
url = "https://www.iplt20.com/"

fetch(url, "Data/ipl.html")