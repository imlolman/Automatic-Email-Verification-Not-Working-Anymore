from fake_useragent import UserAgent
import AutomaticEmailVerification as aev
import re
import requests
import json
import register as reg
import urllib3
import random
urllib3.disable_warnings()

counter = 0

for i in range(0, 50):
    print('Getting Users')
    users = json.loads(requests.get(
        'https://randomuser.me/api/?results=50&inc=name&nat=us').text)["results"]

    for user in users:
        try:
            uname = user["name"]["first"] + ' ' + user["name"]["last"]
            umail = user["name"]["first"] + \
                user["name"]["last"] + \
                    str(random.randrange(0, 50)) + '@provmail.net'
            registration = reg.register(
                user["name"]["first"], user["name"]["last"], umail)
            if(registration == False):
                continue

            email = aev.fetch(umail)
            if(email == False):
                continue
            body = email[0]["body"]

            startingText = '<a href=\"'
            endingText = '\"'
            expression = '(?<='+startingText+')(.|\s)*?(?='+endingText+')'
            searchForSelect = re.search(expression, body)

            verificationLink = searchForSelect.group(0).strip()
            open('allDone/verificationLinks', 'a+').write(verificationLink)
            headers = {'User-Agent': UserAgent().random}
            result = requests.get(verificationLink, headers=headers).text
            counter += 1
            open('allDone/names', 'a+').write('\n'+str(counter) + ' ' + uname)
            print('User '+str(counter)+' Verified')
        except:
            continue
