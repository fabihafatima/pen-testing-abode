import requests as req
import re
import urllib.parse


subdomain_list = []
subdir_list = []
target_links_list = []


url = input("Enter the website you wish to exlpoit\n")
protocol_id1 = "http://"
protocol_id2 = "https://"
if protocol_id1 not in url or protocol_id2 not in url:
    target_url = "http://" + url
else:
    target_url = url
    

# Check if the site is responding
def request(URL):
    try: 
        return req.get(URL)
    except req.exceptions.ConnectionError:
        pass
    

# Explore sub-domains
with open("C:\MyKaliProg\WebCrawler\wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        if protocol_id1 in target_url:
            temp = target_url.split("http://")[1]
        else:
            temp = target_url.split("https://")[1]

        test_url = "http://" + word + "." + temp 

        response = request(test_url)
        if response:
            subdomain_list.append(test_url)
            #print("[+] Discovered Subdomain --> " + test_url)
print(*subdomain_list, sep = "\n")
print ("______________________________________________________________")


# Explore sub-directories
with open("C:\MyKaliProg\WebCrawler\common.txt", "r") as subdir_file:
    for line in subdir_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            subdir_list.append(test_url)
            #print("[+] Discovered URL --> " + test_url)
print(*subdir_list, sep = "\n")
print ("______________________________________________________________")


# Extracting all the hyperlinks from a website
def extract_links_from(target_url):
    response = req.request('GET', target_url)
    return re.findall(rb'(?:href=")(.*?)"', response.content)
def crawl(target_url):
    href_links = extract_links_from(target_url)
    for link in href_links:
        link = urllib.parse.urljoin(str(target_url), str(link)) #to expand the relative links
    
# To remove the tab links displayed separately, to avoid redundant links
        if "#" in link:
            link = link.split("#")[0] 
        if target_url in link and link not in target_links_list:
            
# To print only the relevant links
            target_links_list.append(link)      
    print(*target_links_list, sep = "\n")
crawl(target_url)
