import requests
import re


def fetch(emailAddress, body=1, subject=1, sender=1, link=1):
    result = requests.get("https://temp-mail.org/en/option/check/",
                          cookies={"mail": emailAddress.replace("@", "%40")}).text
    matchedTable = re.search(
        '(?<=<ul>)((.|\s)*?)(?=</ul>)', result)
    if matchedTable == None:
        return False
        # exit("No Email Table Found on " + emailAddress)
    data = matchedTable.group(0)

    # print(data)
    matchedMails = re.findall(
        "(?<=<li >)((.|\s)*?)(?=<\/li>)", data)
    # print(matchedMails)
    toReturn = []
    for mail in matchedMails:
        link_data = ""
        sender_data = ""
        subject_data = ""
        body_data = ""
        if link:
            link_data = re.search(
                '(?<=href=\")((.|\s)*?)(?=\")', mail[0].strip()).group(0)
        if sender:
            sender_data = re.search(
                "(?<=<span class=\"bullets-ico is-active\"><\/span>)((.|\s)*?)(?=<\/span>)", mail[0].strip()).group(0)
        if subject:
            subject_data = re.search(
                '(?<=<\/small>)((.|\s)*?)(?=<\/span>)', mail[0].strip()).group(0)
        if body:
            request = requests.get(link_data)
            if(request.status_code == 200):
                body_re = re.search(
                    "(?<=<div class=\"inbox-data-content-intro\">)((.|\s)*?)(?=d-none visable-xs-sm mobileAttachments)", request.text)
                if body_re != None:
                    body_data = body_re.group(0)
        toReturn.append({
            "link": link_data,
            "body": body_data,
            "sender": sender_data,
            "subject": subject_data
        })
    return toReturn


def getAvailableDomains():
    url = "https://temp-mail.org/en/option/change/"
    startingText = '<select id="domain" name="domain" class="select-domain">'
    endingText = '</select>'
    expression = '(?<='+startingText+')(.|\s)*?(?='+endingText+')'
    request = requests.get(url)
    if(request.status_code == 200):
        data = request.text
        searchForSelect = re.search(expression, data)
        if searchForSelect != None:
            data = searchForSelect.group(0).strip()
            startingText = '<option value="'
            endingText = '">'
            expression = '(?<='+startingText+')(.*)(?='+endingText+')'
            searchForOptions = re.findall(expression, data)
            if searchForOptions != None:
                data = searchForOptions
                return data
            else:
                exit("Can't Search For Options")
        else:
            exit("Can't Search For Select")
    else:
        exit("Can't Fatch the url "+url)


def getADomain():
    return getAvailableDomains()[0]

# Source: https://github.com/imlolman/Automatic-Email-Verification
