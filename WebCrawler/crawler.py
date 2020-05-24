#!/usr/bin/python3
import sys
import argparse                                                 #Command line arguments
import requests as req
import re
import urllib.parse


subdomain_list = []
subdir_list = []
target_links_list = []


# Command line arguments
parser = argparse.ArgumentParser(description='Small python script to crawl a website.')
parser.add_argument('url', metavar='url', type=str, help="url to crawl")
parser.add_argument('-wd', '--dirlist', help="wordlist for directory enumeration", type=str)
parser.add_argument('-ws', '--domainlist', help="wordlist for subdomain enumeration", type=str)
args = parser.parse_args()

# Code
protocol_id1 = "http://"
protocol_id2 = "https://"
if protocol_id1 not in args.url or protocol_id2 not in args.url:
    target_url = "http://" + args.url
else:
    target_url = args.url
    

# Check if the site is responding
def request(URL):
    try: 
        return req.get(URL)
    except req.exceptions.ConnectionError:
        pass
    
# Explore sub-domains
domainlist = args.domainlist if args.domainlist else "wordlist.txt"
with open(domainlist, "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        print('\r'+word, flush=False, end='')
        sys.stdout.write('\033[2K\033[1G')                                  #To know it's running
        if protocol_id1 in target_url:
            temp = target_url.split("http://")[1]
        else:
            temp = target_url.split("https://")[1]

        test_url = "http://" + word + "." + temp 

        response = request(test_url)
        if response:
            subdomain_list.append(test_url)
            print("[+] Discovered Subdomain --> " + test_url)
print ("______________________________________________________________")


# Explore sub-directories
dirlist = args.dirlist if args.dirlist else "common.txt"
with open(dirlist, "r") as subdir_file:
    for line in subdir_file:
        word = line.strip()
        print('\r' + word, flush=False, end='')
        sys.stdout.write('\033[2K\033[1G')
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            subdir_list.append(test_url)
            print("[+] Discovered URL --> " + test_url)
print ("______________________________________________________________")


# Extracting all the hyperlinks from a website
def extract_links_from(target_url):
    response = req.request('GET', target_url)
    return re.findall(rb'(?:href=")(.*?)"', response.content)

def crawl(target_url):
    href_links = [url.decode('utf-8') for url in extract_links_from(target_url)]        #Convert bytes to str for easy copy-paste
    for link in href_links:
        link = urllib.parse.urljoin(str(target_url), str(link)) #to expand the relative links
        # To remove the tab links displayed separately, to avoid redundant links
        print(link)
        if "#" in link:
            link = link.split("#")[0].decode('utf-8') 
        if target_url in link and link not in target_links_list:
        # To print only the relevant links
            target_links_list.append(link)      
    print(*target_links_list, sep = "\n")

crawl(target_url)
