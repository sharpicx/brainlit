# made by sharpicx for indonesian only
# built with love to scrape brainly URLs to get the answers
import os.path
import argparse
import urllib.parse, requests, json, base64
from termcolor import colored, cprint
from bs4 import BeautifulSoup

banner = """▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█ ▄▄▀█ ▄▄▀█ ▄▄▀██▄██ ▄▄▀█ ███▄██▄ ▄
█ ▄▄▀█ ▀▀▄█ ▀▀ ██ ▄█ ██ █ ███ ▄██ █
█▄▄▄▄█▄█▄▄█▄██▄█▄▄▄█▄██▄█▄▄█▄▄▄██▄█"""
header = { 
    "Host": "brainly.co.id",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36"
    #"Cookie": "" 
}
#with open("/opt/Security-Wordlist/") as random_agent:
#   pass
def getCookie(username, password):
    url_payload = "https://brainly.co.id/api/28/api_account/authorize"
    data_login = {
        "username": f"{username}",
        "password": f"{password}", 
        "client_type": 5
    }
    jsonToSend = json.dumps(data_login) # type(jsonToSend) => str
    resR = requests.post(url_payload, headers=header, data=jsonToSend)
    jsonLoad = json.loads(resR.text) # type(converted_json) => dict
    cookiefi = os.path.isfile("cookie.txt")
    if cookiefi == False:
        if resR.status_code == 200: 
            cprint("=> Status: 200 OK", "green", attrs=["bold"])
            cprint("[+] Here it is: {}".format(colored(jsonLoad["Set-Cookie"][:-1], "yellow"), "white", attrs="bold"))
            cookief = jsonLoad["Set-Cookie"][:-1]
            que = colored(input("[+] Wanna save it as a file? [y/n] "), "white")
            if que == "y" or que == "Y":
                with open('cookie.txt', 'w') as cookiet:
                    cookiet.write(cookief)
                cprint("[+] saved!", "cyan")
            else:
                cprint("[-] Ok you have picked out the right decision")
        else:
            cprint("[X] Status: {}".format(resR.status_code), "red", attrs=["bold"])
            resJ = resR.json()
            load_resJ = colored(str(resJ["url"][:-1]), "white")
            cprint("[-] Response => {}".format(load_resJ), "blue", attrs=["bold"])
    else:
        with open("cookie.txt", "r") as openCo:
            if openCo.read():
                cprint("[-] It has cookie inside", "green", attrs=["bold"])

def remove(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(["br", "body", "p", "html"]):
        data.decompose()
    return ' '.join(soup.stripped_strings)

def queryToSendTo(query, counts=int):
    with open("cookie.txt", "r") as cooks:
        url_payload = "https://brainly.co.id/graphql/id"
        query_dicts = { # -> type(query_dicts) => dict
            "query": f"{query}",
            "after": None,
            "first": int(counts)
        }
        json_dicts = json.dumps(query_dicts) # -> type(query_dicts) => str
        encoded_query = urllib.parse.quote(json_dicts)
        data_extensions = { 
                "persistedQuery": {
                "version": 1,
                "sha256Hash": "2e22c88f25e89f006d83db5d97c30bcd5163b2b08619ac1807e67fb6eb4e059e"
            }
        }
        json_extensions = json.dumps(data_extensions)
        encoded_extensions = urllib.parse.quote(json_extensions)
        params = f"?operationName=SearchPage&variables={encoded_query}&extensions={encoded_extensions}"
        payload = url_payload + params
        res = requests.get(payload, headers=header.update({"Cookie": f"{cooks}"}))
        if res.status_code == 200: 
            dataJson = json.loads(res.text)["data"]["questionSearch"]["edges"]
            for i in range(counts):
                dataId = colored(base64.b64decode(str(dataJson[i]["node"]["id"])).decode("utf-8"), "blue", attrs=["bold"])
                databaseId = colored(str(dataJson[i]["node"]["databaseId"]), "blue", attrs=["bold"])
                contentId = colored(str(dataJson[i]["node"]["content"]), "blue", attrs=["bold"])
                urlId = colored(f"https://brainly.co.id/tugas/{databaseId}", "blue", attrs=["bold"])
                authorId = remove(colored(str(dataJson[i]["node"]["author"]["databaseId"]), "blue", attrs=["bold"]))
                
                # totalP = int(json.loads(res.text)["data"]["questionSearch"]["count"])
                # crawlTheNode = json.loads(res.text)["data"]["questionSearch"]["edges"]["node"]
                # print(str(dataJson[0]["node"]["databaseId"]))
                # for i in range(len_cTN):

                cprint("[{}] FOUND!".format(i), "cyan", attrs=["bold"])
                cprint("    [+] dataId => {}".format(dataId), "green", attrs=["bold"])
                cprint("    [+] databaseId => {}".format(databaseId), "green", attrs=["bold"])
                cprint("    [+] contentId => {}".format(contentId.replace("<br />", "")), "green", attrs=["bold"])
                cprint("    [+] authorId => {}".format(authorId), "green", attrs=["bold"])
                cprint("    [+] URL => {}\n".format(urlId), "green", attrs=["bold"])
        else: 
            print(res)
            print("kayanya ada yang salah dalam memasukkan argumen")
def main():
    cprint(banner, "red")
    cprint("created by sharpicx @ mycutestgirl.pics", "magenta", attrs=["bold"])
    cprint("made for receiving similar questions to obtain the answers", "blue", attrs=["underline"]); print("")
    # create the parser
    parser = argparse.ArgumentParser(
        prog="brainlit", 
        usage="python brainlit.py [option] QUERY JUMLAH", 
        description="This tool is dedicated for searching questions within queries and obtaining how much stuff would like to be printed. Afterwards, get the answers that each URLs have been scrapped from brainly.co.id.", 
        epilog="The guy who created this is still staying in love with Ra."
    )
    parser.add_argument(
        '--query', 
        metavar="Q", 
        type=str, 
        help="put some queries as contents to be searched with."
    )
    parser.add_argument(
        '--count', 
        metavar="C", 
        type=int, 
        help="put some numbers down to be printed."
    )
    parser.add_argument(
        '--username',
        metavar="U",
        type=str,
        help="take your username off here"
    )
    parser.add_argument(
        '--password',
        metavar="P",
        type=str,
        help="now, put your password in to login and saving cookie into a file"
    )
    args = parser.parse_args() # parse the list of arguments into an object

    query = args.query 
    counts = args.count
    username = args.username
    password = args.password

    if os.path.isfile("cookie.txt") == True:
        queryToSendTo(query, counts)
    else:
        cprint("[-] If you get this message, it means you have to\nsave a cookie into a file that called as cookie.txt (datadome=)", "magenta", attrs=["dark"])
        cprint("[-] If you get a warn from 403 status\nit means you have been blocked by cloudflare from brainly.co.id.\n", "magenta", attrs=["dark"])
        getCookie(username, password)

    # getCookie(sys.argv[1], sys.argv[2])
    #return queryToSendTo(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
