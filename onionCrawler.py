import requests
import csv
import re
import time

def get_tor_session():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9151'} #tor use port 9050 as default socks port
    return session

def public_test():
    
    #regex pattern for matching numbers
    pattern = "(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}"
    #URLs of websites to crawl
    urls = ['pastebin.com/diff/E34JsqAy', 'pastebin.pl/view/0f9e7cc4']

    #loop through the URLs to fetch the HTML content
    for url in urls:
        
        response = requests.get("http://{}".format(url), timeout=25)
        response.close()
        html_content = response.content

        #search for regex pattern in HTML content
        matches = re.findall(pattern, html_content.decode("ISO-8859-1"))

        #output the matching numbers
        print("Matching numbers on {}:".format(url))
        for match in matches:
            print(match)
        with open('scraped_data.csv', mode = 'a') as file:
            writer = csv.writer(file)
            for match in matches:
                writer.writerow([match])

def onion_test():

    #regex pattern for matching numbers
    pattern = "(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}"

    #URLs of websites to crawl
    data = [line.strip() for line in open("sites2938.txt", 'r')]
    urls = data

    #loop through the URLs and fetch HTML content
    for url in urls:
        time.sleep(5)
        try:
            response = darksession.get("http://{}".format(url), timeout=25)
            response.close()
            html_content = response.content
        except requests.ConnectionError:
            continue

    #search for the regex pattern in the HTML content
    matches = re.findall(pattern, html_content.decode("ISO-8859-1"))

    #output the matching numbers
    print("Matching numbers on {}:".format(url))
    for match in matches:
        print(match)
    with open('scraped_data.csv', mode = 'a') as file:
        writer = csv.writer(file)
        for match in matches:
            writer.writerow([match])

print("Connecting to TOR")
darksession = get_tor_session()
#print("New IP Address is:{}".format(darksession.get("http://httpbin.org/ip").text))
#onion_test()
#public_test()
