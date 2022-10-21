import requests
import random
import argparse
import pyperclip
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser(description='Grab random LWN article and copy it to your clipboard.')
parser.add_argument('-c', metavar='Category', type=str,
                    help='Specify kernel (k) or security (s) category')

urls=[]

BASE_URL = "https://lwn.net"
SECURITY_URL = BASE_URL + "/Security/Index/"
KERNEL_URL = BASE_URL + "/Kernel/Index/"


def main():
    args = parser.parse_args()
    category = args.c
    if (category == 'k'):
        url = KERNEL_URL
    elif (category == 's'):
        url = SECURITY_URL
    else:
        print("Please specify either kernel (k) or security (s) category")
        exit(1)

    print("Parsing " + url + "...")
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    entries = soup.find_all(class_="IndexEntry")
    for entry in entries:
        link = entry.find('a')
        urls.append(BASE_URL + link["href"])

    rand_int = random.randrange(0, len(urls))
    pyperclip.copy(urls[rand_int])



if __name__ == "__main__":
    main()