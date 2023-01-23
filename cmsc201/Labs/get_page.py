import requests

if __name__== "__main__":
    grit_page = requests.get("http://www.umbc.edu").text
    test = grit_page.split('</a>')
    print(len(test)-1)
