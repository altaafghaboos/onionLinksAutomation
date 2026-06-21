import requests
import random
import re


def scrape(newdata):
    yourquery = newdata

    #because searches typed in search engines involve spaces, we are getting rid of them
    #e.g searching for "credit card" makes it into "credit+card"
    if " " in yourquery:
        yourquery = yourquery.replace(" ", "+")
    #url format below
    #ahmia is the search engine used for onion links
    #is replacing "{}" with the value of yourquery
    url = "https://ahmia.fi/search/?q={}".format(yourquery)

    #adding fake user-agent headers to prevent Ahmia from recognising script as bot
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    #passing headers into the get request
    request = requests.get(url, headers=headers)
    #returning the url in a readable form
    content = request.text

    #checking for onion links
    '''regexquery = "\w+\.onion"'''     #is the pattern to be looked for
    regexquery = "[a-z2-7]{56}\.onion"  #to catch modern links
    mineddata = re.findall(regexquery, content) #the search function

    #making sure that script is reusable
    #random number to make sure that filename is not repeated
    n = random.randint(1, 9999)
    filename = "sites{}.txt".format(str(n))
    print("Saving to ... ", filename)

    #converting into dictionary to remove duplicates (dict cannot have duplicates)
    #converting back to list mineddata
    mineddata = list(dict.fromkeys(mineddata))

    #writing the content of the list into a file
    for k in mineddata:         #iterates through the list
        with open(filename, "a") as newfile:
            k = k + "\n"        #forcing link to be written on new line
            newfile.write(k)    #writing the link at index k
    print("All the files written to a text file: ", filename)


    #displaying the content
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
        head = lines[:5]
        contents = '\n'.join(head)
        print("\n--- Preview of First 5 Links ---")
        print(contents if contents else "[No links found]")
        '''head = [next(input_file) for x in range(5)] #read only the first 5 values
        contents = '\n'.join(map(str, head)) #remove the '\n'
        print(contents)'''
    


newdata = input("[*] Please Enter Your Query: ")
scrape(newdata)
