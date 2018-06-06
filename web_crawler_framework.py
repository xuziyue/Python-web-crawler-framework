import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() # if status != 200, raise HTTP ERROR
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "HTTP ERROR"

if __name__ == "__main__":
    url = "http://www.google.com"
    print(getHTMLText(url))
